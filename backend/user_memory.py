# =========================
# FILE: backend/user_memory.py
# =========================

import json
import os

MEMORY_FILE = "user_memory.json"


def load_user_preferences(user_id):

    if not os.path.exists(MEMORY_FILE):

        return {}

    with open(MEMORY_FILE, "r") as f:

        data = json.load(f)

    return data.get(user_id, {})


def save_user_preferences(
    user_id,
    preferences
):

    if os.path.exists(MEMORY_FILE):

        with open(MEMORY_FILE, "r") as f:

            data = json.load(f)

    else:

        data = {}

    data[user_id] = preferences

    with open(MEMORY_FILE, "w") as f:

        json.dump(data, f, indent=4)