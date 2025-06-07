from app.extensions import db


class IngredientType(db.Model):
    __tablename__ = "ingredient_types"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
