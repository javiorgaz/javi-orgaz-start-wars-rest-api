from .. import db
from sqlalchemy import Enum
# from .. import relationship

class Planet(db.Model):

    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30),nullable= False,unique = True)
    biome = db.Column(Enum('Dessert', 'Forest', 'Frozen', 'Volcanic', name='biome_enum'), nullable=False)  
    # biome = db.Column(db.Enum('Dessert','Forest','Frozen','Volcanic'))
    # cities = relationship('City',back_populates = 'planet')
    # races = relationship('Race', back_populates = 'planet')

    def __repr__(self):
        return '<Planet %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "biome": self.biome
        }