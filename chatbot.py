
# =========================
# FILE: chatbot.py
# =========================

from langchain_community.llms import Ollama

# =========================
# LOAD MODEL
# =========================

llm = Ollama(
    model="qwen:latest"
)

# =========================
# CHATBOT
# =========================

def chat_with_bot(question):

    try:

        prompt = f"""

You are an expert Indian AI nutrition coach.

Answer the user's nutrition question naturally and practically.

STRICT RULES:
- Give DIRECT answers
- Avoid generic textbook explanations
- Avoid saying "consult a professional"
- Avoid repeating the question
- Keep answer short and useful
- Focus on Indian foods
- Suggest MEALS not recipes
- Do NOT suggest unhealthy foods
- Do NOT suggest white bread frequently
- Mention protein/calorie benefits when relevant
- Use bullet points when listing meals
- Sound like a smart modern nutrition coach

Examples:

Q: Suggest high protein Indian breakfast
A:
• Moong dal chilla with curd
• Paneer bhurji with chapati
• Greek yogurt with fruits and nuts
• Oats with milk and chia seeds
• Sprouts salad with boiled eggs

Q: Can I eat gulab jamun during weight loss?
A:
Yes, occasionally. Limit to 1 small gulab jamun once in a while and maintain overall calorie balance during the day.

Q: Suggest weight loss dinner under 400 calories
A:
• Grilled paneer with salad
• Dal soup with vegetables
• Stir-fried tofu with veggies
• Egg bhurji with sautéed vegetables
• Grilled chicken with cucumber salad

USER QUESTION:
{question}

"""

        response = llm.invoke(
            prompt
        )

        return response.strip()

    except Exception:

        return (
            "Unable to generate nutrition response right now."
        )

