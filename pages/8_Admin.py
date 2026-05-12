
# =========================
# FILE: pages/8_Admin.py
# =========================

import streamlit as st
import sqlite3
import pandas as pd

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(

    page_title="Admin Dashboard",

    page_icon="🛠",

    layout="wide"
)

# =========================
# LOGIN CHECK
# =========================

if "logged_in" not in st.session_state:

    st.error(
        "Please login first."
    )

    st.stop()

if "user_id" not in st.session_state:

    st.error(
        "Session expired. Please login again."
    )

    st.stop()

# =========================
# ADMIN CHECK
# =========================

if st.session_state.user.lower() != "admin":

    st.warning(
        "Access denied. Admins only."
    )

    st.stop()


# =========================
# TITLE
# =========================

st.title(
    "🛠 Admin Dashboard"
)

st.caption(
    "Manage users, meals, analytics, and AI nutrition system data"
)

# =========================
# DATABASE
# =========================

conn = sqlite3.connect(
    "nutrition_app.db",
    check_same_thread=False
)

cursor = conn.cursor()

# =========================
# LOAD USERS
# =========================

try:

    users_df = pd.read_sql_query(

        """
        SELECT
            id,
            name,
            age,
            gender,
            weight,
            height,
            goal,
            diet_type,
            activity_level
        FROM users
        """,

        conn
    )

except:

    users_df = pd.DataFrame()

# =========================
# LOAD MEAL HISTORY
# =========================

try:

    meals_df = pd.read_sql_query(

        """
        SELECT *
        FROM meal_history
        ORDER BY id DESC
        """,

        conn
    )

except:

    meals_df = pd.DataFrame()

# =========================
# TOP METRICS
# =========================

total_users = len(users_df)

total_meals = len(meals_df)

avg_calories = 0

if not meals_df.empty:

    try:

        avg_calories = round(
            meals_df["calories"].mean(),
            2
        )

    except:

        avg_calories = 0

m1, m2, m3 = st.columns(3)

m1.metric(
    "👥 Total Users",
    total_users
)

m2.metric(
    "🍽 Meals Logged",
    total_meals
)

m3.metric(
    "🔥 Avg Calories",
    avg_calories
)

st.divider()

# =========================
# USERS SECTION
# =========================

st.subheader(
    "👤 Registered Users"
)

if not users_df.empty:

    st.dataframe(

        users_df,

        use_container_width=True
    )

else:

    st.info(
        "No users found."
    )

# =========================
# USER GOAL ANALYTICS
# =========================

if not users_df.empty:

    st.subheader(
        "🎯 User Goal Distribution"
    )

    goal_counts = users_df[
        "goal"
    ].value_counts()

    st.bar_chart(
        goal_counts
    )

# =========================
# DIET TYPE ANALYTICS
# =========================

if not users_df.empty:

    st.subheader(
        "🥗 Diet Type Distribution"
    )

    diet_counts = users_df[
        "diet_type"
    ].value_counts()

    st.bar_chart(
        diet_counts
    )

# =========================
# MEAL HISTORY
# =========================

st.subheader(
    "📜 Meal History"
)

if not meals_df.empty:

    st.dataframe(

        meals_df,

        use_container_width=True
    )

else:

    st.info(
        "No meal history found."
    )

# =========================
# CALORIE ANALYTICS
# =========================

if not meals_df.empty:

    if "calories" in meals_df.columns:

        st.subheader(
            "📈 Calories Analytics"
        )

        calorie_chart = meals_df[
            ["username", "calories"]
        ]

        st.bar_chart(
            calorie_chart.set_index(
                "username"
            )
        )

# =========================
# GLUCOSE ANALYTICS
# =========================

if not meals_df.empty:

    if "glucose_peak" in meals_df.columns:

        st.subheader(
            "🩸 Glucose Peaks"
        )

        glucose_chart = meals_df[
            ["username", "glucose_peak"]
        ]

        st.line_chart(
            glucose_chart.set_index(
                "username"
            )
        )

# =========================
# DELETE USER
# =========================

st.divider()

st.subheader(
    "🗑 Delete User"
)

if not users_df.empty:

    selected_user = st.selectbox(

        "Select User",

        users_df["name"].tolist()
    )

    if st.button(
        "Delete User"
    ):

        try:

            cursor.execute(

                """
                DELETE FROM users
                WHERE name=?
                """,

                (selected_user,)
            )

            conn.commit()

            st.success(
                f"{selected_user} deleted successfully."
            )

            st.rerun()

        except Exception as e:

            st.error(str(e))

# =========================
# EXPORT DATA
# =========================

st.divider()

st.subheader(
    "⬇ Export Data"
)

if not users_df.empty:

    csv_users = users_df.to_csv(
        index=False
    )

    st.download_button(

        label="Download Users CSV",

        data=csv_users,

        file_name="users_data.csv",

        mime="text/csv"
    )

if not meals_df.empty:

    csv_meals = meals_df.to_csv(
        index=False
    )

    st.download_button(

        label="Download Meal History CSV",

        data=csv_meals,

        file_name="meal_history.csv",

        mime="text/csv"
    )

# =========================
# SYSTEM INFO
# =========================

st.divider()

st.subheader(
    "⚙ System Information"
)

st.info(
    """
    AI Nutrition Coach System

    • Streamlit Frontend
    • FastAPI Backend
    • SQLite Database
    • Ollama LLM
    • RAG Nutrition Retrieval
    • Glucose Prediction Engine
    • Personalized Meal Recommendations
    """
)

# =========================
# CLOSE DB
# =========================

conn.close()

