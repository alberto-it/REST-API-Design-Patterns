from marshmallow import fields
from schemas import ma

class EmplSchema(ma.Schema):
    id = fields.Integer(required=False) 
    name = fields.String(required=True)
    position = fields.String(required=True)

    class Meta:
        fields = ("id", "name", "position")

empl_schema = EmplSchema()
empls_schema = EmplSchema(many=True)