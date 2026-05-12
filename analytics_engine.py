import pandas as pd

# =========================
# HEALTH SCORE
# =========================

def generate_health_score(df):

    if len(df) == 0:

        return 0

    protein_score = min(
        df['protein'].mean() / 80,
        1
    ) * 30

    calorie_score = 30

    glucose_score = 40

    if df['glucose_peak'].mean() > 140:

        glucose_score = 15

    total = (
        protein_score +
        calorie_score +
        glucose_score
    )

    return round(total)