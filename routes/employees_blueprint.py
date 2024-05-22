from flask import Blueprint
from controllers.empl_controller import save, find_all

empl_bp = Blueprint("empl_bp", __name__)
empl_bp.route('/', methods=['POST'])(save)
empl_bp.route('/', methods=['GET'])(find_all)