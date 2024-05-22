from flask import request, jsonify
from schemas.production import production_schema, productions_schema
from services import production_service
from marshmallow import ValidationError
from caching import cache

def save():
    try:
        production_data = production_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    production_save = production_service.save(production_data)
    if production_save is not None:
        return production_schema.jsonify(production_save), 201
    else:
        return jsonify({"message": "Fallback method error activated", "body": production_data}), 400

@cache.cached(timeout=60)
def find_all():
    productions = production_service.find_all()
    return productions_schema.jsonify(productions), 200