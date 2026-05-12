
# =========================
# FILE: backend/nutrition_engine.py
# =========================

import re
import pandas as pd

from rapidfuzz import process

# =========================
# LOAD DATASET
# =========================

food_db = pd.read_csv(
   "datasets/Indian_Food_Nutrition_Processed.csv"
)

# =========================
# AUTO DETECT FOOD COLUMN
# =========================

possible_food_columns = [

    "Food",

    "Dish Name",

    "food",

    "dish",

    "Item"
]

FOOD_COLUMN = None

for col in possible_food_columns:

    if col in food_db.columns:

        FOOD_COLUMN = col

        break

if FOOD_COLUMN is None:

    raise Exception(
        f"Food column not found. Available columns: {food_db.columns.tolist()}"
    )

# =========================
# COLUMN MAP
# =========================

COLUMN_MAP = {

    "calories": [

        "Calories",

        "Calories (kcal)",

        "calories"
    ],

    "protein": [

        "Protein",

        "Protein (g)",

        "protein"
    ],

    "carbs": [

        "Carbs",

        "Carbohydrates (g)",

        "carbs"
    ],

    "fat": [

        "Fat",

        "Fats (g)",

        "fat"
    ],

    "fiber": [

        "Fiber",

        "Fibre (g)",

        "fiber"
    ]
}

# =========================
# GET COLUMN
# =========================

def get_column(possible_names):

    for col in possible_names:

        if col in food_db.columns:

            return col

    return None

CALORIES_COL = get_column(
    COLUMN_MAP["calories"]
)

PROTEIN_COL = get_column(
    COLUMN_MAP["protein"]
)

CARBS_COL = get_column(
    COLUMN_MAP["carbs"]
)

FAT_COL = get_column(
    COLUMN_MAP["fat"]
)

FIBER_COL = get_column(
    COLUMN_MAP["fiber"]
)

# =========================
# CLEAN FOOD NAMES
# =========================

def clean_food_name(food):

    food = str(food).lower()

    food = food.replace("(", " ")

    food = food.replace(")", " ")

    food = food.replace("-", " ")

    food = re.sub(
        r"[^a-zA-Z ]",
        "",
        food
    )

    return food.strip()

food_db["clean_name"] = food_db[
    FOOD_COLUMN
].astype(str).apply(clean_food_name)

# =========================
# FOOD ALIASES
# =========================

FOOD_ALIASES = {

    "roti": "chapati",

    "curd": "yogurt",

    "anda": "egg",

    "dal": "lentils",

    "paneer curry": "paneer",

    "chicken curry": "chicken",

    "fish curry": "fish",

    "milkshake": "milk",

    "tea": "green tea",

    "veggies": "vegetable",

    "sabji": "vegetable",

    "nuts": "almonds"
}

# =========================
# QUANTITY MULTIPLIERS
# =========================

UNIT_MULTIPLIERS = {

    # breads

    "chapati": 1,
    "roti": 1,
    "slice": 1,
    "slices": 1,

    # liquids

    "glass": 1,
    "cup": 1,
    "cups": 1,

    # curry / bowl

    "bowl": 1.2,
    "plate": 1.5,

    # eggs

    "egg": 1,
    "eggs": 1,

    # nuts

    "nuts": 0.08,
    "almonds": 0.08,
    "cashews": 0.08,
    "peanuts": 0.08,

    # spoon

    "tablespoon": 0.15,
    "tbsp": 0.15,

    # salad

    "salad": 1,

    # smoothie

    "smoothie": 1
}

# =========================
# SPLIT ITEMS
# =========================

def split_meal_items(text):

    text = text.lower()

    splitters = [

        ",",

        " and ",

        "+",

        " with "
    ]

    for splitter in splitters:

        text = text.replace(
            splitter,
            "|"
        )

    return [

        x.strip()

        for x in text.split("|")

        if x.strip()
    ]

# =========================
# EXTRACT QUANTITY
# =========================

