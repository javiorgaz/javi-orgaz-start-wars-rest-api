from models import db

class City(db.Model):
    __tablename__ = 'cities'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30),nullable=False,unique = True)
    population = db.Column(db.Integer)
    planet_id = db.Column(db.Integer,db.ForeignKey('planets.id'))

    planet = db.relationship('Planet',back_populates = 'cities')
    characters = db.relationship('Character',back_populates = 'city')

    def __repr__(self):
        return '<City %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "population":self.population,
            "planet_id":self.planet_id
        }