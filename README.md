🥗 AI Nutrition Coach — IISc Final Project

LLM + RAG Powered Personalized Nutrition Recommendation System

📌 Project Overview

AI Nutrition Coach is an intelligent personalized nutrition and meal recommendation platform developed as an IISc final project.

The system combines:

Large Language Models (LLMs)
Retrieval Augmented Generation (RAG)
Glucose prediction
Personalized diet planning
Meal tracking
AI nutrition insights
Indian food nutrition analysis

to generate adaptive and personalized dietary recommendations.

🚀 Features
✅ Personalized Diet Planning
AI-generated Indian diet plans
Veg / Non-Veg / Mixed support
Weight loss / maintenance / muscle gain goals
High protein / balanced meal plans
✅ Meal Tracker
Calorie estimation
Macronutrient tracking
Glucose prediction
Meal quality scoring
Nutrition insights
✅ AI Nutrition Chatbot
LLM powered nutrition assistant
Indian food recommendations
Healthy eating guidance
✅ Glucose Prediction Engine
Glycemic load estimation
Meal-based glucose spike prediction
Risk classification
✅ Admin Dashboard
User analytics
Meal history monitoring
Nutrition trends
✅ PDF Export
Download personalized diet plans
🧠 AI Technologies Used
Ollama
Qwen LLM
LangChain
RAG Pipeline
ChromaDB
Embeddings
Vector Search
🛠 Tech Stack
Technology	Usage
Python	Core backend
Streamlit	Frontend UI
FastAPI	API backend
SQLite	Database
Pandas	Data processing
Ollama	Local LLM
LangChain	LLM orchestration
ChromaDB	Vector database
📂 Project Structure
AI-Nutrition-Coach-IISc/
│
├── backend/
├── pages/
├── datasets/
├── rag/
├── chroma_db/
├── reports/
├── screenshots/
│
├── main.py
├── database.py
├── requirements.txt
├── README.md
└── nutrition_app.db
⚙ Installation Guide
1. Clone Repository
git clone https://github.com/Tejashree2025/AI-Nutrition-Coach-IISc.git
2. Install Requirements
pip install -r requirements.txt
🤖 Run Ollama

Install Ollama:

https://ollama.com/download

Run model:

ollama run qwen:latest
🚀 Run FastAPI Backend
uvicorn main:app --reload
🌐 Run Streamlit Frontend
streamlit run Home.py
👨‍💼 Admin Access

Admin access is available for evaluation and testing.

📊 Core Modules
Nutrition Engine
Diet Planner
Meal Tracker
Glucose Prediction
AI Chatbot
Recommendation Engine
RAG Retrieval Engine
Admin Dashboard
📈 Future Improvements
Real-time CGM integration
Mobile app deployment
Voice-based nutrition assistant
Wearable device integration
Deep learning glucose forecasting
👩‍💻 Developed By

Tejashree2025

IISc Final Year Project

AI Powered Personalized Nutrition Recommendation System

📜 License

This project is developed for educational and research purposes.