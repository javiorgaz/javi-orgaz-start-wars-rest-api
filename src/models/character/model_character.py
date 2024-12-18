from models import db

class Character(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30),nullable=False,unique = True)
    age = db.Column(db.Integer)
    race_id = db.Column(db.Integer,db.ForeignKey('races.id'))
    city_id = db.Column(db.Integer,db.ForeignKey('cities.id'))
    battleship_id = db.Column(db.Integer,db.ForeignKey('battleship.id'))
    
    race = db.relationship('Race',back_populates = 'characters')
    city = db.relationship('City',back_populates = 'characters')
    battleship = db.relationship('Battleship',back_populates = 'character')
    favourites = db.relationship('Favourite',back_populates = 'character')

    def __repr__(self):
        return '<Character %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.biome,
            "race_id":self.race_id,
            "city_id":self.city_id,
            "battleship_id":self.battleship_id
        }