
# =========================
# FILE: backend/adaptive_engine.py
# =========================

def analyze_user_patterns(history):

    insights = []

    if len(history) == 0:

        return {

            "low_protein_days": 0,

            "high_glucose_days": 0,

            "low_fiber_days": 0,

            "insights": []
        }

    low_protein_days = 0
    high_glucose_days = 0
    low_fiber_days = 0

    for item in history:

        nutrition = item.get(
            "nutrition",
            {}
        )

        glucose = item.get(
            "glucose",
            {}
        )

        totals = nutrition.get(
            "totals",
            {}
        )

        protein = totals.get(
            "protein",
            0
        )

        fiber = totals.get(
            "fiber",
            0
        )

        peak = glucose.get(
            "predicted_peak",
            0
        )

        if protein < 20:

            low_protein_days += 1

        if fiber < 15:

            low_fiber_days += 1

        if peak > 130:

            high_glucose_days += 1

    # =========================
    # AI STYLE INSIGHTS
    # =========================

    if low_protein_days >= 3:

        insights.append(
            "Protein intake has been consistently low recently."
        )

    if low_fiber_days >= 3:

        insights.append(
            "Fiber intake has been low across recent meals."
        )

    if high_glucose_days >= 3:

        insights.append(
            "Recent meals showed repeated glucose spikes."
        )

    return {

        "low_protein_days": low_protein_days,

        "low_fiber_days": low_fiber_days,

        "high_glucose_days": high_glucose_days,

        "insights": insights
    }

