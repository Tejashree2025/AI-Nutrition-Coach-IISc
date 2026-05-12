# =========================
# FILE: backend/weekly_rotation.py
# =========================

import random

BREAKFASTS = [

    "Moong dal chilla + curd",
    "Oats smoothie + almonds",
    "Greek yogurt + fruits",
    "Vegetable poha + sprouts",
    "Besan chilla + mint chutney"
]

LUNCHES = [

    "Millet roti + paneer bhurji",
    "Brown rice + dal + salad",
    "Rajma + brown rice",
    "Vegetable khichdi + curd",
    "Chicken curry + millet"
]

DINNERS = [

    "Paneer tikka + vegetables",
    "Vegetable soup + salad",
    "Grilled chicken + sautéed vegetables",
    "Dal + sautéed vegetables",
    "Tofu stir fry"
]


def generate_weekly_rotation():

    week = {}

    days = [

        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]

    for day in days:

        week[day] = {

            "breakfast": random.choice(BREAKFASTS),

            "lunch": random.choice(LUNCHES),

            "dinner": random.choice(DINNERS)
        }

    return week