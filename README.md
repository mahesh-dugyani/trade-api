# 🚀 Trade Opportunities API

A FastAPI-based backend service that analyzes Indian market sectors and generates structured trade opportunity reports using AI.

---

## 📌 Overview

The **Trade Opportunities API** is designed to provide insights into different industry sectors in India.
It accepts a sector name as input and returns a structured market analysis report including trends, opportunities, risks, and future outlook.

This project demonstrates:

* Backend API development using FastAPI
* Integration with AI (Gemini API)
* Data collection from external sources
* Clean response formatting and error handling
* Deployment using cloud platforms

---

## ⚙️ Features

* 🚀 FastAPI backend with clean architecture
* 🤖 AI-powered analysis using Gemini API
* 🔁 Fallback mechanism for API failures (quota handling)
* 🔐 API key-based authentication
* ⏱️ Rate limiting to prevent abuse
* ✅ Input validation for secure requests
* 📄 Structured and readable output
* 🌐 Deployed and publicly accessible

---

## 🔗 Live API

👉 https://trade-api-4emb.onrender.com/docs

---

## 🧪 API Endpoint

### `GET /analyze/{sector}`

#### 🔹 Example Request

```bash
GET /analyze/technology
```

#### 🔹 Headers

```bash
api-key: mysecretkey
```

---

## 📊 Sample Response

```json
{
  "report": "📊 Market Analysis Report: Technology\n\nOverview:\nThe Indian technology sector is growing rapidly..."
}
```

---

## 🏗️ Project Structure

```
trade_api/
│
├── main.py                # FastAPI entry point
│
├── services/             # Core logic
│   ├── data_collector.py # Fetch market data
│   ├── ai_analyzer.py    # AI analysis (Gemini)
│   ├── report_generator.py # Format output
│
├── utils/                # Utility modules
│   ├── auth.py           # API authentication
│   ├── rate_limiter.py   # Rate limiting logic
│
├── requirements.txt      # Dependencies
├── .env                  # Environment variables (not pushed)
├── .gitignore
```

---

## 🔐 Environment Variables

Create a `.env` file in the root directory:

```
GEMINI_API_KEY=your_api_key_here
```

⚠️ The `.env` file is excluded using `.gitignore` to keep sensitive data secure.

---

## 🛠️ Installation & Run Locally

```bash
git clone https://github.com/yourusername/trade-api.git
cd trade-api

pip install -r requirements.txt

uvicorn main:app --reload
```

Open in browser:

```
http://127.0.0.1:8000/docs
```

---

## 🚀 Deployment (Render)

This project is deployed using **Render**.

### Steps:

1. Push code to GitHub
2. Create a new Web Service on Render
3. Connect your GitHub repository
4. Add environment variable:

   * `GEMINI_API_KEY`
5. Set commands:

**Build Command**

```bash
pip install -r requirements.txt
```

**Start Command**

```bash
uvicorn main:app --host 0.0.0.0 --port 10000
```

---

## ⚠️ Error Handling

* Handles external API failures gracefully
* Implements fallback responses when AI quota is exceeded
* Prevents invalid inputs using validation
* Uses rate limiting to avoid abuse

---

## 💡 Design Approach

The system follows a modular architecture:

* **API Layer** → Handles requests
* **Service Layer** → Business logic (data + AI)
* **Utility Layer** → Security and rate limiting

This ensures scalability, maintainability, and clean separation of concerns.

---

## 🔮 Future Improvements

* 📡 Real-time news scraping (Economic Times, etc.)
* ⚡ Caching for faster responses
* 📊 Dashboard UI for visualization
* 🧠 Improved prompt engineering
* 📦 Docker containerization

---

## 👨‍💻 Author

**Mahesh Dugyani**

---

## 📢 Notes

* Gemini API free tier has usage limits
* Fallback logic ensures API reliability even when limits are exceeded
* This project focuses on demonstrating backend + AI integration

---

# ⭐ If you like this project, give it a star!
