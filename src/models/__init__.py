# este archivo hace que python tome models como un paquete
# en versiones actuales de python, se toma model ya como paquete y no hace falta crear __init__.py, aun asi es buena practica
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import relationship

# SQLAlchemy: Es un ORM (Object-Relational Mapper) que convierte las tablas de la base de datos en objetos de Python

db = SQLAlchemy()

from .user.model_user import User
from .planet.model_planet import Planet