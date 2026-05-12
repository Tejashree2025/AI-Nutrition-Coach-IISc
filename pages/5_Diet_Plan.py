
# =========================
# FILE: pages/5_Diet_Plan.py

# =========================

import streamlit as st

from backend.diet_targets import (
    get_daily_targets
)

from backend.diet_llm_planner import (
    generate_diet_plan
)

from backend.pdf_report import (
    export_diet_pdf
)

from database import (
    get_user_profile
)

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="AI Diet Plan",
    page_icon="📅",
    layout="wide"
)

# =========================
# LOGIN CHECK
# =========================

if "logged_in" not in st.session_state:

    st.error("Please login first.")
    st.stop()

if "user_id" not in st.session_state:

    st.error("Session expired.")
    st.stop()

# =========================
# PROFILE
# =========================

profile = get_user_profile(
    st.session_state.user_id
)

if profile is None:

    st.error(
        "User profile not found."
    )

    st.stop()

# =========================
# PROFILE VALUES
# =========================

age = profile["age"]

weight = float(profile["weight"])

height = float(profile["height"])

goal = str(profile["goal"]).lower()

activity = str(
    profile["activity_level"]
).lower()

diet_type = str(
    profile["diet_type"]
).lower()

gender = str(
    profile["gender"]
).lower()

# =========================
# TITLE
# =========================

st.title(
    "📅 AI Personalized Diet Plan"
)

st.caption(
    "LLM + RAG Powered Adaptive Nutrition Planning"
)

# =========================
# PROFILE UI
# =========================

st.subheader(
    "👤 User Profile"
)

col1, col2 = st.columns(2)

with col1:

    st.write(f"Age: {age}")
    st.write(f"Weight: {weight} kg")
    st.write(f"Height: {height} cm")

with col2:

    st.write(f"Goal: {goal}")
    st.write(f"Activity: {activity}")
    st.write(f"Diet Type: {diet_type}")
    st.write(f"Gender: {gender}")

# =========================
# PREFERENCES
# =========================

st.subheader(
    "⚙ Personalized Preferences"
)

allergies = st.text_input(
    "Food Allergies / Avoid",
    "soya chunk"
)

meals_per_day = st.selectbox(
    "Meals Per Day",
    [3, 4, 5]
)

water = st.text_input(
    "Daily Water Intake",
    "3 Liters"
)

plan_type = st.selectbox(
    "Diet Plan Type",
    [
        "Balanced",
        "High Protein",
        "Low Carb"
    ]
)

# =========================
# GENERATE
# =========================

if st.button(
    "Generate AI Diet Plan"
):

    targets = get_daily_targets(
        goal,
        weight
    )

    profile_data = {

        "goal": goal,

        "diet_type": diet_type,

        "activity": activity,

        "allergies": allergies,

        "meals_per_day": meals_per_day,

        "water_intake": water,

        "plan_type": plan_type
    }

    plan = generate_diet_plan(
        profile_data,
        targets
    )

    st.success(
        "✅ Personalized AI Diet Plan Generated"
    )

    # =========================
    # TARGETS
    # =========================

    a, b, c = st.columns(3)

    a.metric(
        "Calories Target",
        f"{targets['Calories']} kcal"
    )

    b.metric(
        "Protein Goal",
        f"{targets['Protein']} g"
    )

    c.metric(
        "Water Goal",
        water
    )

    # =========================
    # PLAN
    # =========================

    st.subheader(
        "🥗 Personalized Indian Diet Plan"
    )

    st.write(plan)

    # =========================
    # PDF
    # =========================

    pdf_content = f"""

AI Personalized Diet Plan

Calories Target:
{targets['Calories']} kcal

Protein Goal:
{targets['Protein']} g

Water Intake:
{water}

Diet Plan:

{plan}

"""

    pdf_path = export_diet_pdf(
        pdf_content
    )

    with open(
        pdf_path,
        "rb"
    ) as file:

        st.download_button(

            label="📥 Download Diet Plan PDF",

            data=file,

            file_name="AI_Diet_Plan.pdf",

            mime="application/pdf"
        )

