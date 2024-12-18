from .. import db
from sqlalchemy import Enum
from sqlalchemy.orm import relationship

class Planet(db.Model):

    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30),nullable= False,unique = True)
    biome = db.Column(Enum('Dessert', 'Forest', 'Frozen', 'Volcanic', name='biome_enum'), nullable=True)
    population = db.Column(db.Integer)
    cities = db.relationship('City',back_populates = 'planet')
    favourites = db.relationship('Favourite',back_populates = 'planet')
    races = db.relationship('Race',back_populates = 'planet')

    def __repr__(self):
        return '<Planet %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "biome": self.biome,
            "population": self.population,
            "cities": [city.serialize() for city in self.cities],  # Serializa las ciudades asociadas
            "favourites": [favourite.id for favourite in self.favourites],  # Solo los IDs
            "races": [race.serialize() for race in self.races]  # Serializa las razas asociadas
        }