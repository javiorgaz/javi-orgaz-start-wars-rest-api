# este archivo hace que python tome models como un paquete
# en versiones actuales de python, se toma model ya como paquete y no hace falta crear __init__.py, aun asi es buena practica
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import relationship

# SQLAlchemy: Es un ORM (Object-Relational Mapper) que convierte las tablas de la base de datos en objetos de Python

db = SQLAlchemy()

from .battleship.model_battleship import Battleship
from .character.model_character import Character
from .city.model_city import City
from .favourite.model_favourite import Favourite
from .planet.model_planet import Planet
from .race.model_race import Race
from .user.model_user import User