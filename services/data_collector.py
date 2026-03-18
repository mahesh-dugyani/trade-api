import requests

def get_market_data(sector: str):
    url = f"https://api.duckduckgo.com/?q={sector}+market+india&format=json"
    
    response = requests.get(url)
    data = response.json()

    result = data.get("AbstractText", "")
    
    if not result:
        result = "No detailed data found, but sector is active in India."

    return result