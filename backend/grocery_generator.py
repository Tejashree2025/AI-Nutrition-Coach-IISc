
def generate_grocery_list(
    meals
):

    groceries = []

    for meal in meals:

        lower = meal.lower()

        if "paneer" in lower:
            groceries.append("Paneer")

        if "oats" in lower:
            groceries.append("Oats")

        if "sprouts" in lower:
            groceries.append("Sprouts")

        if "milk" in lower:
            groceries.append("Milk")

        if "vegetable" in lower:
            groceries.append("Mixed vegetables")

        if "egg" in lower:
            groceries.append("Eggs")

    groceries = list(
        set(groceries)
    )

    return groceries

