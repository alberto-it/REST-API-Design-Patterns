from flask import request, jsonify
from schemas.customer_schema import customer_schema, customers_schema
from services import customer_service
from marshmallow import ValidationError
from caching import cache

def save():
    try:
        customer_data = customer_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    customer_save = customer_service.save(customer_data)
    if customer_save is not None:
        return customer_schema.jsonify(customer_save), 201
    else:
        return jsonify({"message": "Fallback method error activated", "body": customer_data}), 400

@cache.cached(timeout=60)
def find_all():
    customers = customer_service.find_all()
    return customers_schema.jsonify(customers), 200