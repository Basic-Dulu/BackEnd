from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models import Product, Ingredient, SkinTestResult, SkinProblem

recommendation_bp = Blueprint("recommendation", __name__)


@recommendation_bp.route("/recommendation", methods=["POST"])
def api_recommendation():
    data = request.get_json()
    input_skin_result_id = data.get("skin_test_result_id")
    input_skin_problem_id = data.get("skin_problem_id")

    if not input_skin_result_id or not input_skin_problem_id:
        return (
            jsonify({"error": "skin_test_result_id and skin_problem_id are required"}),
            400,
        )

    # Constants
    bobot = {"jenis_kulit": 0.4, "masalah_kulit": 0.6}

    # Get input points
    skin_result = SkinTestResult.query.get(input_skin_result_id)
    skin_problem = SkinProblem.query.get(input_skin_problem_id)

    if not skin_result or not skin_problem:
        return jsonify({"error": "Invalid skin_test_result_id or skin_problem_id"}), 404

    input_r1 = skin_result.saw_point
    input_r2 = skin_problem.saw_point

    # Filter relevant products
    products = (
        db.session.query(Product)
        .join(Ingredient, Product.ingredient_id == Ingredient.id)
        .join(SkinTestResult, Ingredient.skin_test_result_id == SkinTestResult.id)
        .join(SkinProblem, Product.skin_problem_id == SkinProblem.id)
        .filter(Ingredient.skin_test_result_id == input_skin_result_id)
        .filter(Product.skin_problem_id == input_skin_problem_id)
        .all()
    )

    if not products:
        # Try looser filter: match either
        products = (
            db.session.query(Product)
            .join(Ingredient, Product.ingredient_id == Ingredient.id)
            .join(SkinTestResult, Ingredient.skin_test_result_id == SkinTestResult.id)
            .join(SkinProblem, Product.skin_problem_id == SkinProblem.id)
            .filter(
                (Ingredient.skin_test_result_id == input_skin_result_id)
                | (Product.skin_problem_id == input_skin_problem_id)
            )
            .all()
        )

    if not products:
        return jsonify([])

    # Scoring
    product_scores = []
    for product in products:
        st_result = product.ingredient.skin_test_result
        s_problem = product.skin_problem

        if not st_result or not s_problem:
            continue

        r1 = st_result.saw_point
        r2 = s_problem.saw_point

        product_scores.append({"product": product, "r1": r1, "r2": r2})

    if not product_scores:
        return jsonify([])

    max_r1 = max(p["r1"] for p in product_scores)
    max_r2 = max(p["r2"] for p in product_scores)

    results = []
    for p in product_scores:
        nr1 = p["r1"] / max_r1 if max_r1 else 0
        nr2 = p["r2"] / max_r2 if max_r2 else 0

        cocok_jenis = 1 if p["r1"] == input_r1 else 0
        cocok_masalah = 1 if p["r2"] == input_r2 else 0
        bonus = 0.2 * (cocok_jenis + cocok_masalah)

        skor = bobot["jenis_kulit"] * nr1 + bobot["masalah_kulit"] * nr2 + bonus

        results.append({**p["product"].to_dict(), "skor": round(skor, 4)})

    sorted_results = sorted(results, key=lambda x: x["skor"], reverse=True)
    return jsonify(sorted_results)
