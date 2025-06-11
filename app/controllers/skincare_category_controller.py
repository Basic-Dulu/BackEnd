from flask import Blueprint, request, jsonify, current_app
from app.models.skincare_category import SkinCareCategory, db
from collections import OrderedDict

import jwt
import datetime
import os

skincare_category_bp = Blueprint(
    "skincare_category", __name__, url_prefix="/skincare-categories"
)


@skincare_category_bp.route("/", methods=["GET"])
def get_skin_categories():
    skin_categories = [
        skin_category.to_dict()
        for skin_category in SkinCareCategory.query.order_by(
            SkinCareCategory.id.asc()
        ).all()
    ]

    response = OrderedDict(
        [
            ("success", True),
            ("message", "Data fetched successfully"),
            ("data", skin_categories),
        ]
    )

    return jsonify(response)


@skincare_category_bp.route("/<int:id>", methods=["GET"])
def get_skin_category_by_id(id):
    base_url = request.host_url.rstrip("/")

    skin_category = SkinCareCategory.query.get(id)

    if not skin_category:
        response = OrderedDict(
            [
                ("success", False),
                ("message", f"Skincare category with ID {id} not found"),
                ("data", None),
            ]
        )
        return jsonify(response), 404

    # Prepare related product type details with their product types
    product_type_details_data = []
    for detail in skin_category.product_type_details:
        product_type_details_data.append(
            {
                "id": detail.id,
                "description": detail.description,
                "product_type": {
                    "id": detail.product_type.id,
                    "name": detail.product_type.name,
                },
            }
        )

    skin_category_data = {
        "id": skin_category.id,
        "name": skin_category.name,
        "slogan": skin_category.slogan,
        "description": skin_category.description,
        "image": (
            f"{base_url}/static/uploads/{skin_category.image}"
            if skin_category.image
            else None
        ),
        "benefit": skin_category.benefit,
        "how_to_use": skin_category.how_to_use,
        "product_type_details": product_type_details_data,
    }

    response = OrderedDict(
        [
            ("success", True),
            ("message", "Data fetched successfully"),
            ("data", skin_category_data),
        ]
    )

    return jsonify(response), 200


@skincare_category_bp.route("/", methods=["GET"])
def get_users():
    skincare_categories = [
        skincare_category.to_dict()
        for skincare_category in SkinCareCategory.query.order_by(
            SkinCareCategory.id.asc()
        ).all()
    ]

    response = OrderedDict(
        [
            ("success", True),
            ("message", "Data fetched successfully"),
            ("data", skincare_categories),
        ]
    )

    return jsonify(response)
