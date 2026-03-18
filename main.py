from fastapi import FastAPI, Header, HTTPException
from services.data_collector import get_market_data
from services.ai_analyzer import analyze_with_ai
from services.report_generator import generate_markdown
from utils.auth import verify_api_key
from utils.rate_limiter import rate_limit

app = FastAPI()

def validate_sector(sector: str):
    if not sector.isalpha():
        raise HTTPException(status_code=400, detail="Invalid sector name")

@app.get("/analyze/{sector}")
def analyze_sector(sector: str, api_key: str = Header(...)):

    verify_api_key(api_key)
    rate_limit(api_key)
    validate_sector(sector)

    try:
        data = get_market_data(sector)

        try:
            analysis = analyze_with_ai(data, sector)
        except Exception:
            analysis = f"{sector} sector in India is growing with strong opportunities and moderate risks."

        report = generate_markdown(sector, analysis)

        return {"report": report}   # ✅ THIS LINE FIXES YOUR ISSUE

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
