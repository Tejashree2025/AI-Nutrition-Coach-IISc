
# =========================
# FILE: backend/recommendation_engine.py
# =========================

# =========================
# VEG PROTEIN OPTIONS
# =========================

VEG_PROTEINS = (

    "paneer, Greek yogurt, sprouts, tofu, "
    "lentils, chickpeas, quinoa, nuts, seeds"
)

# =========================
# NON VEG PROTEIN OPTIONS
# =========================

NON_VEG_PROTEINS = (

    "paneer, Greek yogurt, sprouts, tofu, "
    "eggs, fish, chicken"
)

# =========================
# RECOMMENDATIONS
# =========================

def generate_recommendations(

    nutrition,

    glucose,

    goal,

    diet_type="mixed"
):

    recommendations = []

    # =========================
    # TOTALS
    # =========================

    totals = nutrition["totals"]

    calories = totals["calories"]

    protein = totals["protein"]

    carbs = totals["carbs"]

    fat = totals["fat"]

    fiber = totals["fiber"]

    # =========================
    # PROTEIN SOURCE
    # =========================

    if diet_type == "veg":

        protein_sources = VEG_PROTEINS

    else:

        protein_sources = NON_VEG_PROTEINS

    # =========================
    # LOW PROTEIN
    # =========================

    if protein < 20:

        recommendations.append(

            f"Increase protein using {protein_sources}."
        )

    # =========================
    # LOW FIBER
    # =========================

    if fiber < 8:

        recommendations.append(

            "Add vegetables, salads, fruits, oats, chia seeds, or flaxseeds for better fiber intake."
        )

    # =========================
    # HIGH CALORIES
    # =========================

    if goal == "weight_loss":

        if calories > 600:

            recommendations.append(

                "Reduce portion sizes slightly and avoid oily or fried foods."
            )

    # =========================
    # HIGH FAT
    # =========================

    if fat > 25:

        recommendations.append(

            "Use lighter cooking methods and reduce excess oils or butter."
        )

    # =========================
    # HIGH CARBS
    # =========================

    if carbs > 70:

        recommendations.append(

            "Reduce refined carbs slightly and balance meals with more protein and fiber."
        )

    # =========================
    # GLUCOSE
    # =========================

    if glucose["predicted_peak"] > 140:

        recommendations.append(

            "Prefer low glycemic foods and avoid sugary beverages or sweets."
        )

    # =========================
    # FALLBACK
    # =========================

    if len(recommendations) == 0:

        recommendations.append(

            "Your meal looks balanced overall with decent nutrition distribution."
        )

    return recommendations

