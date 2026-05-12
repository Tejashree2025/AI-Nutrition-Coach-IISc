import json
import os

MEMORY_FILE = "memory.json"


def load_all_memory():

    if not os.path.exists(MEMORY_FILE):

        return {}

    with open(MEMORY_FILE, "r") as f:

        return json.load(f)


def load_memory(user_id):

    data = load_all_memory()

    return data.get(
        user_id,
        {
            "history": []
        }
    )


def save_user_meal(
    user_id,
    meal_data
):

    data = load_all_memory()

    if user_id not in data:

        data[user_id] = {
            "history": []
        }

    data[user_id]["history"].append(
        meal_data
    )

    with open(MEMORY_FILE, "w") as f:

        json.dump(
            data,
            f,
            indent=2
        )