from flask import Blueprint,request,jsonify
from models import Planet,Favourite,Character,db

bp_favourite = Blueprint('/favourite',__name__)

# Añadir planeta favorito al user
@bp_favourite.route('/favourite/post-planet/<int:planet_id>',methods = ["POST"])
def post_favourite_planet(planet_id):
    # convertimos el json de la request en un diccionario python
    data = request.get_json()
    user_id = data["user_id"]

    if not user_id:
        return jsonify({"error: tienes que introducir un user"}),

    planet = Planet.query.get(planet_id)
    print(planet)
    if not planet:
        return jsonify({"error": "planeta no encontrado"}), 404
    
    new_favourite_planet = Favourite(user_id = user_id,planet_id = planet_id)
    db.session.add(new_favourite_planet)
    db.session.commit()

    return jsonify({"planeta añadido":planet.serialize()})


# Añadir character favorito al user
@bp_favourite.route('/favourite/post-character/<int:character_id>',methods = ["POST"])
def post_favourite_character(character_id):
    # convertimos el json de la request en un diccionario python
    data = request.get_json()
    user_id = data["user_id"]

    if not user_id:
        return jsonify({"error: tienes que introducir un user"}),

    character = Character.query.get(character_id)
    if not character:
        return jsonify({"error": "character no encontrado"}), 404
    
    new_favourite_character = Favourite(user_id = user_id,character_id = character_id)
    db.session.add(new_favourite_character)
    db.session.commit()

    return jsonify({"character añadido":character.serialize()})

# delete favourite planet
@bp_favourite.route('/favourite/delete-planet/<int:planet_id>',methods = ["DELETE"])
def delete_favourite_planet(planet_id):
    favourites = Favourite.query.filter(Favourite.planet_id == planet_id).all()
    
    if not favourites:
        return jsonify({"error":"planeta no encontrado"})
    
    for favourite in favourites:
        db.session.delete(favourite)

    db.session.commit()
 
    return "Planeta eliminado de la lista de favoritos correctamente"

# delete favourite characters
@bp_favourite.route('/favourite/delete-character/<int:character_id>',methods = ["DELETE"])
def delete_favourite_character(character_id):
    favourites = Favourite.query.filter(Favourite.character_id == character_id).all()
    
    if not favourites:
        return jsonify({"error":"character no encontrado"})

    for favourite in favourites:
        db.session.delete(favourite)

    db.session.commit()
 
    return "Character eliminado de la lista de favoritos correctamente"


# esto lo he hecho para probar la lista de characters
@bp_favourite.route('/characters',methods = ["GET"])
def get_characters():
    characters = Character.query.all()

    lista = [char.serialize() for char in characters]

    return jsonify({"lista de personajes":lista})


