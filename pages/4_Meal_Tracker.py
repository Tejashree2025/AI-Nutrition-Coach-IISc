
# =========================
# FILE: pages/4_Meal_Tracker.py

# =========================

import streamlit as st
import pandas as pd

from backend.nutrition_engine import analyze_meal
from backend.glucose_model import predict_glucose_response
from backend.meal_generator import generate_next_meal
from backend.llm_reasoning import (
    generate_ai_insight,
    generate_daily_insight
)
from backend.recommendation_engine import (
    generate_recommendations
)
from backend.diet_targets import (
    get_daily_targets
)

from database import (
    get_user_profile,
    save_meal_history
)

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Meal Tracker",
    page_icon="🍽",
    layout="wide"
)

# =========================
# LOGIN CHECK
# =========================

if "logged_in" not in st.session_state:

    st.error("Please login first.")
    st.stop()

if "user_id" not in st.session_state:

    st.error("Session expired. Please login again.")
    st.stop()

# =========================
# USER PROFILE
# =========================

profile = get_user_profile(
    st.session_state.user_id
)

if profile is None:

    st.error("User profile not found.")
    st.stop()

# =========================
# PROFILE VALUES
# =========================

goal = str(profile["goal"]).lower()

diet_type = str(
    profile["diet_type"]
).lower()

activity_level = str(
    profile["activity_level"]
).lower()

weight = float(profile["weight"])

username = profile["name"]

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

st.title("🍽 Meal Tracker")

st.caption(
    "AI Powered Meal Analysis + Glucose Prediction + Smart Nutrition Guidance"
)

# =========================
# MODE
# =========================

mode = st.selectbox(

    "Select Mode",

    [
        "One Meal Calorie Counter",
        "Whole Day Calorie Counter"
    ]
)

# =========================
# TARGETS UI
# =========================

st.subheader(
    "🎯 Daily Nutrition Targets"
)

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Calories",
    f"{targets['Calories']} kcal"
)

c2.metric(
    "Protein",
    f"{targets['Protein']} g"
)

c3.metric(
    "Carbs",
    f"{targets['Carbs']} g"
)

c4.metric(
    "Fat",
    f"{targets['Fat']} g"
)

st.info(
    "Recommended Fiber Intake: 25 g"
)

# =========================
# SINGLE MEAL MODE
# =========================

if mode == "One Meal Calorie Counter":

    st.subheader(
        "🍛 Single Meal Analysis"
    )

    meal = st.text_area(

        "Enter Meal",

        "2 chapati, dal, salad"
    )

    if st.button(
        "Analyze Meal"
    ):

        nutrition = analyze_meal(
            meal,
            goal,
            diet_type
        )

        glucose = predict_glucose_response(
            nutrition,
            activity_level,
            {}
        )

        insight = generate_ai_insight(
            nutrition,
            glucose,
            goal,
            meal
        )

        next_meal = generate_next_meal(
            nutrition,
            goal,
            diet_type,
            glucose
        )

        recommendations = generate_recommendations(
            nutrition,
            glucose,
            goal,
            diet_type
        )

        # =========================
        # SAVE HISTORY
        # =========================

        save_meal_history(
            username,
            meal,
            nutrition,
            glucose
        )

        st.success(
            "Meal analyzed successfully"
        )

        # =========================
        # METRICS
        # =========================

        m1, m2, m3 = st.columns(3)

        m1.metric(
            "Calories",
            round(
                nutrition["totals"]["calories"],
                2
            )
        )

        m2.metric(
            "Protein",
            round(
                nutrition["totals"]["protein"],
                2
            )
        )

        m3.metric(
            "Glucose",
            round(
                glucose["predicted_peak"],
                2
            )
        )

        # =========================
        # NUTRITION
        # =========================

        st.subheader(
            "🥗 Nutrition Breakdown"
        )

        st.json(
            nutrition["totals"]
        )

        st.subheader(
            "🍽 Meal Components"
        )

        st.json(
            nutrition["items"]
        )

        # =========================
        # GLUCOSE
        # =========================

        st.subheader(
            "🩸 Glucose Prediction"
        )

        st.json(
            glucose
        )

        # =========================
        # AI INSIGHT
        # =========================

        st.subheader(
            "🧠 AI Insight"
        )

        st.write(
            insight
        )

        # =========================
        # SWAP
        # =========================

        st.subheader(
            "🔁 Suggested Better Swap"
        )

        st.write(
            f"Recommended Meal: {next_meal['recommended_meal']}"
        )

        st.write(
            f"Reason: {next_meal['reason']}"
        )

        # =========================
        # RECOMMENDATIONS
        # =========================

        st.subheader(
            "📌 Personalized Recommendations"
        )

        for rec in recommendations:

            st.write(
                f"• {rec}"
            )

