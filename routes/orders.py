from flask import Blueprint
from controllers.order_controller import save, find_all

order_bp = Blueprint("order_bp", __name__)
order_bp.route('/', methods=['POST'])(save)
order_bp.route('/', methods=['GET'])(find_all)