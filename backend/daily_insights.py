
# =========================
# FILE: backend/daily_insights.py
# =========================

def calculate_daily_score(
    summary,
    goal
):

    score = 50

    protein = summary.get(
        "Protein",
        0
    )

    fiber = summary.get(
        "Fiber",
        0
    )

    glucose = summary.get(
        "Average_Glucose",
        0
    )

    calories = summary.get(
        "Calories",
        0
    )

    # =========================
    # PROTEIN
    # =========================

    if protein >= 80:

        score += 20

    elif protein >= 60:

        score += 10

    # =========================
    # FIBER
    # =========================

    if fiber >= 25:

        score += 15

    elif fiber >= 15:

        score += 8

    # =========================
    # GLUCOSE
    # =========================

    if glucose < 110:

        score += 10

    elif glucose < 130:

        score += 5

    # =========================
    # CALORIES
    # =========================

    if goal == "weight_loss":

        if calories <= 1800:

            score += 10

    return min(score, 100)


# =========================
# EXPLAINABLE AI
# =========================

def explain_daily_score(
    summary
):

    explanations = []

    protein = summary.get(
        "Protein",
        0
    )

    fiber = summary.get(
        "Fiber",
        0
    )

    glucose = summary.get(
        "Average_Glucose",
        0
    )

    if protein >= 80:

        explanations.append(
            "High protein intake improved diet quality."
        )

    else:

        explanations.append(
            "Protein intake could be improved."
        )

    if fiber < 20:

        explanations.append(
            "Fiber intake was lower than recommended."
        )

    else:

        explanations.append(
            "Fiber intake supported digestion and fullness."
        )

    if glucose < 110:

        explanations.append(
            "Meals maintained stable glucose responses."
        )

    else:

        explanations.append(
            "Some meals may have caused glucose spikes."
        )

    return explanations


# =========================
# DAILY AI INSIGHT
# =========================

def generate_daily_insight(
    summary,
    goal
):

    protein = summary.get(
        "Protein",
        0
    )

    fiber = summary.get(
        "Fiber",
        0
    )

    glucose = summary.get(
        "Average_Glucose",
        0
    )

    insights = []

    if protein >= 80:

        insights.append(
            "Protein intake was strong across the day."
        )

    else:

        insights.append(
            "Protein intake could be improved for better satiety and recovery."
        )

    if fiber < 20:

        insights.append(
            "Fiber intake could be improved with vegetables, fruits, and whole grains."
        )

    if glucose < 110:

        insights.append(
            "Meals maintained relatively stable glucose responses."
        )

    else:

        insights.append(
            "Some meals may have caused higher glucose variability."
        )

    return " ".join(insights)

