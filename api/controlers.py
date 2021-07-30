from flask_restful import Resource
from flask import request
from pickle import load
import json
from validators import *
from converters import *
from database import *
from parameters import MODEL

class clasification(Resource):
    def __init__(self) -> None:
        super().__init__()
        self.model = load(open(f'../resources/{MODEL}.pkl', 'rb'))

    def post(self):
        """
        Method to clasify order into taken by a courier (1) or not taken (0)
        It works with one an n samples
        ---
            tags:
              - Order clasification
            parameters:
              - in: body
                name: orders
                type: object
                required: true
                schema:
                    properties:
                        orders:
                            type: array
                            description: An array with all the orders to classify. There must be at least one order
                            items:
                                type: object
                                description: order information that allows classification
                                properties:
                                    order_id:
                                        type: integer
                                        description: Order ID
                                    store_id:
                                        type: integer
                                        description: Store ID of the order
                                    to_user_distance:
                                        type: number
                                        example: 2.4781
                                        description: Distance (km) between store and user location
                                    to_user_elevation:
                                        type: number
                                        example: 21.63
                                        description: Difference in meters between the store and user altitude (m.a.s.l.)
                                    total_earning:
                                        type: number
                                        description: Courier earning by delivering the order
                                        example: 3500
                                    created_at:
                                        type: string
                                        format: date-time
                                        example: "2017-09-07T20:02:17Z"
                                        description: Timestamp of order creation
            responses:
                200:
                    description: An array of orders with their classification and the database result
                    schema:
                        properties:
                            response:
                                type: array
                                description: An array with each classification
                                items:
                                    type: object
                                    description: classification of each order
                                    properties:
                                        order_id:
                                            type: integer
                                            description: Order ID
                                        taken:
                                            type: integer
                                            description: Takes the value of 1 if the order was taken by a courier, 0 otherwise.
                            "database result":
                                type: string
                                description: A message showing if the writting in the database was succesfull
                400:
                    description: A message specifying the error found in the input
                    schema:
                        type: string
                        example: "The 'total_earning' paramater was not found"

                500:
                    description: A message specifying the was an internal error
                    schema:
                        type: string
                        example: "There was an error during the classification task"
        """    
        isValid, message = InputValidator.validate(request)
        if not isValid:
            return message, 400

        data = json.loads(request.data)
        sucessConvertion, modelInput = InputConverter.convert(data)
        if not sucessConvertion:
            return modelInput, 500

        try:
            prediction = self.model.predict(modelInput)
            probabilities = self.model.predict_proba(modelInput)
        except:
            return "There was an error during the classification task", 500

        dbWrittingMessage = dbWritter.writeResult(prediction, probabilities[:,1], data)
        #dbWrittingMessage = "Not avilable"

        successOutConversion, modelOutput = OutputConverter.convert(prediction, data, dbWrittingMessage)
        if not successOutConversion:
            return modelOutput, 500

        return modelOutput, 200
