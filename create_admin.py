
import sqlite3

# =========================
# CONNECT DATABASE
# =========================

conn = sqlite3.connect(
    "nutrition_app.db"
)

cursor = conn.cursor()

# =========================
# CREATE ADMIN USER
# =========================

try:

    cursor.execute(
        """
        INSERT INTO users (
            name,
            password,
            age,
            weight,
            height,
            gender,
            goal,
            diet_type,
            activity_level
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            "Admin",
            "admin123",
            30,
            70,
            170,
            "male",
            "maintenance",
            "mixed",
            "moderate"
        )
    )

    conn.commit()

    print(
        "✅ Admin created successfully"
    )

except Exception as e:

    print(
        "⚠ Error:",
        e
    )

conn.close()

