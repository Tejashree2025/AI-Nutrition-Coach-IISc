
# =========================
# FILE: pages/1_Login.py

# WITH ADMIN BUTTON
# =========================

import streamlit as st

from database import (
    login_user
)

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(

    page_title="Login",

    page_icon="🔐",

    layout="centered"
)

# =========================
# CUSTOM CSS
# =========================

st.markdown("""

<style>

.main {
    background-color: #f8fafc;
}

.login-box {

    background: white;

    padding: 2rem;

    border-radius: 20px;

    box-shadow: 0px 4px 20px rgba(0,0,0,0.08);

    margin-top: 20px;
}

.title {

    text-align: center;

    font-size: 36px;

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
    "<div class='title'>🥗 AI Nutrition Coach</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Login to continue to your personalized dashboard</div>",
    unsafe_allow_html=True
)

# =========================
# LOGIN CONTAINER
# =========================

with st.container():

    st.markdown(
        "<div class='login-box'>",
        unsafe_allow_html=True
    )

    username = st.text_input(
        "👤 Username"
    )

    password = st.text_input(
        "🔑 Password",
        type="password"
    )

    # =========================
    # NORMAL LOGIN
    # =========================

    if st.button(
        "🚀 Login",
        use_container_width=True
    ):

        user = login_user(
            username,
            password
        )

        if user:

            st.session_state.logged_in = True

            st.session_state.user_id = username

            st.session_state.user = username

            st.success(
                "Login successful."
            )

            st.switch_page(
                "pages/3_Dashboard.py"
            )

        else:

            st.error(
                "Invalid username or password."
            )

    # =========================
    # ADMIN SECTION
    # =========================

    st.divider()

    st.subheader(
        "👨‍💼 Admin Access"
    )

    admin_password = st.text_input(

        "Enter Admin Password",

        type="password"
    )

    if st.button(
        "🔐 Login as Admin",
        use_container_width=True
    ):

        if admin_password == "123":

            st.session_state.logged_in = True

            st.session_state.user_id = "admin"

            st.session_state.user = "admin"

            st.success(
                "Admin login successful."
            )

            st.switch_page(
                "pages/8_Admin.py"
            )

        else:

            st.error(
                "Invalid admin password."
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
    "🥗 AI Powered Personalized Nutrition & Health Platform"
)

