from flask import Blueprint
from controllers.production_controller import save, find_all

production_bp = Blueprint("production_bp", __name__)
production_bp.route('/', methods=['POST'])(save)
production_bp.route('/', methods=['GET'])(find_all)