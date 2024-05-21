from flask import request, jsonify
from schemas.schemas import empl_schema, empls_schema
from services import empl_service
from marshmallow import ValidationError
from caching import cache

def save():
    try:
        empl_data = empl_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    empl_save = empl_service.save(empl_data)
    if empl_save is not None:
        return empl_schema.jsonify(empl_save), 201
    else:
        return jsonify({"message": "Fallback method error activated", "body": empl_data}), 400

@cache.cached(timeout=60)
def find_all():
    empls = empl_service.find_all()
    return empls_schema.jsonify(empls), 200