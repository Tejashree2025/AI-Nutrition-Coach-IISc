
# FILE: pages/6_AI_Chatbot.py

import streamlit as st
import requests

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="AI Nutrition Chatbot",
    layout="centered"
)

# =========================
# TITLE
# =========================

st.title(
    "🤖 AI Nutrition Chatbot"
)

st.caption(
    "Ask nutrition, weight loss, muscle gain, diabetes, Indian food, or healthy eating questions."
)

st.markdown("---")

# =========================
# INPUT
# =========================

question = st.text_area(

    "Ask Nutrition Question",

    placeholder=(
        "Example: Best Indian snacks for diabetes control"
    ),

    height=120
)

# =========================
# ASK BUTTON
# =========================

if st.button(
    "💬 Ask AI Nutrition Coach"
):

    if question.strip() == "":

        st.warning(
            "Please enter a nutrition question."
        )

    else:

        with st.spinner(
            "Thinking like a nutrition coach..."
        ):

            # =========================
            # STRONG PROMPT
            # =========================

            prompt = f"""
You are an expert AI nutrition coach and Indian dietitian.

Answer nutrition questions naturally like a real nutrition expert.

STRICT RULES:
- Maximum 3 short sentences
- Give DIRECT practical answers
- Include REAL food examples
- Indian foods allowed
- Never give vague answers
- Never completely ban foods
- Encourage moderation and balance
- Sound modern, supportive, and realistic
- Avoid robotic wording
- Avoid textbook explanations

IMPORTANT:
If user asks:
- snacks -> suggest actual snacks
- meals -> suggest actual meals
- desserts -> explain moderation
- diabetes -> suggest low GI foods
- weight loss -> mention portion control
- protein -> suggest high protein foods

GOOD RESPONSE EXAMPLES:

Question:
Best Indian snacks for diabetes control

Answer:
Roasted chana, sprouts chaat, boiled eggs, peanuts, Greek yogurt, vegetable sandwich on brown bread, and roasted makhana are better Indian snack options for diabetes control. Pairing snacks with protein and fiber helps maintain steadier glucose levels.

Question:
Can I eat gulab jamun during weight loss?

Answer:
Yes, you can occasionally enjoy 1 small gulab jamun during weight loss if portions are controlled and overall calorie balance across the day is maintained. Pairing sweets with protein or eating them after meals may help reduce glucose spikes.

Question:
Suggest high protein Indian breakfast

Answer:
Paneer sandwich, egg bhurji with millet toast, oats smoothie with peanut butter, moong chilla, Greek yogurt bowls, and idli with sambar are good high-protein Indian breakfast options.

User Question:
{question}

Answer:
"""

            # =========================
            # API CALL
            # =========================

            try:

                response = requests.post(

                    "http://localhost:11434/api/generate",

                    json={
                        "model": "qwen:latest",
                        "prompt": prompt,
                        "stream": False
                    },

                    timeout=120
                )

                result = response.json()

                # =========================
                # SAFE RESPONSE HANDLING
                # =========================

                if "response" in result:

                    answer = result[
                        "response"
                    ].strip()

                elif "error" in result:

                    answer = (
                        f"⚠ Ollama Error: {result['error']}"
                    )

                else:

                    answer = (
                        "⚠ AI response unavailable right now."
                    )

                # =========================
                # CLEAN LONG RESPONSES
                # =========================

                sentences = answer.split(".")

                if len(sentences) > 3:

                    answer = ".".join(
                        sentences[:3]
                    ) + "."

                # =========================
                # DISPLAY ANSWER
                # =========================

                st.success(answer)

            # =========================
            # ERROR
            # =========================

            except Exception as e:

                st.error(
                    f"Error: {e}"
                )

# =========================
# EXAMPLES
# =========================

st.markdown("---")

st.subheader(
    "💡 Example Questions"
)

examples = [

    "Can I eat 2 gulab jamun during weight loss?",

    "Best Indian snacks for diabetes control",

    "Suggest high protein Indian breakfast",

    "Can I eat pizza during fat loss?",

    "Suggest dinner under 400 calories",

    "Is dosa healthy for weight loss?",

    "Can I eat chocolate cake occasionally?",

    "Best Indian protein foods for gym"
]

for ex in examples:

    st.write(f"• {ex}")

