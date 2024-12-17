# las rutas las vamos a manejar con algo llamado blueprints. Los importamos de flask
# blueprint nos permite manejar las rutas desde aqui y enviarlas a app

from flask import Blueprint,request,jsonify
from models import User,db

# o user_route
#2 parametros: el nombre de la ruta de este modulo / nombre del modulo
user_bp = Blueprint('user1',__name__)

# OBTENER TODA LA LISTA DE USERS
@user_bp.route("/get-all",methods = ["GET"])
def get_all_users():
    # obtenemos una lista de todos los objetos User desde la base de datos
    # la lista contiene instancias del modelo(clase) User recuperadas de la base de datos.
    user_list = User.query.all()
    print(user_list)
    # Convertimos cada objeto User a un diccionario utilizando el método serialize()
    lista_serializada = [user.serialize() for user in user_list]
   # serializamos la lista en formato JSON para enviarla como respuesta HTTP
    return jsonify(lista_serializada)

# OBTENER UN USER
@user_bp.route("/get-user/<int:id>",methods = ["GET"])
def get_user(id):
    # user -> es el modelo 
    # query -> objeto que permite realizar consultas a la base de datos
    # get(id) -> Este es un método de SQLAlchemy que se utiliza para obtener una fila (un registro) de la base de datos según su clave primaria
    user = User.query.get(id)
    diccionario_user = user.serialize()
    return jsonify(diccionario_user)

# CREAR UN USER
@user_bp.route("/create-user",methods = ["POST"])
def create_user():
    # convertimos la respuesta json recibida en un diccionario python
    response = request.get_json()
    # creamos una instancia de user con la respuesta

    # usamos response.get("email") en lugar de response["email"], porque esta ultima lanzara un error KeyError si email no esta presente
    # Este método devuelve None si la clave no existe, en lugar de lanzar una excepción
    if(not response.get("email")):
        return jsonify({"error":"falta el campo email..."}),400
    if(not response.get("password")):
        return "Falta el campo password",400
    if(not response.get("is_active")):
        return "Falta el campo is_active",400
    

    new_user = User(**response)
    # lo guardamos en la base de datos
    db.session.add(new_user)
    db.session.commit()
    print(new_user)
    return "Usuario creado correctamente!"

@user_bp.route("/delete-user/<int:id>",methods = ["DELETE"])
def delete_user(id):
    user_to_delete = User.query.get(id)
    db.session.delete(user_to_delete)
    db.session.commit()
    return "Usuario eliminado correctamente!"


