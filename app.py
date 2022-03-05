"""Flask app for Cupcakes"""
from flask import Flask, request, jsonify, render_template, flash, session
from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['SECRET_KEY'] = 'key'

connect_db(app)

@app.route("/")
def home():
    cups = Cupcake.query.all()
    return render_template('index.html', cups = cups)

@app.route("/api/cupcakes")
def list_cupcakes():
    """all cupcakes using json"""

    cupcakes = [cup.serialize() for cup in Cupcake.query.all()]
    return jsonify(cupcakes = cupcakes)

@app.route("/api/cupcakes/<int:cup_id>")
def single_cupcake(cup_id):
    """showing particular cupcake"""

    cupcake = Cupcake.query.get_or_404(cup_id)
    return jsonify(cupcake = cupcake.serialize())

@app.route("/api/cupcakes", methods = ['POST'])
def create_cupcake():
    """add a cupcake"""
    new_cupcake = Cupcake(flavor = request.json["flavor"],
                          size = request.json["size"],
                          rating = request.json["rating"],
                          image = request.json["image"])
    db.session.add(new_cupcake)
    db.session.commit()
    response_json = jsonify(cupcake = new_cupcake.serialize())
    return(response_json, 201)

@app.route("/api/cupcakes/<int:cup_id>", methods = ["PATCH"])
def edit_cupcake(cup_id):
   """edit a cupcake"""
   cupcake = Cupcake.query.get_or_404(cup_id)
   cupcake.flavor = request.json.get('flavor', cupcake.flavor)
   cupcake.size = request.json.get('size', cupcake.size)
   cupcake.rating = request.json.get('rating', cupcake.rating)
   cupcake.image = request.json.get('image', cupcake.image)
   db.session.commit()
   return jsonify(cupcake = cupcake.serialize())

@app.route('/api/cupcakes/<int:id>', methods=["DELETE"])
def delete_todo(id):
    """Deletes a particular Cupcake"""
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="deleted")