import socket

SPECTED_ORDER_FEATURES = ['order_id'
                        ,'store_id'
                        ,'created_at'
                        ,'to_user_distance'
                        ,'to_user_elevation'
                        ,'total_earning']

NUMERIC_ORDER_FEATURES = ['to_user_distance'
                        ,'to_user_elevation'
                        ,'total_earning']

DATE_ORDER_FEATURES = ['created_at']

MODEL_INPUT_FEATURES = ['to_user_distance', 'total_earning']

MODEL = 'model'

DATABASE_CONNECTION = ('Driver={SQL Server};'
                      'Server=' + socket.gethostname() + ';'
                      'Database=RappiML;'
                      'Trusted_Connection=yes;')

DATABASE_QUERY = """INSERT INTO dbo.ordersClassification
                    VALUES(?,?,?,?,?,?,?,?)"""

DOCS_TEMPLATE = {
  "swagger": "2.0",
  "info": {
    "title": "ML Engineer Rappi test API",
    "description": "A simple API that classifies orders",
    "version": "0.0.1",
    "contact": {
      "name": "Javier Tellez",
      "mail": "mailto:ja.tellez@uniandes.edu.co",
    }
  }
}