# CrisisLens-AI

An AI-powered civic intelligence and disaster response platform built for the AlgoHub-2025 Hackathon. CrisisLens-AI provides real-time disaster mapping, AI-driven emergency briefings, and logistical tracking for citizens, NGOs, and Government authorities.

## 🚀 Live Demo

- **Frontend (Citizen/Gov Dashboard):** [Deploying to Vercel...] *(Update link once deployed)*
- **Backend API:** [Deploying to Render...] *(Update link once deployed)*

## 🛠️ Tech Stack

- **Frontend:** React (Vite), Leaflet (Maps), Vanilla CSS (Glassmorphism UI)
- **Backend:** FastAPI (Python), Uvicorn
- **AI/ML Layer:** Groq (Llama-3-70b) for NLP analysis, XGBoost/RandomForest for structured severity prediction

## 📂 Project Structure

- `frontend/`: React + Vite frontend application.
- `api_server.py`: FastAPI main application entry point.
- `utils/`: Reusable ML pipelines, AI prompt handlers, and maps logic.
- `notebooks/`: Jupyter notebooks for training ML models.
- `models/`: Trained ML model artifacts (`.pkl` files).
- `data/`: Datasets used for training the severity prediction modules.

## ⚙️ Getting Started (Local Development)

### 1. Backend (FastAPI)
Ensure you have Python 3.9+ installed.

```bash
# Create a virtual environment
python -m venv venv
venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt

# Start the FastAPI server
python -m uvicorn api_server:app --reload
```
The backend will run on `http://localhost:8000`.

### 2. Frontend (React + Vite)
Ensure you have Node.js installed.

```bash
cd frontend

# Install dependencies
npm install

# Start the Vite development server
npm run dev
```
The frontend will run on `http://localhost:5173`.

## 🏆 Hackathon Notes
- **Civic AI Guardrails:** The LLM is strictly constrained from hallucinating evacuation routes.
- **Historical Overlays:** Features map overlays of the 2022 Pakistan Floods and 2005 Earthquake to highlight systemic vulnerabilities.
- **National Broadcast System:** Government dashboard includes mock Twilio SMS triggers for critical disaster zones.
