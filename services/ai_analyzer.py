from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def analyze_with_ai(data, sector):

    prompt = f"""
    Analyze the Indian {sector} sector.

    Give:
    - Market Trends
    - Opportunities
    - Risks
    - Future Outlook

    Data:
    {data}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text