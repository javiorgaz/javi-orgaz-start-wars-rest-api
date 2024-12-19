"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
# esto se hace asi gracias a que models actua como modulo, si no, habria que importar las clases o tablas una a una
from models import db, User,Planet
#from models import Person
from routes import user_bp,planet_bp,bp_favourite

# ESTA todo MUY COMENTADO SRRY PERO ES PARA ENTENDERLO todo OK

app = Flask(__name__)
app.url_map.strict_slashes = False

# con os accedemos a env

db_url = os.getenv("DATABASE_URL")

if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(user_bp,url_prefix = "/user")
app.register_blueprint(planet_bp,url_prefix = "/planet")
app.register_blueprint(bp_favourite)

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
