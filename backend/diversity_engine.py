
# =========================
# FILE: backend/diversity_engine.py
# =========================

def calculate_diversity_score(
    meals
):

    unique_foods = set()

    for meal in meals.values():

        items = meal.lower().split(",")

        for item in items:

            unique_foods.add(
                item.strip()
            )

    diversity = len(unique_foods)

    # =========================
    # SCORE
    # =========================

    if diversity >= 12:

        return 100

    elif diversity >= 8:

        return 85

    elif diversity >= 5:

        return 70

    else:

        return 50
