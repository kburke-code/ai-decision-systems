import streamlit as st

st.title("Executive Briefing Copilot")

company = st.text_input("Company")
topic = st.text_input("Topic")
question = st.text_area("Executive Question")

if st.button("Generate Briefing"):

    briefing = f"""
Executive Briefing

Company: {company}
Topic: {topic}

Key considerations:
- Strategic relevance to the organisation
- Market opportunity and competitive positioning
- Operational and technology implications

Executive Question:
{question}

Recommendation:
Further analysis recommended before executive decision
"""
    
    st.write(briefing)