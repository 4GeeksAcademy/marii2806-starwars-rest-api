from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
            "username": self.username,
            "favorites": [favorite.serialize() for favorite in self.favorites]
        }

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.db.String(250), nullable=False)
    height = db.Column(db.Integer, nullable=False)
    mass = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(50))
    eye_color = db.Column(db.String(50), nullable=False)
    hair_color = db.Column(db.String(50), nullable=False)
    skin_color = db.Column(db.String(50), nullable=False)
    birth_year = db.Column(db.Integer, nullable=False)
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'), nullable=False)
    # vehicles = db.relationship('Vehicle', backref='character', uselist=False)
    favorites = db.relationship('Favorite', backref='character', lazy=True)

    def serialize(self):
        return{
            'id': self.id,
            'name': self.name,
            'height': self.height,
            'mass': self.mass,
            'gender': self.gender,
            'eye_color': self.eye_color,
            'hair_color': self.hair_color,
            'skin_color': self.skin_color,
            'birth_year': self.birth_year,
            'planet_id': self.planet_id
        }
    

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    diameter = db.Column(db.Integer, nullable=False)
    rotation_period = db.Column(db.Integer, nullable=False)
    orbital_period = db.Column(db.Integer, nullable=False)
    climate = db.Column(db.String(250), nullable=False)
    population = db.Column(db.Integer, nullable=False)
    terrain = db.Column(db.String(250), nullable=False)
    surface_water = db.Column(db.Integer, nullable=True)
    characters = db.relationship('Character', backref='planet', lazy=True)
    favorites = db.relationship('Favorite', backref='planet', lazy=True)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'diameter': self.diameter,
            'rotation_period': self.rotation_period,
            'orbital_period': self.orbital_period,
            'climate': self.climate,
            'population': self.population,
            'terrain': self.terrain,
            'surface_water': self.surface_water
        }

class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'))
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))
    # vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'))


# class Vehicle(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(250), nullable=False)
#     model = db.Column(db.String(250), nullable=False)
#     crew = db.Column(db.Integer, nullable=False)
#     length = db.Column(db.String(250), nullable=False)
#     manufacturer = db.Column(db.String(250), nullable=False)
#     character_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=False, unique=True)
#     favourites = db.relationship('Favorite', backref='vehicle', lazy=True)

