def build_nutrition_prompt(
    nutrition,
    glucose,
    goal,
    meal_text,
    rag_context,
    health_conditions
):

    prompt = f"""
You are an advanced Indian AI nutritionist.

Analyze the following meal scientifically.

Meal:
{meal_text}

Nutrition:
{nutrition}

Glucose:
{glucose}

Goal:
{goal}

Health Conditions:
{health_conditions}

Retrieved Context:
{rag_context}

Provide:
1. Nutrition quality
2. Satiety analysis
3. Glucose reasoning
4. Weight management advice
5. Improvement suggestions

Keep answer concise but realistic.
"""

    return prompt