
from flask import Flask, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import db, Pet  # Ensure Pet is imported from your models.py

app = Flask(__name__)

# Configuration for SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  # Adjust as needed
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Add views here 
@app.route('/')
def index():
    body = {'message': 'Welcome to the pet directory!'}
    return jsonify(body)  # Use jsonify to return a JSON response

@app.route('/pets/<int:id>')
def pet_by_id(id):
    pet = Pet.query.filter(Pet.id == id).first()
    if pet:
        response_body = {'name': pet.name, 'species': pet.species}
        response_status = 200
    else:
        response_body = {'message': f'Pet {id} not found'}
        response_status = 404
        
    response = make_response(jsonify(response_body), response_status)  # Return JSON response
    return response

@app.route('/species/<string:species>')
def pet_by_species(species):
    pets = Pet.query.filter_by(species=species).all()
    
    size = len(pets)
    response_body = {'count': size, 'species': species, 'pets': [pet.name for pet in pets]}  # Create a JSON response
    response = make_response(jsonify(response_body), 200)  # Return JSON response
    return response

if __name__ == '__main__':
    app.run(port=5555, debug=True)
