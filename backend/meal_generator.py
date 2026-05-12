
# =========================
# FILE: backend/meal_generator.py
# =========================

import random

# =========================
# VEG HIGH PROTEIN OPTIONS
# =========================

VEG_PROTEIN_MEALS = [

    "Add paneer tikka",

    "Add Greek yogurt bowl",

    "Add sprouts salad",

    "Add roasted chana",

    "Add moong dal chilla",

    "Add mixed lentil soup",

    "Add curd with chia seeds",

    "Add quinoa salad",

    "Add cottage cheese sandwich",

    "Add peanut chaat"
]

# =========================
# NON VEG OPTIONS
# =========================

NONVEG_PROTEIN_MEALS = [

    "Add boiled eggs",

    "Add grilled chicken",

    "Add fish curry",

    "Add chicken salad",

    "Add egg bhurji",

    "Add tuna sandwich"
]

# =========================
# FIBER OPTIONS
# =========================

VEG_FIBER_MEALS = [

    "Add fruit bowl",

    "Add vegetable salad",

    "Add oats smoothie",

    "Add cucumber salad",

    "Add sautéed vegetables",

    "Add chia seed yogurt",

    "Add apple with nuts"
]

# =========================
# LOW CARB OPTIONS
# =========================

LOW_CARB_SWAPS = [

    "Reduce refined carbs slightly",

    "Replace rice with millet",

    "Use whole wheat chapati",

    "Reduce sugary beverages",

    "Use smaller rice portions"
]

# =========================
# MAIN GENERATOR
# =========================

def generate_next_meal(

    nutrition,
    goal,
    diet_type,
    glucose
):

    # =========================
    # HANDLE TOTALS
    # =========================

    if "totals" in nutrition:

        totals = nutrition["totals"]

    else:

        totals = nutrition

    # =========================
    # VALUES
    # =========================

    protein = totals.get(
        "protein",
        0
    )

    carbs = totals.get(
        "carbs",
        0
    )

    calories = totals.get(
        "calories",
        0
    )

    fiber = totals.get(
        "fiber",
        0
    )

    # =========================
    # SWAPS
    # =========================

    recommendations = []

    reasoning = []

    # =========================
    # PROTEIN
    # =========================

    if protein < 20:

        if diet_type == "veg":

            recommendations.append(

                random.choice(
                    VEG_PROTEIN_MEALS
                )
            )

        elif diet_type == "non_veg":

            recommendations.append(

                random.choice(
                    NONVEG_PROTEIN_MEALS
                )
            )

        else:

            mixed = (
                VEG_PROTEIN_MEALS +
                NONVEG_PROTEIN_MEALS
            )

            recommendations.append(
                random.choice(mixed)
            )

        reasoning.append(
            "Protein intake was slightly low."
        )

    # =========================
    # FIBER
    # =========================

    if fiber < 6:

        recommendations.append(

            random.choice(
                VEG_FIBER_MEALS
            )
        )

        reasoning.append(
            "Fiber intake can be improved."
        )

    # =========================
    # CARBS
    # =========================

    if carbs > 60:

        recommendations.append(

            random.choice(
                LOW_CARB_SWAPS
            )
        )

        reasoning.append(
            "Meal carbohydrate load was high."
        )

    # =========================
    # CALORIES
    # =========================

    if goal == "weight_loss":

        if calories > 600:

            recommendations.append(
                "Reduce portion size slightly"
            )

            reasoning.append(
                "Meal calories were high for your goal."
            )

    # =========================
    # DEFAULT
    # =========================

    if len(recommendations) == 0:

        if diet_type == "veg":

            recommendations.append(
                "Maintain balanced veg protein intake"
            )

        elif diet_type == "non_veg":

            recommendations.append(
                "Maintain balanced lean protein intake"
            )

        else:

            recommendations.append(
                "Maintain balanced meal portions"
            )

        reasoning.append(
            "Meal looked balanced overall."
        )

    # =========================
    # REMOVE DUPLICATES
    # =========================

    recommendations = list(
        dict.fromkeys(
            recommendations
        )
    )

    # =========================
    # RETURN
    # =========================

    return {

        "recommended_meal": " | ".join(
            recommendations[:3]
        ),

        "reason": " ".join(
            reasoning[:3]
        )
    }

