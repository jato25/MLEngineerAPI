from parameters import SPECTED_ORDER_FEATURES, NUMERIC_ORDER_FEATURES, DATE_ORDER_FEATURES
from datetime import datetime
import json

class InputValidator:
    @staticmethod
    def validate(request):
        try:
            data = json.loads(request.data)
        except:
            return False, "The input data cannot be converted, json format error"

        if not 'orders' in data.keys():
            return False, "The 'orders' parameter was not found"

        if len(data['orders']) == 0:
            return False, "There is not any order inside orders array"

        for order in data['orders']:
            validation, message = OrderValidator.validate(order)
            if not validation:
                return validation, message
        
        return True, ''

class OrderValidator:
    @staticmethod
    def validate(order):
        orderKeys = order.keys()

        for feature in SPECTED_ORDER_FEATURES:
            if feature not in orderKeys:
                return False, f"The '{feature}' paramater was not found"

        order_id = order['order_id']

        for feature in NUMERIC_ORDER_FEATURES:
            try:
                float(order[feature])
            except:
                return False, f"The '{feature}' paramater for order {order_id} does not have the expected type (numeric)"

        for feature in DATE_ORDER_FEATURES:
            try:
                datetime.strptime(order[feature], '%Y-%m-%dT%H:%M:%SZ')
            except:
                return False, f"The '{feature}' paramater for order {order_id} does not have the expected type (date)"

        return True,''