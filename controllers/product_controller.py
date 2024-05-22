from flask import request, jsonify
from schemas.product import product_schema, products_schema
from services import product_service
from marshmallow import ValidationError
from caching import cache

def save():
    try:
        product_data = product_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    product_save = product_service.save(product_data)
    if product_save is not None:
        return product_schema.jsonify(product_save), 201
    else:
        return jsonify({"message": "Fallback method error activated", "body": product_data}), 400

@cache.cached(timeout=60)
def find_all():
    products = product_service.find_all()
    return products_schema.jsonify(products), 200