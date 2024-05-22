from flask import request, jsonify
from schemas.order_schema import order_schema, orders_schema
from services import order_service
from marshmallow import ValidationError

def save():
    try:
        order_data = order_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    new_order = order_service.save(order_data)

    return order_schema.jsonify(new_order), 201

def find_all():
    args = request.args
    page = args.get('page', 1, type=int)
    per_page = args.get('per_page', 10, type=int)
    search_term = args.get('search')
    orders = order_service.find_all(page, per_page, search_term)
    return orders_schema.jsonify(orders), 200