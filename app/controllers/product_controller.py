from flask import Blueprint, jsonify
from app.models.product import Product
from collections import OrderedDict

product_bp = Blueprint("product", __name__, url_prefix="/products")


@product_bp.route("/", methods=["GET"])
def get_products():
    products = Product.query.order_by(Product.id.asc()).all()
    product_list = [product.to_dict() for product in products]

    return jsonify(
        {
            "success": True,
            "message": "Products fetched successfully",
            "data": product_list,
        }
    )


@product_bp.route("/<int:product_id>", methods=["GET"])
def get_product_by_id(product_id):
    product = Product.query.get(product_id)

    if not product:
        return jsonify({"success": False, "message": "Product not found"}), 404

    return jsonify(
        {
            "success": True,
            "message": "Product fetched successfully",
            "data": product.to_dict(),
        }
    )


@product_bp.route("/by-type-detail/<int:product_type_detail_id>", methods=["GET"])
def get_product_by_product_type_detail_id(product_type_detail_id):
    product = Product.query.filter_by(
        product_type_detail_id=product_type_detail_id
    ).first()

    if not product:
        return jsonify({"success": False, "message": "Product not found"}), 404

    return jsonify(
        {
            "success": True,
            "message": "Product fetched successfully",
            "data": product.to_dict(),
        }
    )
