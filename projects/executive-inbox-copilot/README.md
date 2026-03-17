import streamlit as st
from openai import OpenAI

client = OpenAI()

st.title("Executive Calendar Copilot")

calendar_text = st.text_area("Paste your calendar events here (copy from Outlook/Google Calendar)")

if st.button("Optimize Schedule"):
    prompt = f"""
You are an executive assistant.
Review the following schedule and suggest:
1. Prioritized agenda
2. Conflicts
3. Recommendations to free up time

Calendar:
{calendar_text}
"""
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )
    st.subheader("Optimized Schedule")
    st.write(response.output_text)