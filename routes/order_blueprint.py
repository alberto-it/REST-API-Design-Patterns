from flask import Blueprint
from controllers.order_controller import save, find_all

order_blueprint = Blueprint("order_bp", __name__)
order_blueprint.route('/', methods=['POST'])(save)
order_blueprint.route('/', methods=['GET'])(find_all)