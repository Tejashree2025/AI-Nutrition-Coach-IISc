
# =========================
# FILE: backend/meal_rating.py
# =========================

def get_meal_rating(score):

    if score >= 90:

        return "Excellent"

    elif score >= 75:

        return "Good"

    elif score >= 60:

        return "Average"

    else:

        return "Poor"

