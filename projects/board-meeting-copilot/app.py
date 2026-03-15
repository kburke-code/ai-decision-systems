import streamlit as st

st.title("Board Meeting Copilot")

# Input raw notes
notes = st.text_area("Enter raw meeting notes or bullet points:")

# Button to generate summary
if st.button("Generate Board Summary"):
    if notes.strip() == "":
        st.warning("Please enter some notes first.")
    else:
        summary = f"""
Board Summary:

Key Decisions:
- Placeholder for decisions from notes

Action Items:
- Placeholder for action items

Discussion Highlights:
- Placeholder for important discussion points
"""
        st.write(summary)
        