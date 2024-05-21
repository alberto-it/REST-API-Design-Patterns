from flask import Blueprint
from controllers.product_controller import save, find_all

product_bp = Blueprint("product_bp", __name__)
product_bp.route('/', methods=['POST'])(save)
product_bp.route('/', methods=['GET'])(find_all)