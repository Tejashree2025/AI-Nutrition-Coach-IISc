
# =========================
# FILE: pages/2_Signup.py

# =========================

import streamlit as st

from database import (
    register_user
)

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(

    page_title="Signup",

    page_icon="📝",

    layout="centered"
)

# =========================
# CUSTOM UI
# =========================

st.markdown("""

<style>

.main {
    background-color: #f8fafc;
}

.signup-box {

    background: white;

    padding: 2rem;

    border-radius: 20px;

    box-shadow: 0px 4px 20px rgba(0,0,0,0.08);

    margin-top: 20px;
}

.title {

    text-align: center;

    font-size: 34px;

    font-weight: bold;

    color: #0f172a;
}

.subtitle {

    text-align: center;

    color: gray;

    margin-bottom: 25px;
}

</style>

""", unsafe_allow_html=True)

# =========================
# TITLE
# =========================

st.markdown(
    "<div class='title'>📝 Create Account</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Join the AI Nutrition Coach Platform</div>",
    unsafe_allow_html=True
)

# =========================
# FORM
# =========================

with st.container():

    st.markdown(
        "<div class='signup-box'>",
        unsafe_allow_html=True
    )

    name = st.text_input(
        "👤 Full Name"
    )

    username = st.text_input(
        "🆔 Username"
    )

    password = st.text_input(
        "🔑 Password",
        type="password"
    )

    age = st.number_input(
        "🎂 Age",
        min_value=10,
        max_value=100,
        value=24
    )

    weight = st.number_input(
        "⚖ Weight (kg)",
        min_value=20.0,
        max_value=250.0,
        value=58.0
    )

    height = st.number_input(
        "📏 Height (cm)",
        min_value=100.0,
        max_value=250.0,
        value=162.0
    )

    gender = st.selectbox(

        "🚻 Gender",

        [

            "male",
            "female"
        ]
    )

    goal = st.selectbox(

        "🎯 Goal",

        [

            "weight_loss",
            "maintenance",
            "muscle_gain"
        ]
    )

    activity_level = st.selectbox(

        "🏃 Activity Level",

        [

            "low",
            "moderate",
            "high"
        ]
    )

    diet_type = st.selectbox(

        "🥗 Diet Type",

        [

            "veg",
            "non_veg",
            "mixed"
        ]
    )

    # =========================
    # BUTTON
    # =========================

    if st.button(
        "✅ Create Account",
        use_container_width=True
    ):

        if (

            name == "" or
            username == "" or
            password == ""

        ):

            st.error(
                "Please fill all fields."
            )

        else:

            success = register_user(

                username=username,

                password=password,

                name=name,

                age=age,

                weight=weight,

                height=height,

                gender=gender,

                goal=goal,

                diet_type=diet_type,

                activity_level=activity_level
            )

            if success:

                st.success(
                    "Account created successfully."
                )

                st.info(
                    "Now login from Login page."
                )

            else:

                st.error(
                    "Username already exists."
                )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )

# =========================
# FOOTER
# =========================

st.markdown("---")

st.caption(
    "🥗 Personalized AI Nutrition & Health Platform"
)

