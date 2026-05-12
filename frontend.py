import streamlit as st

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="AI Nutrition Coach",
    layout="wide"
)

# =========================
# SESSION DEFAULTS
# =========================

if "logged_in" not in st.session_state:

    st.session_state.logged_in = False

# =========================
# NOT LOGGED IN
# =========================

if not st.session_state.logged_in:

    st.title(
        "🥗 AI Nutrition Coach"
    )

    st.subheader(
        "Context-Aware Personalized Diet Intelligence System"
    )

    st.markdown("---")

    st.warning(
        "Please Login or Signup"
    )

    col1, col2 = st.columns(2)

    with col1:

        if st.button("Login"):

            st.switch_page(
                "pages/1_Login.py"
            )

    with col2:

        if st.button("Signup"):

            st.switch_page(
                "pages/2_Signup.py"
            )

# =========================
# LOGGED IN
# =========================

else:

    username = st.session_state.get(
        "username",
        "User"
    )

    st.title(
        "🥗 AI Nutrition Coach"
    )

    st.subheader(
        "Context-Aware Personalized Diet Intelligence System"
    )

    st.markdown("---")

    st.success(
        f"Welcome {username} 👋"
    )

    st.info(
        "Use sidebar pages."
    )

    st.markdown(
        """
✅ Dashboard

✅ Meal Tracker

✅ AI Diet Plan

✅ AI Chatbot

✅ Meal History

✅ Admin Dashboard
"""
    )

    st.markdown("---")

    st.subheader(
        "👤 User Profile"
    )

    col1, col2 = st.columns(2)

    with col1:

        st.session_state.age = st.number_input(
            "Age",
            min_value=10,
            max_value=100,
            value=st.session_state.get(
                "age",
                24
            )
        )

        st.session_state.weight = st.number_input(
            "Weight (kg)",
            min_value=20,
            max_value=200,
            value=st.session_state.get(
                "weight",
                58
            )
        )

        st.session_state.height = st.number_input(
            "Height (cm)",
            min_value=100,
            max_value=250,
            value=st.session_state.get(
                "height",
                162
            )
        )

    with col2:

        st.session_state.goal = st.selectbox(
            "Goal",
            [
                "weight_loss",
                "maintenance",
                "muscle_gain"
            ]
        )

        st.session_state.activity_level = st.selectbox(
            "Activity Level",
            [
                "low",
                "moderate",
                "high"
            ]
        )

        st.session_state.diet_type = st.selectbox(
            "Diet Type",
            [
                "veg",
                "non_veg",
                "mixed"
            ]
        )

    st.success(
        "✅ Profile Updated"
    )