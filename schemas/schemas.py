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

class ProductSchema(ma.Schema):
    id = fields.Integer(required=False) 
    name = fields.String(required=True)
    price = fields.Float(required=True)

    class Meta:
        fields = ("id", "name", "price")

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

class OrderSchema(ma.Schema):
    id = fields.Integer(required=False) 
    customer_id = fields.Integer(required=True)
    product_id = fields.Integer(required=True)
    quantity = fields.Integer(required=True)
    total_price = fields.Float(required=True)

    class Meta:
        fields = ("id", "customer_id", "product_id", "quantity","total_price")

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)

class CustomerSchema(ma.Schema):
    id = fields.Integer(required=False) 
    name = fields.String(required=True)
    email = fields.String(required=True)
    phone = fields.String(required=True)

    class Meta:
        fields = ("id", "name", "email", "phone")

customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)

class ProductionSchema(ma.Schema):
    id = fields.Integer(required=False) 
    product_id = fields.Integer(required=True)
    quantity_produced = fields.Integer(required=True)
    date_produced = fields.Date(required=True)

    class Meta:
        fields = ("id", "product_id", "quantity_produced", "date_produced")

production_schema = ProductionSchema()
productions_schema = ProductionSchema(many=True)