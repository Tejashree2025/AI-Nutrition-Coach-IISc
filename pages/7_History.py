
# =========================
# FILE: pages/7_History.py
# FINAL UPDATED VERSION
# =========================

import streamlit as st
import pandas as pd
import sqlite3

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(

    page_title="Meal History",

    page_icon="📜",

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

if "user" not in st.session_state:

    st.error(
        "Session expired. Please login again."
    )

    st.stop()

# =========================
# USER
# =========================

username = st.session_state.user

# =========================
# TITLE
# =========================

st.title(
    "📜 Meal History"
)

st.caption(
    "Track your previous meals, nutrition, and glucose responses"
)

# =========================
# DATABASE
# =========================

conn = sqlite3.connect(
    "nutrition_app.db"
)

# =========================
# LOAD DATA
# =========================

try:

    query = """

    SELECT *

    FROM meal_history

    WHERE username = ?

    ORDER BY id DESC

    """

    df = pd.read_sql_query(

        query,

        conn,

        params=(username,)
    )

except Exception as e:

    st.error(
        f"Database Error: {e}"
    )

    conn.close()

    st.stop()

conn.close()

# =========================
# EMPTY CHECK
# =========================

if len(df) == 0:

    st.warning(
        "No meal history found."
    )

    st.stop()

# =========================
# SHOW DATA
# =========================

st.subheader(
    "🍽 Previous Meals"
)

st.dataframe(
    df,
    use_container_width=True
)

# =========================
# CHARTS
# =========================

numeric_columns = []

for col in [

    "calories",
    "protein",
    "carbs",
    "fat",
    "glucose"

]:

    if col in df.columns:

        numeric_columns.append(col)

# =========================
# CALORIES
# =========================

if "calories" in df.columns:

    st.subheader(
        "📈 Calories Trend"
    )

    st.line_chart(
        df["calories"]
    )

# =========================
# PROTEIN
# =========================

if "protein" in df.columns:

    st.subheader(
        "💪 Protein Trend"
    )

    st.bar_chart(
        df["protein"]
    )

# =========================
# GLUCOSE
# =========================

if "glucose" in df.columns:

    st.subheader(
        "🩸 Glucose Trend"
    )

    st.line_chart(
        df["glucose"]
    )

# =========================
# SUMMARY
# =========================

st.subheader(
    "📊 Nutrition Summary"
)

summary = {}

for col in numeric_columns:

    summary[col] = round(
        df[col].mean(),
        2
    )

st.json(summary)

