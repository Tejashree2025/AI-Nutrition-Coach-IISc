
# =========================
# FILE: backend/llm_reasoning.py
# =========================

from langchain_community.llms import Ollama

# =========================
# LOAD MODEL
# =========================

llm = Ollama(
    model="qwen:latest"
)

# =========================
# SINGLE MEAL AI INSIGHT
# =========================

def generate_ai_insight(
    nutrition,
    glucose,
    goal,
    meal_text
):

    try:

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

        risk = glucose.get(
            "risk_level",
            "Low"
        )

        # =========================
        # SMART PROMPT
        # =========================

        prompt = f"""

You are an elite Indian nutrition coach.

Analyze this Indian meal intelligently.

Meal:
{meal_text}

Nutrition:
Calories: {calories}
Protein: {protein}
Carbs: {carbs}
Fat: {fat}
Fiber: {fiber}

Predicted Glucose Peak:
{glucose_peak}

Risk Level:
{risk}

Goal:
{goal}

Rules:
- Keep answer short
- Maximum 2 sentences
- Sound natural and human
- Avoid robotic wording
- Mention positives first
- Give practical advice
- Mention Indian foods naturally
- NEVER recommend non-veg foods if meal looks vegetarian
- Avoid repeating all nutrition numbers
- Avoid generic advice

Good examples:
"Your meal has good fiber balance from dal and salad, which may help control hunger. Adding paneer, curd, sprouts, or extra dal can improve protein for better satiety during weight loss."

"Balanced carbohydrates and fiber help keep this meal relatively glucose friendly. Slightly increasing protein using paneer or Greek yogurt may improve fullness and muscle recovery."

"""

        response = llm.invoke(
            prompt
        )

        return response.strip()

    except Exception:

        # =========================
        # FALLBACK LOGIC
        # =========================

        insights = []

        # =========================
        # POSITIVE FIRST
        # =========================

        if fiber >= 8:

            insights.append(
                "Your meal has good fiber balance which may support digestion and appetite control."
            )

        elif calories <= 500:

            insights.append(
                "This meal fits reasonably well within a weight loss calorie range."
            )

        # =========================
        # PROTEIN
        # =========================

        if protein < 20:

            if "chicken" in meal_text.lower() or "egg" in meal_text.lower():

                insights.append(
                    "Adding slightly more protein may improve fullness and muscle recovery."
                )

            else:

                insights.append(
                    "Adding paneer, curd, sprouts, lentils, or Greek yogurt can improve protein quality."
                )

        # =========================
        # CARB LOAD
        # =========================

        if carbs > 70:

            insights.append(
                "The carbohydrate load is slightly high, so balancing with more protein may improve glucose stability."
            )

        # =========================
        # GLUCOSE
        # =========================

        if glucose_peak > 130:

            insights.append(
                "This meal may create a moderate glucose spike, so portion control and slower eating may help."
            )

        # =========================
        # FINAL
        # =========================

        if len(insights) == 0:

            return (
                "This meal looks reasonably balanced with decent nutrition distribution and glucose control."
            )

        return " ".join(
            insights[:2]
        )

# =========================
# DAILY AI INSIGHT
# =========================

def generate_daily_insight(
    summary,
    goal
):

    calories = summary["Calories"]

    protein = summary["Protein"]

    carbs = summary["Carbs"]

    fat = summary["Fat"]

    fiber = summary["Fiber"]

    insights = []

    # =========================
    # POSITIVE START
    # =========================

    if fiber >= 25:

        insights.append(
            "Your overall fiber intake looked good today, which may support digestion and appetite control."
        )

    # =========================
    # PROTEIN
    # =========================

    if protein < 70:

        insights.append(
            "Protein intake was slightly low today, so adding paneer, curd, sprouts, dal, or Greek yogurt may improve satiety and recovery."
        )

    # =========================
    # CALORIES
    # =========================

    if calories > 1700 and goal == "weight_loss":

        insights.append(
            "Calories were slightly higher than your target, so lighter dinners and smaller portions may help weight loss consistency."
        )

    # =========================
    # CARBS
    # =========================

    if carbs > 220:

        insights.append(
            "Carbohydrate intake was relatively high today, so balancing meals with more protein may improve glucose stability."
        )

    # =========================
    # FAT
    # =========================

    if fat > 70:

        insights.append(
            "Fat intake was on the higher side today, so reducing fried foods and excess oils may help calorie balance."
        )

    # =========================
    # DEFAULT
    # =========================

    if len(insights) == 0:

        insights.append(
            "Your meals looked balanced overall with decent calorie control and nutrition distribution."
        )

    return " ".join(
        insights[:2]
    )

