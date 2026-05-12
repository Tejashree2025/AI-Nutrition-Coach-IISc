
# =========================
# FILE: backend/glucose_model.py
# =========================

def predict_glucose_response(
    nutrition,
    activity_level,
    memory
):

    if "totals" in nutrition:

        totals = nutrition["totals"]

    else:

        totals = nutrition

    carbs = totals.get("carbs", 0)

    fiber = totals.get("fiber", 0)

    protein = totals.get("protein", 0)

    fat = totals.get("fat", 0)

    calories = totals.get("calories", 0)

    # =========================
    # IMPROVED GLYCEMIC LOAD
    # =========================

    glycemic_load = max(
        carbs - (fiber * 1.5),
        0
    )

    # =========================
    # SMART BASE SPIKE
    # =========================

    spike = 85 + (
        glycemic_load * 0.9
    )

    # =========================
    # PROTEIN REDUCTION
    # =========================

    spike -= protein * 0.7

    # =========================
    # FAT REDUCTION
    # =========================

    spike -= fat * 0.3

    # =========================
    # FIBER REDUCTION
    # =========================

    spike -= fiber * 0.5

    # =========================
    # ACTIVITY EFFECT
    # =========================

    if activity_level == "high":

        spike -= 18

    elif activity_level == "moderate":

        spike -= 10

    # =========================
    # MEMORY PERSONALIZATION
    # =========================

    if memory:

        history = memory.get(
            "history",
            []
        )

        previous_peaks = []

        for item in history:

            glucose = item.get(
                "glucose",
                {}
            )

            peak = glucose.get(
                "predicted_peak"
            )

            if peak:

                previous_peaks.append(
                    peak
                )

        if previous_peaks:

            avg_peak = sum(
                previous_peaks
            ) / len(previous_peaks)

            spike = (
                spike * 0.7
            ) + (
                avg_peak * 0.3
            )

    # =========================
    # LIMITS
    # =========================

    spike = max(
        80,
        min(spike, 220)
    )

    # =========================
    # RISK LEVEL
    # =========================

    risk = "Low"

    caution = ""

    if spike >= 180:

        risk = "High"

        caution = (
            "⚠ High glucose spike predicted."
        )

    elif spike >= 140:

        risk = "Moderate"

        caution = (
            "⚠ Moderate glucose spike predicted."
        )

    return {

        "predicted_peak": round(
            spike,
            2
        ),

        "glycemic_load": round(
            glycemic_load,
            2
        ),

        "risk_level": risk,

        "caution": caution
    }

