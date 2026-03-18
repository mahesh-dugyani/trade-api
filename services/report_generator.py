def generate_markdown(sector, analysis):

    clean = analysis.replace("\\n", "\n")

    return f"""📊 Market Analysis Report: {sector.title()}

Overview:
{clean}

Opportunities:
- Growth potential
- Investment opportunities

Risks:
- Competition
- Regulations

Future Outlook:
Strong growth expected.
"""
