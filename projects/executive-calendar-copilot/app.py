import streamlit as st

st.title("Executive Calendar Copilot (Demo Mode)")

events = st.text_area("Paste your upcoming meetings or events")

if st.button("Generate Schedule Summary"):

    if events.strip() == "":
        st.warning("Please enter events first.")
    else:
        # Demo output
        st.write("High-priority meetings: Board Review, Client Pitch")
        st.write("Time conflicts detected: None")
        st.write("Suggested prep: Review quarterly report, prepare slides for client pitch")
        st.write("Opportunities: Combine internal check-ins into one block to save time")
