
# =========================
# FILE: main.py
# =========================

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, Any

# =========================
# DATABASE
# =========================

from database import (
    create_tables
)

create_tables()

# =========================
# BACKEND IMPORTS
# =========================

from backend.nutrition_engine import (
    analyze_meal
)

from backend.glucose_model import (
    predict_glucose_response
)

from backend.meal_generator import (
    generate_next_meal
)

from backend.llm_reasoning import (
    generate_ai_insight
)

from backend.memory_engine import (
    load_memory,
    save_user_meal
)

from backend.diet_targets import (
    get_daily_targets
)

from backend.diet_llm_planner import (
    generate_diet_plan
)

from backend.recommendation_engine import (
    generate_recommendations
)

# =========================
# CHATBOT
# =========================

from chatbot import (
    chat_with_bot
)

# =========================
# FASTAPI APP
# =========================

app = FastAPI(

    title="AI Nutrition Coach",

    description="""
    LLM + RAG Powered Personalized Nutrition System
    """,

    version="4.0"
)

# =========================
# USER PROFILE
# =========================

class UserProfile(BaseModel):

    name: str = "User"

    age: int

    weight: float

    height: float

    gender: str

    goal: str

    diet_type: str

    activity_level: str

# =========================
# MEAL REQUEST
# =========================

class MealRequest(BaseModel):

    user_id: str

    profile: UserProfile

    meal_text: str

# =========================
# CHAT REQUEST
# =========================

class ChatRequest(BaseModel):

    profile: Dict[str, Any]

    message: str

# =========================
# DIET PLAN REQUEST
# =========================

class DietPlanRequest(BaseModel):

    age: int

    weight: float

    height: float

    gender: str

    goal: str

    diet_type: str

    activity: str

    allergies: str = ""

    dislikes: str = ""

    meals_per_day: int = 3

    water_intake: str = "3 Liters"

    region: str = "Indian"

    budget: str = "medium"

    diabetic: bool = False

    plan_type: str = "balanced"

# =========================
# HOME ROUTE
# =========================

@app.get("/")

async def home():

    return {

        "message": "AI Nutrition Coach Running Successfully",

        "features": [

            "Meal Nutrition Analysis",

            "Glucose Prediction",

            "AI Meal Recommendations",

            "LLM Nutrition Chatbot",

            "RAG Food Retrieval",

            "Personalized Diet Plans",

            "Memory-Based Personalization",

            "Daily Target Tracking"
        ]
    }

# =========================
# HEALTH CHECK
# =========================

@app.get("/health")

async def health():

    return {

        "status": "healthy"
    }

# =========================
# ANALYZE MEAL API
# =========================

@app.post("/analyze")

async def analyze(
    request: MealRequest
):

    try:

        # =========================
        # NUTRITION ANALYSIS
        # =========================

        nutrition = analyze_meal(

            meal_text=request.meal_text,

            goal=request.profile.goal,

            diet_type=request.profile.diet_type
        )

        # =========================
        # USER MEMORY
        # =========================

        memory = load_memory(
            request.user_id
        )

        # =========================
        # GLUCOSE PREDICTION
        # =========================

        glucose = predict_glucose_response(

            nutrition=nutrition,

            activity_level=request.profile.activity_level,

            memory=memory
        )

        # =========================
        # AI INSIGHT
        # =========================

        insight = generate_ai_insight(

            nutrition=nutrition,

            glucose=glucose,

            goal=request.profile.goal,

            meal_text=request.meal_text
        )

        # =========================
        # SMART SWAP
        # =========================

        next_meal = generate_next_meal(

            nutrition=nutrition,

            goal=request.profile.goal,

            diet_type=request.profile.diet_type,

            glucose=glucose
        )

        # =========================
        # RECOMMENDATIONS
        # =========================

        recommendations = generate_recommendations(

            nutrition,

            glucose,

            request.profile.goal
        )

        # =========================
        # SAVE MEMORY
        # =========================

        save_user_meal(

            request.user_id,

            {

                "meal": request.meal_text,

                "nutrition": nutrition,

                "glucose": glucose
            }
        )

        # =========================
        # RETURN
        # =========================

        return {

            "status": "success",

            "nutrition": nutrition,

            "glucose_prediction": glucose,

            "ai_insight": insight,

            "next_meal": next_meal,

            "recommendations": recommendations
        }

    except Exception as e:

        return {

            "status": "error",

            "message": str(e)
        }

# =========================
# AI CHATBOT API
# =========================

@app.post("/chat")

async def chat(
    request: ChatRequest
):

    try:

        response = chat_with_bot(
            request.message
        )

        return {

            "status": "success",

            "response": response
        }

    except Exception as e:

        return {

            "status": "error",

            "message": str(e)
        }

# =========================
# DAILY TARGETS API
# =========================

@app.get("/daily_targets")

async def daily_targets(

    goal: str,

    weight: float
):

    try:

        targets = get_daily_targets(

            goal=goal,

            weight=weight
        )

        return {

            "status": "success",

            "targets": targets
        }

    except Exception as e:

        return {

            "status": "error",

            "message": str(e)
        }

# =========================
# DIET PLAN API
# =========================

@app.post("/generate_diet_plan")

async def create_diet_plan(

    request: DietPlanRequest
):

    try:

        # =========================
        # DAILY TARGETS
        # =========================

        targets = get_daily_targets(

            goal=request.goal,

            weight=request.weight
        )

        # =========================
        # PROFILE
        # =========================

        profile = {

            "gender": request.gender,

            "goal": request.goal,

            "diet_type": request.diet_type,

            "activity": request.activity,

            "allergies": request.allergies,

            "dislikes": request.dislikes,

            "meals_per_day": request.meals_per_day,

            "water_intake": request.water_intake,

            "region": request.region,

            "budget": request.budget,

            "diabetic": request.diabetic,

            "plan_type": request.plan_type
        }

        # =========================
        # GENERATE PLAN
        # =========================

        plan = generate_diet_plan(

            profile=profile,

            targets=targets
        )

        # =========================
        # RETURN
        # =========================

        return {

            "status": "success",

            "targets": targets,

            "diet_plan": plan
        }

    except Exception as e:

        return {

            "status": "error",

            "message": str(e)
        }

