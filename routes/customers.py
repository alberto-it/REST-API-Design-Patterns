from flask import Blueprint
from controllers.customer_controller import save, find_all

customer_bp = Blueprint("customer_bp", __name__)
customer_bp.route('/', methods=['POST'])(save)
customer_bp.route('/', methods=['GET'])(find_all)