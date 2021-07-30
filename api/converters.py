from parameters import MODEL_INPUT_FEATURES

class InputConverter:
    @staticmethod
    def convert(input):
        data = []
        try:
            for order in input['orders']:
                orderData = []
                for feature in MODEL_INPUT_FEATURES:
                    orderData.append(float(order[feature]))
                data.append(orderData)

            return True, data

        except:
            return False, "There was an error converting the input data"

class OutputConverter:
    @staticmethod
    def convert(output, input, dbMessage):
        data = []
        try:
            for clasification, dataIn in zip(output, input['orders']):
                data.append({"order_id" : dataIn['order_id']
                            ,"taken" : int(clasification)})
            return True, {"response" : data, "database result": dbMessage}
        except:
            return False, "There was an error converting the output data"