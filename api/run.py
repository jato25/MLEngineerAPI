from flask import Flask
from flask_restful import Api
from flasgger import Swagger
from controlers import clasification
from parameters import DOCS_TEMPLATE

app = Flask(__name__)

api = Api(app)
swagger = Swagger(app, template=DOCS_TEMPLATE)

api.add_resource(clasification, '/clasification')

if __name__ == '__main__':
    app.run(debug=True, port=8080)