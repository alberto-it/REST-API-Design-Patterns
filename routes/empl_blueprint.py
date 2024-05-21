from flask import Blueprint
from controllers.empl_controller import save, find_all

empl_blueprint = Blueprint("empl_bp", __name__)
empl_blueprint.route('/', methods=['POST'])(save)
empl_blueprint.route('/', methods=['GET'])(find_all)