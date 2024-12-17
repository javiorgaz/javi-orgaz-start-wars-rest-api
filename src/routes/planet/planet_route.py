from flask import Blueprint
from flask import request,jsonify

planet_bp = Blueprint('planet1',__name__)

@planet_bp.route('/get-all',methods = ["GET"])
def get_all_planets():
    return "Lista de todos los planetas"
