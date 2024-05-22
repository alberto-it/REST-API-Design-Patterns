from flask import Flask
from database import db
from schemas import ma
from limiter import limiter
from caching import cache

from models.employee_model import Employee
from models.product_model import Product
from models.order_model import Order
from models.customer_model import Customer
from models.productions_model import Production

from routes.employees_blueprint import empl_bp
from routes.products_blueprint import product_bp
from routes.orders_blueprint import order_bp
from routes.customers_blueprint import customer_bp
from routes.productions_blueprint import production_bp

def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(f'config.{config_name}')

    db.init_app(app)
    ma.init_app(app)
    limiter.init_app(app)
    cache.init_app(app)

    return app

def blueprint_config(app):
    app.register_blueprint(empl_bp, url_prefix='/employees')
    app.register_blueprint(product_bp, url_prefix='/products')
    app.register_blueprint(order_bp, url_prefix='/orders')
    app.register_blueprint(customer_bp, url_prefix='/customers')
    app.register_blueprint(production_bp, url_prefix='/productions')

def config_rate_limit():
    limiter.limit("100 per hour")(empl_bp)
    limiter.limit("100 per hour")(product_bp)
    limiter.limit("100 per hour")(order_bp)
    limiter.limit("100 per hour")(customer_bp)
    limiter.limit("100 per hour")(production_bp)

if __name__ == "__main__":
    app = create_app('DevelopmentConfig')

    blueprint_config(app)
    config_rate_limit()

    with app.app_context(): db.create_all()

    app.run(debug=True)