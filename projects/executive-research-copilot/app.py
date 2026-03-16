import streamlit as st
from openai import OpenAI

client = OpenAI()

st.title("Executive Research Copilot")

company = st.text_input("Enter company name")

if st.button("Generate Executive Brief"):

    if company.strip() == "":
        st.warning("Please enter a company name")

    else:

        prompt = f"""
You are a strategic advisor.

Provide a short executive briefing on {company} including:

1. Strategic overview
2. Key competitors
3. AI opportunities
4. Strategic risks

Keep it concise and suitable for a C-suite briefing.
"""

        response = client.responses.create(
            model="gpt-4.1-mini",
            input=prompt
        )

        briefing = response.output_text

        st.write(briefing)