from flask import Blueprint
from flask import request,jsonify
from models import db,Planet

planet_bp = Blueprint('planet1',__name__)


@planet_bp.route('/<int:id>',methods = ["GET"])
def get_one_planet(id):
    planet = Planet.query.get(id)
    serialized_planet = planet.serialize()
    return jsonify({"Tu planeta":serialized_planet})

@planet_bp.route('/get-all',methods = ["GET"])
def get_all_planets():
    planet_list = Planet.query.all()
    serialized_list = [planet.serialize() for planet in planet_list]
    return jsonify({"lista de planetas":serialized_list})

@planet_bp.route('/create-planet',methods = ["POST"])
def create_planet():
    response = request.get_json()
    new_planet = Planet(**response)
    db.session.add(new_planet)
    db.session.commit()
    print(new_planet)
    return "Planeta creado correctamenet"

@planet_bp.route('/delete-planet/<int:id>',methods = ["DELETE"])
def delete_planet(id):
    planeta_borrar = Planet.query.get(id)
    print(planeta_borrar)
    db.session.delete(planeta_borrar)
    db.session.commit()
    return "Planeta borrado correctamente"
