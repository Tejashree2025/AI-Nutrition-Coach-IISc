# 🧠 AI Personalized Nutrition & Fitness Coach

LLM + RAG Powered Adaptive Indian Nutrition Intelligence System

---

# 📌 Project Overview

This project is an AI-powered personalized nutrition and fitness recommendation system designed for Indian dietary habits.

The system combines:

- Large Language Models (LLMs)
- Retrieval-Augmented Generation (RAG)
- Nutrition Intelligence
- Glucose Prediction
- Personalized Meal Planning
- User Memory
- Adaptive Recommendations

The platform analyzes meals, predicts glucose response, generates personalized diet plans, and provides intelligent nutrition guidance.

---

# 🚀 Key Features

## 🍽 AI Meal Analysis

- Nutrition breakdown
- Calories
- Protein
- Carbohydrates
- Fiber
- Meal quality scoring

---

## 🩸 Glucose Prediction Engine

- Predicts glucose spikes
- Glycemic load estimation
- Risk-level detection
- Diabetic-aware recommendations

---

## 🤖 AI Nutrition Chatbot

- LLM-powered chatbot
- Personalized nutrition guidance
- Indian food recommendations
- Weight loss / muscle gain support

---

## 📅 AI Personalized Diet Planning

- Adaptive meal generation
- Weekly meal rotation
- Budget-based diet planning
- Diabetic diet mode
- South Indian / North Indian personalization

---

## 🛒 Grocery Recommendation System

Automatically generates:

- Vegetable list
- Protein sources
- Healthy snacks
- Grain recommendations

---

## 🧠 User Memory System

Stores:

- Previous meals
- Preferences
- Allergies
- Disliked foods
- Historical nutrition behavior

---

## 🔍 RAG + Embedding Pipeline

- Semantic food retrieval
- Vector database support
- ChromaDB integration
- Embedding-based nutrition search
- Retrieval-Augmented Generation architecture

---

# 🏗 System Architecture

```text
                    ┌─────────────────────┐
                    │     User Input      │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   FastAPI Backend   │
                    └──────────┬──────────┘
                               │
        ┌──────────────────────┼──────────────────────┐
        │                      │                      │
        ▼                      ▼                      ▼
┌───────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ Nutrition AI │    │ Glucose Engine │    │ User Memory AI │
└──────┬────────┘    └────────┬────────┘    └────────┬────────┘
       │                      │                      │
       └──────────────────────┼──────────────────────┘
                              ▼
                  ┌─────────────────────┐
                  │  RAG Retrieval Layer │
                  └──────────┬──────────┘
                             │
               ┌─────────────┴─────────────┐
               ▼                           ▼
      ┌─────────────────┐       ┌──────────────────┐
      │ Sentence Encoder │       │   Chroma Vector  │
      │  Embeddings AI   │       │      Database    │
      └─────────────────┘       └──────────────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │  LLM (Qwen/Ollama)  │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │ Personalized Output │
                  └─────────────────────┘