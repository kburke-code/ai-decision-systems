import streamlit as st

st.title("Decision Matrix Copilot (Demo Mode)")

decision = st.text_input("What decision are you making?")
options = st.text_area("List your options (comma separated)")

if st.button("Evaluate Decision"):

    if decision.strip() == "" or options.strip() == "":
        st.warning("Please complete all fields.")
    else:
        # Fake AI output for demo
        st.write(f"Decision: {decision}")
        st.write("Recommended Option: " + options.split(",")[0].strip())
        st.write("Reasoning: Based on scalability, cost, and ease of implementation, the first option is recommended.")
        st.write("Risks: Implementation time, staff training.")
        st.write("Trade-offs: Cost vs integration complexity.")