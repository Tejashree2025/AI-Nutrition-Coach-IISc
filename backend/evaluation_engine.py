
# =========================
# MEAL EVALUATION ENGINE
# =========================

def evaluate_meal_quality(
    nutrition,
    glucose,
    goal
):

    totals = nutrition["totals"]

    calories = totals.get(
        "calories",
        0
    )

    protein = totals.get(
        "protein",
        0
    )

    carbs = totals.get(
        "carbs",
        0
    )

    fat = totals.get(
        "fat",
        0
    )

    fiber = totals.get(
        "fiber",
        0
    )

    glucose_peak = glucose.get(
        "predicted_peak",
        0
    )

    score = 50

    # =========================
    # PROTEIN
    # =========================

    if protein >= 25:

        score += 20

    elif protein >= 15:

        score += 15

    elif protein >= 10:

        score += 10

    # =========================
    # FIBER
    # =========================

    if fiber >= 10:

        score += 20

    elif fiber >= 5:

        score += 15

    elif fiber >= 3:

        score += 10

    # =========================
    # GLUCOSE
    # =========================

    if glucose_peak <= 110:

        score += 15

    elif glucose_peak <= 140:

        score += 8

    # =========================
    # CALORIES
    # =========================

    if goal == "weight_loss":

        if calories <= 500:

            score += 10

        elif calories <= 700:

            score += 5

    # =========================
    # FAT
    # =========================

    if fat <= 20:

        score += 5

    # =========================
    # LIMIT
    # =========================

    score = max(
        0,
        min(score, 100)
    )

    # =========================
    # LABEL
    # =========================

    if score >= 85:

        label = "✅ Excellent Meal"

    elif score >= 70:

        label = "✅ Good Meal Quality"

    elif score >= 55:

        label = "⚠ Moderate Meal Quality"

    else:

        label = "❌ Needs Improvement"

    return {

        "score": score,

        "label": label
    }