def extract_quantity(item_text):

    item_text = item_text.lower()

    quantity = 1

    # =========================
    # NUMBER
    # =========================

    quantity_match = re.search(
        r"(\d+(\.\d+)?)",
        item_text
    )

    if quantity_match:

        quantity = float(
            quantity_match.group(1)
        )

    # =========================
    # GRAMS
    # =========================

    gram_match = re.search(
        r"(\d+)g",
        item_text
    )

    if gram_match:

        grams = float(
            gram_match.group(1)
        )

        quantity = grams / 100

        return max(quantity, 0.1)

    # =========================
    # APPLY MULTIPLIERS
    # =========================

    for unit, multiplier in UNIT_MULTIPLIERS.items():

        if unit in item_text:

            quantity = quantity * multiplier

            break

    # =========================
    # LIMIT HUGE VALUES
    # =========================

    quantity = min(quantity, 4)

    return max(quantity, 0.1)

# =========================
# NORMALIZE FOOD
# =========================

def normalize_food_name(food):

    food = clean_food_name(food)

    for alias, replacement in FOOD_ALIASES.items():

        if alias in food:

            food = food.replace(
                alias,
                replacement
            )

    return food.strip()

# =========================
# FUZZY MATCH
# =========================

def fuzzy_match_food(food_name):

    choices = food_db[
        "clean_name"
    ].tolist()

    match = process.extractOne(
        food_name,
        choices
    )

    if not match:

        return None

    matched_name = match[0]

    score = match[1]

    if score < 60:

        return None

    row = food_db[
        food_db["clean_name"] == matched_name
    ]

    if len(row) == 0:

        return None

    return row.iloc[0]

# =========================
# SAFE FLOAT
# =========================

def safe_float(value):

    try:

        return float(value)

    except:

        return 0

# =========================
# MEAL SCORE
# =========================

def calculate_meal_score(
    total,
    goal
):

    score = 50

    protein = total["protein"]

    fiber = total["fiber"]

    calories = total["calories"]

    # protein

    if protein >= 20:

        score += 20

    elif protein >= 15:

        score += 10

    # fiber

    if fiber >= 8:

        score += 15

    # calories

    if calories <= 600:

        score += 10

    # weight loss bonus

    if goal == "weight_loss":

        if calories <= 500:

            score += 5

    return min(score, 100)

# =========================
# ANALYZE MEAL
# =========================

def analyze_meal(

    meal_text,
    goal,
    diet_type
):

    items = split_meal_items(
        meal_text
    )

    total = {

        "calories": 0,

        "protein": 0,

        "carbs": 0,

        "fat": 0,

        "fiber": 0
    }

    detailed_items = []

    for item in items:

        quantity = extract_quantity(
            item
        )

        normalized_item = normalize_food_name(
            item
        )

        row = fuzzy_match_food(
            normalized_item
        )

        if row is None:

            continue

        calories = safe_float(

            row.get(
                CALORIES_COL,
                0
            )

        ) * quantity

        protein = safe_float(

            row.get(
                PROTEIN_COL,
                0
            )

        ) * quantity

        carbs = safe_float(

            row.get(
                CARBS_COL,
                0
            )

        ) * quantity

        fat = safe_float(

            row.get(
                FAT_COL,
                0
            )

        ) * quantity

        fiber = safe_float(

            row.get(
                FIBER_COL,
                0
            )

        ) * quantity

        # =========================
        # TOTALS
        # =========================

        total["calories"] += calories

        total["protein"] += protein

        total["carbs"] += carbs

        total["fat"] += fat

        total["fiber"] += fiber

        # =========================
        # ITEM DETAILS
        # =========================

        detailed_items.append({

            "food": normalized_item,

            "quantity_multiplier": round(
                quantity,
                2
            ),

            "calories": round(
                calories,
                2
            ),

            "protein": round(
                protein,
                2
            ),

            "carbs": round(
                carbs,
                2
            ),

            "fat": round(
                fat,
                2
            ),

            "fiber": round(
                fiber,
                2
            )
        })

    # =========================
    # ROUND TOTALS
    # =========================

    for key in total:

        total[key] = round(
            total[key],
            2
        )

    # =========================
    # SCORE
    # =========================

    total["meal_quality_score"] = calculate_meal_score(

        total,

        goal
    )

    # =========================
    # RETURN
    # =========================

    return {

        "items": detailed_items,

        "totals": total
    }