# =========================
# WHOLE DAY MODE
# =========================

else:

    st.subheader(
        "🌞 Whole Day Meal Tracking"
    )

    breakfast = st.text_area(
        "🥣 Breakfast"
    )

    lunch = st.text_area(
        "🍛 Lunch"
    )

    snack = st.text_area(
        "🥜 Snack"
    )

    dinner = st.text_area(
        "🍲 Dinner"
    )

    if st.button(
        "Analyze Full Day"
    ):

        meals = {

            "Breakfast": breakfast,

            "Lunch": lunch,

            "Snack": snack,

            "Dinner": dinner
        }

        total_calories = 0
        total_protein = 0
        total_carbs = 0
        total_fat = 0
        total_fiber = 0

        glucose_values = []

        chart_data = []

        daily_recommendations = []

        # =========================
        # LOOP
        # =========================

        for meal_name, meal_text in meals.items():

            if meal_text.strip() == "":

                continue

            nutrition = analyze_meal(
                meal_text,
                goal,
                diet_type
            )

            glucose = predict_glucose_response(
                nutrition,
                activity_level,
                {}
            )

            recommendations = generate_recommendations(
                nutrition,
                glucose,
                goal,
                diet_type
            )

            for rec in recommendations:

                if rec not in daily_recommendations:

                    daily_recommendations.append(rec)

            totals = nutrition["totals"]

            total_calories += totals["calories"]
            total_protein += totals["protein"]
            total_carbs += totals["carbs"]
            total_fat += totals["fat"]
            total_fiber += totals["fiber"]

            glucose_values.append(
                glucose["predicted_peak"]
            )

            # =========================
            # SAVE HISTORY
            # =========================

            save_meal_history(
                username,
                meal_text,
                nutrition,
                glucose
            )

            st.success(
                f"✅ {meal_name}"
            )

            a, b, c = st.columns(3)

            a.metric(
                "Calories",
                round(
                    totals["calories"],
                    2
                )
            )

            b.metric(
                "Protein",
                round(
                    totals["protein"],
                    2
                )
            )

            c.metric(
                "Glucose",
                round(
                    glucose["predicted_peak"],
                    2
                )
            )

            st.json(
                totals
            )

            st.json(
                glucose
            )

            chart_data.append({

                "Meal": meal_name,

                "Calories": totals["calories"],

                "Protein": totals["protein"],

                "Glucose": glucose["predicted_peak"]
            })

        # =========================
        # SUMMARY
        # =========================

        st.subheader(
            "📊 Daily Summary"
        )

        summary = {

            "Calories": round(
                total_calories,
                2
            ),

            "Protein": round(
                total_protein,
                2
            ),

            "Carbs": round(
                total_carbs,
                2
            ),

            "Fat": round(
                total_fat,
                2
            ),

            "Fiber": round(
                total_fiber,
                2
            ),

            "Average_Glucose": round(
                sum(glucose_values) / len(glucose_values),
                2
            )
        }

        st.json(
            summary
        )

        # =========================
        # RECOMMENDATIONS
        # =========================

        st.subheader(
            "🔁 Overall Better Swaps"
        )

        for rec in daily_recommendations:

            st.write(
                f"• {rec}"
            )

        # =========================
        # AI DAILY INSIGHT
        # =========================

        st.subheader(
            "🧠 Daily AI Nutrition Insight"
        )

        daily_insight = generate_daily_insight(
            summary,
            goal
        )

        st.write(
            daily_insight
        )

        # =========================
        # CHARTS
        # =========================

        df = pd.DataFrame(
            chart_data
        )

        st.subheader(
            "📈 Calories"
        )

        st.bar_chart(
            df.set_index("Meal")[["Calories"]]
        )

        st.subheader(
            "💪 Protein"
        )

        st.bar_chart(
            df.set_index("Meal")[["Protein"]]
        )

        st.subheader(
            "🩸 Glucose"
        )

        st.line_chart(
            df.set_index("Meal")[["Glucose"]]
        )

