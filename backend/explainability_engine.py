
def generate_explanations(
    nutrition,
    glucose
):

    totals = nutrition["totals"]

    explanations = []

    if totals["protein"] < 20:

        explanations.append(
            "Protein intake was slightly low."
        )

    if glucose["glycemic_load"] > 50:

        explanations.append(
            "High glycemic load detected."
        )

    if totals["fiber"] < 8:

        explanations.append(
            "Fiber intake could be improved."
        )

    if totals["calories"] > 700:

        explanations.append(
            "Calories were high for a single meal."
        )

    return explanations

