
def analyze_weekly_trends(
    history
):

    calories = []
    protein = []
    glucose = []

    for item in history:

        nutrition = item.get(
            "nutrition",
            {}
        )

        totals = nutrition.get(
            "totals",
            {}
        )

        calories.append(
            totals.get("calories", 0)
        )

        protein.append(
            totals.get("protein", 0)
        )

        glucose_data = item.get(
            "glucose",
            {}
        )

        glucose.append(
            glucose_data.get(
                "predicted_peak",
                0
            )
        )

    return {

        "avg_calories":
        round(sum(calories)/max(len(calories),1),2),

        "avg_protein":
        round(sum(protein)/max(len(protein),1),2),

        "avg_glucose":
        round(sum(glucose)/max(len(glucose),1),2)
    }
