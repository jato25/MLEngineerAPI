from parameters import DATABASE_QUERY
import pyodbc
from parameters import DATABASE_CONNECTION, SPECTED_ORDER_FEATURES

connection = pyodbc.connect(DATABASE_CONNECTION)
db = connection.cursor()

class dbWritter():
    @staticmethod
    def writeResult(predictions, probabilities, data):
        try:
            for pred, prob, order in zip(predictions, probabilities, data['orders']):
                info = []
                for feature in SPECTED_ORDER_FEATURES:
                    info.append(order[feature])
                db.execute(DATABASE_QUERY, *info, int(pred), float(prob))
                connection.commit()
            return "Preditions sucessfully written in the database"
        except:
            return "There was an error writting the results in the database"