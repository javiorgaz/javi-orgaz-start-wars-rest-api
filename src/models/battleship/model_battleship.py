from models import db
class Battleship(db.Model):
    __tablename__ = 'battleship'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30),nullable=False,unique = True)
    strenght = db.Column(db.Integer)
    size = db.Column(db.Integer)

    character = db.relationship('Character',back_populates = 'battleship')

    def __repr__(self):
        return '<Battleship %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "strength": self.biome,
            "size":self.planet
        }