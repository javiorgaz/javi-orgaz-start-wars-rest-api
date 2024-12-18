from .. import db
from sqlalchemy.orm import relationship

class Race(db.Model):

    __tablename__ = 'races'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30),nullable= False,unique = True)
    avg_height = db.Column(db.Integer)
    skin_color = db.Column(db.String(30))
    planet_id = db.Column(db.Integer,db.ForeignKey('planets.id'))

    planet = db.relationship('Planet',back_populates = 'races')
    characters = db.relationship('Character',back_populates = 'race')

    def __repr__(self):
        return '<Race %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "avg_height": self.avg_height,
            "skin_color": self.skin_color,
            "planet_id": self.planet_id
        }