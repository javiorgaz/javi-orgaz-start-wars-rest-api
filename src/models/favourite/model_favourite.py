from models import db

class Favourite(db.Model):
    __tablename__ = 'favourites'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    planet_id = db.Column(db.Integer,db.ForeignKey('planets.id'))
    character_id = db.Column(db.Integer,db.ForeignKey('characters.id'))

    user = db.relationship('User',back_populates = 'favourites')
    planet = db.relationship('Planet',back_populates = 'favourites')
    character = db.relationship('Character',back_populates = 'favourites')

    def __repr__(self):
        return '<Favourite %r>' % self.user

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id,
            "character_id": self.character_id,
        }