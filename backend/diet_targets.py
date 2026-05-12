
# =========================
# FILE: backend/diet_targets.py
# =========================

# =========================
# DAILY TARGETS
# =========================

def get_daily_targets(
    goal,
    weight
):

    # =========================
    # WEIGHT LOSS
    # =========================

    if goal == "weight_loss":

        calories = weight * 25

        protein = weight * 1.8

        carbs = weight * 2.5

        fat = weight * 0.8

        fiber = 25

    # =========================
    # MUSCLE GAIN
    # =========================

    elif goal == "muscle_gain":

        calories = weight * 35

        protein = weight * 2.0

        carbs = weight * 4.0

        fat = weight * 1.0

        fiber = 30

    # =========================
    # MAINTENANCE
    # =========================

    else:

        calories = weight * 30

        protein = weight * 1.6

        carbs = weight * 3.0

        fat = weight * 0.9

        fiber = 28

    # =========================
    # RETURN TARGETS
    # =========================

    return {

        "Calories": round(calories),

        "Protein": round(protein),

        "Carbs": round(carbs),

        "Fat": round(fat),

        "Fiber": round(fiber)
    }

# =========================
# COMPARE WITH TARGETS
# =========================

def compare_with_targets(
    summary,
    targets
):

    comparison = {}

    # =========================
    # CALORIES
    # =========================

    comparison["Calories"] = {

        "consumed": round(
            summary.get("Calories", 0),
            2
        ),

        "target": targets["Calories"],

        "remaining": round(
            targets["Calories"]
            - summary.get("Calories", 0),
            2
        )
    }

    # =========================
    # PROTEIN
    # =========================

    comparison["Protein"] = {

        "consumed": round(
            summary.get("Protein", 0),
            2
        ),

        "target": targets["Protein"],

        "remaining": round(
            targets["Protein"]
            - summary.get("Protein", 0),
            2
        )
    }

    # =========================
    # CARBS
    # =========================

    comparison["Carbs"] = {

        "consumed": round(
            summary.get("Carbs", 0),
            2
        ),

        "target": targets["Carbs"],

        "remaining": round(
            targets["Carbs"]
            - summary.get("Carbs", 0),
            2
        )
    }

    # =========================
    # FAT
    # =========================

    comparison["Fat"] = {

        "consumed": round(
            summary.get("Fat", 0),
            2
        ),

        "target": targets["Fat"],

        "remaining": round(
            targets["Fat"]
            - summary.get("Fat", 0),
            2
        )
    }

    # =========================
    # FIBER
    # =========================

    comparison["Fiber"] = {

        "consumed": round(
            summary.get("Fiber", 0),
            2
        ),

        "target": targets["Fiber"],

        "remaining": round(
            targets["Fiber"]
            - summary.get("Fiber", 0),
            2
        )
    }

    return comparison

