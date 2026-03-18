def generate_markdown(sector, analysis):

    # Clean AI text
    clean_analysis = analysis.replace("\\n", "\n")

    return f"""# 📊 Market Analysis Report: {sector.title()}

##  Overview
{clean_analysis}

##  Opportunities
- Growth potential in India
- Increasing demand
- Investment opportunities

##  Risks
- High competition
- Regulatory challenges
- Market volatility

##  Future Outlook
The {sector} sector shows promising growth in India.
"""