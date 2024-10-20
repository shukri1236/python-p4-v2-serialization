
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

# Initialize the SQLAlchemy object
db = SQLAlchemy()

class Pet(db.Model, SerializerMixin):  # Corrected class definition
    __tablename__ = 'pets'  # Define the table name

    id = db.Column(db.Integer, primary_key=True)  # Define the id column
    name = db.Column(db.String)  # Define the name column
    species = db.Column(db.String)  # Define the species column

    def __repr__(self):
        return f'<Pet {self.id}, {self.name}, {self.species}>'  # Properly formatted __repr__ method
    