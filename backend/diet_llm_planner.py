
# =========================
# FILE: backend/diet_llm_planner.py
# FINAL SUBMISSION VERSION
# =========================

from langchain_community.llms import Ollama

# =========================
# LOAD MODEL
# =========================

llm = Ollama(
    model="qwen:latest"
)

# =========================
# GENERATE DIET PLAN
# =========================

def generate_diet_plan(
    profile,
    targets
):

    # =========================
    # SAFE PROFILE VALUES
    # =========================

    goal = profile.get(
        "goal",
        "weight_loss"
    )

    diet_type = profile.get(
        "diet_type",
        "veg"
    ).lower()

    activity = profile.get(
        "activity",
        "moderate"
    )

    allergies = profile.get(
        "allergies",
        ""
    )

    dislikes = profile.get(
        "dislikes",
        ""
    )

    meals_per_day = profile.get(
        "meals_per_day",
        3
    )

    water = profile.get(
        "water_intake",
        "3 Liters"
    )

    plan_type = profile.get(
        "plan_type",
        "balanced"
    )

    calories = targets.get(
        "Calories",
        1800
    )

    protein = targets.get(
        "Protein",
        80
    )

    # =========================
    # AI PROMPT
    # =========================

    prompt = f"""

You are an Indian nutrition coach.

Generate a SIMPLE Indian meal plan.

IMPORTANT RULES:

- ONLY provide MEALS
- DO NOT provide recipes
- DO NOT explain ingredients
- DO NOT describe cooking methods
- DO NOT use fancy foods
- DO NOT use western dishes
- DO NOT use restaurant foods
- DO NOT use long paragraphs
- Keep meals realistic and homemade
- Keep meals short and simple

Goal:
{goal}

Diet Type:
{diet_type}

Activity:
{activity}

Calories:
{calories}

Protein:
{protein}g

Avoid Foods:
{allergies}
{dislikes}

Meals Per Day:
{meals_per_day}

If diet_type is veg:
ONLY provide vegetarian meals.

STRICTLY NEVER INCLUDE:
chicken
fish
egg
meat
seafood
mutton
non veg

If diet_type is mixed:
You may include eggs, chicken, fish.

GOOD EXAMPLES:
4 eggs, milk, banana
2 chapati, dal, salad
rice, chicken curry, curd
fish curry, chapati
paneer curry, rice
idli, sambar
dosa, chutney
roasted peanuts
protein shake
upma
poha
rajma rice
chana curry

BAD EXAMPLES:
grilled salmon with roasted asparagus
vegetable stir fry with snow peas
scrambled eggs with herbs
naan
pizza
burger
pasta

FORMAT STRICTLY:

Breakfast:
Option 1:
Option 2:

Lunch:
Option 1:
Option 2:

Snack:
Option 1:
Option 2:

Dinner:
Option 1:
Option 2:

ONLY meal names.
NO markdown.
NO bullet points.
NO explanations.

"""

    # =========================
    # GENERATE RESPONSE
    # =========================

    try:

        response = llm.invoke(
            prompt
        )

        response = response.strip()

        # =========================
        # VEG SAFETY FILTER
        # =========================

        if diet_type == "veg":

            banned_words = [

                "chicken",
                "fish",
                "egg",
                "meat",
                "mutton",
                "seafood"
            ]

            lower_response = response.lower()

            for word in banned_words:

                if word in lower_response:

                    raise Exception(
                        "Non veg meal detected"
                    )

        return response

    # =========================
    # FALLBACK RESPONSE
    # =========================

    except Exception:

        if diet_type == "veg":

            return """

Breakfast:
Option 1: Idli, sambar
Option 2: Oats upma, curd

Lunch:
Option 1: 2 chapati, dal, salad
Option 2: Rajma rice, curd

Snack:
Option 1: Roasted chana
Option 2: Sprouts salad

Dinner:
Option 1: Paneer curry, chapati
Option 2: Vegetable khichdi, curd

"""

        else:

            return """

Breakfast:
Option 1: 4 eggs, milk, banana
Option 2: Oats, peanut butter, milk

Lunch:
Option 1: Rice, chicken curry, curd
Option 2: 2 chapati, egg curry

Snack:
Option 1: Protein shake, peanuts
Option 2: Roasted chana, banana

Dinner:
Option 1: Fish curry, chapati
Option 2: Chicken curry, rice

"""

