
# =========================
# FILE: pages/3_Dashboard.py
# =========================

import streamlit as st

from backend.diet_targets import (
    get_daily_targets
)

from database import (
    get_user_profile
)

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(

    page_title="Dashboard",

    page_icon="🏠",

    layout="wide"
)

# =========================
# LOGIN CHECK
# =========================

if "logged_in" not in st.session_state:

    st.error(
        "Please login first."
    )

    st.switch_page(
        "pages/1_Login.py"
    )

    st.stop()

# =========================
# USER
# =========================

user_id = st.session_state.user_id

profile = get_user_profile(
    user_id
)

if profile is None:

    st.error(
        "User profile not found."
    )

    st.stop()

# =========================
# PROFILE VALUES
# =========================

name = profile.get("name", "User")

goal = profile.get(
    "goal",
    "weight_loss"
)

diet_type = profile.get(
    "diet_type",
    "veg"
)

activity = profile.get(
    "activity_level",
    "moderate"
)

weight = float(
    profile.get(
        "weight",
        60
    )
)

height_cm = float(
    profile.get(
        "height",
        170
    )
)

gender = profile.get(
    "gender",
    "male"
)

# =========================
# HEIGHT CONVERSION
# =========================

height_inches = height_cm / 2.54

feet = int(
    height_inches // 12
)

inches = int(
    height_inches % 12
)

height_display = f"{feet} ft {inches} in"

# =========================
# TARGETS
# =========================

targets = get_daily_targets(
    goal,
    weight
)

# =========================
# TITLE
# =========================

st.title(
    f"Welcome {name} 👋"
)

st.caption(
    "Your personalized AI nutrition dashboard"
)

# =========================
# PROFILE CARD
# =========================

st.subheader(
    "👤 User Profile"
)

c1, c2, c3 = st.columns(3)

c1.metric(
    "Goal",
    goal.replace(
        "_",
        " "
    ).title()
)

c2.metric(
    "Diet Type",
    diet_type.title()
)

c3.metric(
    "Weight",
    f"{weight} kg"
)

c4, c5, c6 = st.columns(3)

c4.metric(
    "Height",
    height_display
)

c5.metric(
    "Gender",
    gender.title()
)

c6.metric(
    "Activity",
    activity.title()
)

# =========================
# QUICK ACCESS
# =========================

st.markdown(
    "## 🚀 Quick Access"
)

st.markdown(
    """
    <style>

    div.stButton > button:first-child {

        width: 100%;
        height: 90px;
        font-size: 18px;
        font-weight: bold;
        border-radius: 18px;
        border: none;
        margin-top: 10px;
        margin-bottom: 10px;
        transition: 0.3s;
    }

    div.stButton > button:hover {

        transform: scale(1.03);
        opacity: 0.9;
    }

    </style>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    if st.button(
        "🍽 Meal Tracker"
    ):

        st.switch_page(
            "pages/4_Meal_Tracker.py"
        )

with col2:

    if st.button(
        "📅 Diet Plan"
    ):

        st.switch_page(
            "pages/5_Diet_Plan.py"
        )

col3, col4 = st.columns(2)

with col3:

    if st.button(
        "🤖 AI Chatbot"
    ):

        st.switch_page(
            "pages/6_AI_Chatbot.py"
        )

with col4:

    if st.button(
        "📜 History"
    ):

        st.switch_page(
            "pages/7_History.py"
        )

# =========================
# TARGETS
# =========================

st.subheader(
    "📊 Daily Targets"
)

t1, t2, t3, t4 = st.columns(4)

t1.metric(
    "Calories",
    f"{targets['Calories']} kcal"
)

t2.metric(
    "Protein",
    f"{targets['Protein']} g"
)

t3.metric(
    "Fiber",
    "25 g"
)

t4.metric(
    "Water",
    "3-5 Liters"
)

# =========================
# TIPS
# =========================

st.subheader(
    "💡 Smart Nutrition Tips"
)

tips = [

    "Prioritize protein in every meal.",

    "Add vegetables and salads for better fiber intake.",

    "Stay hydrated throughout the day.",

    "Avoid excessive fried and sugary foods.",

    "Pair carbohydrates with protein for stable energy."
]

for tip in tips:

    st.write(
        f"• {tip}"
    )

