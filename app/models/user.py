from app import db
from collections import OrderedDict

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    # converting the model to JSON format friendly
    def to_dict(self):
        return OrderedDict([
        ("id", self.id),
        ("username", self.username),
        ("email", self.email)
    ])