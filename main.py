from fastapi import FastAPI, Header, HTTPException
from services.data_collector import get_market_data
from services.ai_analyzer import analyze_with_ai
from services.report_generator import generate_markdown
from utils.auth import verify_api_key
from utils.rate_limiter import rate_limit
from fastapi.responses import PlainTextResponse



app = FastAPI()

#  Input validation
def validate_sector(sector: str):
    if not sector.isalpha():
        raise HTTPException(status_code=400, detail="Invalid sector name")


@app.get("/")
def home():
    return {"message": "Trade Opportunities API Running 🚀"}


@app.get("/analyze/{sector}")
def analyze_sector(sector: str, api_key: str = Header(...)):

    # 🔐 Step 1: Security
    verify_api_key(api_key)
    rate_limit(api_key)

    # ✅ Step 2: Validate input
    validate_sector(sector)

    try:
        #  Step 3: Get market data
        data = get_market_data(sector)

        #  Step 4: AI analysis
        analysis = analyze_with_ai(data, sector)

        #  Step 5: Generate report
        report = generate_markdown(sector, analysis)

        

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))