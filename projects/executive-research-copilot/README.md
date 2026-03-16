import streamlit as st
from openai import OpenAI

# Connect to OpenAI (uses your OPENAI_API_KEY environment variable)
client = OpenAI()

st.title("Board Meeting Copilot")
st.write("Paste your meeting notes or bullets and get a dynamic executive summary.")

# Text input for meeting notes
notes = st.text_area("Enter meeting notes here:")

# Button to generate summary
if st.button("Generate Summary"):
    if notes.strip() == "":
        st.warning("Please enter some notes first")
    else:
        # The prompt we send to OpenAI
        prompt = f"""You are an executive assistant.
Take the following raw meeting notes:

{notes}

Generate:
1. Key Decisions
2. Action Items
3. Discussion Highlights

Make it concise, board-ready, and tailored to the notes provided.
"""

        # Call OpenAI
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=prompt
        )

        # Get text output
        summary = response.output_text

        # Show in Streamlit
        st.subheader("Executive Summary")
        st.write(summary)