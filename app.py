"""Flask app for Cupcakes"""
from flask import Flask, redirect, request, render_template, jsonify
from models import db, connect_db, Cupcake
from keys import secret_key

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = secret_key

connect_db(app)
db.create_all()

@app.route('/')
def render_homepage():
    """Renders the template for the main homepage"""
    return render_template('home.html')

@app.route('/api/cupcakes')
def get_all_cupcakes():
    """Get data for all cupcakes in database"""

    cupcakes = Cupcake.query.all()
    serialized = [c.serialize() for c in cupcakes]

    return (jsonify(cupcakes=serialized), 200)

@app.route('/api/cupcakes/<int:cupcake_id>')
def get_cupcake(cupcake_id):
    """Get data for specifie cupcake or return 404 if not found"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    return (jsonify(cupcake=cupcake.serialize()), 200)

@app.route('/api/cupcakes', methods=['POST'])
def add_cupcake():
    """Adds cupcake to database using json given"""

    flavor = request.json['flavor']
    size = request.json['size']
    rating = request.json['rating']
    image = request.json.get('image', None)

    if image:
        new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)
    else:
        new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating)
    
    db.session.add(new_cupcake)
    db.session.commit()

    return (jsonify(cupcake=new_cupcake.serialize()), 201)

@app.route('/api/cupcakes/<int:cupcake_id>', methods=['PATCH'])
def update_cupcake(cupcake_id):
    """Updates chosen cupcake using given JSON parameters if cupcake is found"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.image = request.json.get('image', cupcake.image)
    db.session.commit()
    
    return (jsonify(cupcake=cupcake.serialize()), 200)

@app.route('/api/cupcakes/<int:cupcake_id>', methods=['DELETE'])
def delete_cupcake(cupcake_id):
    """Deletes a chosen cupcake if it is found"""
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    db.session.delete(cupcake)
    db.session.commit()

    return (jsonify(deleted=cupcake_id), 200)