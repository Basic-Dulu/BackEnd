from app.extensions import db


class Brand(db.Model):
    __tablename__ = "brands"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    # products = db.relationship("Product", backref="brand", cascade="all, delete-orphan")
