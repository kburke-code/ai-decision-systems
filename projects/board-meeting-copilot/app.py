import streamlit as st
from openai import OpenAI

client = OpenAI()

st.title("Decision Matrix Copilot")

decision = st.text_input("What decision are you trying to make?")

options = st.text_area("List the options you are considering")

criteria = st.text_area("What criteria matter most? (cost, speed, risk, impact etc)")

if st.button("Generate Decision Matrix"):

    prompt = f"""
Create a decision matrix for the following:

Decision:
{decision}

Options:
{options}

Criteria:
{criteria}

Return:
- A comparison of options
- Pros and cons
- A recommended choice with reasoning
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    st.subheader("Decision Analysis")
    st.write(response.output_text)