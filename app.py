from flask import Flask
from database import db
from schemas import ma
from limiter import limiter
from caching import cache

from models.models import Employee, Product, Order, Customer, Production

from routes.employees import empl_bp
from routes.products import product_bp
from routes.orders import order_bp
from routes.customers import customer_bp
from routes.productions import production_bp

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