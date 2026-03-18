🚀 Trade Opportunities API

A FastAPI-based backend service that analyzes Indian market sectors and generates structured trade opportunity reports using AI.

📌 Overview

This project provides an API that accepts a sector name (e.g., technology, pharmaceuticals) and returns a detailed market analysis report.

It combines:

Data collection from web sources

AI-based analysis

Clean markdown report generation

⚙️ Features

✅ FastAPI backend with clean architecture

✅ AI-powered analysis using Gemini API

✅ Fallback mechanism for API failures

✅ Input validation for secure requests

✅ API key authentication

✅ Rate limiting to prevent abuse

✅ Structured and readable output

✅ Deployed on Render

🔗 Live API

👉 https://trade-api-4emb.onrender.com/docs

🧪 API Endpoint
GET /analyze/{sector}
Example:
/analyze/technology
Headers:
api-key: mysecretkey
📊 Sample Response
{
  "report": "📊 Market Analysis Report: Technology\n\nOverview:\nThe Indian technology sector..."
}
🏗️ Project Structure
trade_api/
│
├── main.py
├── services/
│   ├── data_collector.py
│   ├── ai_analyzer.py
│   ├── report_generator.py
│
├── utils/
│   ├── auth.py
│   ├── rate_limiter.py
│
├── requirements.txt
├── .env
🔐 Environment Variables

Create a .env file:

GEMINI_API_KEY=your_api_key

⚠️ .env is excluded using .gitignore for security.

🛠️ Installation & Run Locally
git clone https://github.com/yourusername/trade-api.git
cd trade-api

pip install -r requirements.txt

uvicorn main:app --reload
🚀 Deployment

This project is deployed using Render.

Steps:

Push code to GitHub

Connect repo to Render

Add environment variables

Set start command:

uvicorn main:app --host 0.0.0.0 --port 10000
⚠️ Notes

Gemini API has free-tier limits

A fallback mechanism ensures API response even if AI fails

💡 Future Improvements

Real-time news scraping

Caching for faster responses

Advanced prompt engineering

UI dashboard for visualization

👨‍💻 Author

Mahesh Dugyani
