"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    "Initiates the connection to the database"
    db.app = app
    db.init_app(app)

class Cupcake(db.Model):
    """Basic data structure for all cupcakes"""

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    flavor = db.Column(db.String, nullable=False)

    size = db.Column(db.String, nullable=False)

    rating = db.Column(db.Float, nullable=False)

    image = db.Column(db.String, nullable=False, default="https://tinyurl.com/demo-cupcake")

    def serialize(self):
        """Returns serialized version of self"""

        return {'id': self.id, 'flavor': self.flavor, 'size': self.size, 'rating': self.rating, 'image': self.image}