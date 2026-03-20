import streamlit as st

# Page config
st.set_page_config(page_title="Executive AI Suite", layout="wide")

# Title
st.title("Executive AI Copilot Suite")

# Sidebar menu
app_mode = st.sidebar.selectbox(
    "Choose a tool",
    ["Inbox Copilot", "KPI Interpreter", "Decision Copilot"]
)

# -------------------------
# INBOX COPILOT
# -------------------------
if app_mode == "Inbox Copilot":
    st.header("Inbox Copilot")

    email = st.text_area("Paste email or message:")

    if st.button("Summarise Email"):
        if email:
            st.subheader("Summary")
            st.write(email[:100] + "...")

            st.subheader("Suggested Response")
            st.write("Thanks for your message. I will review and respond shortly.")

            st.subheader("Action Items")
            st.write("- Review request")
            st.write("- Prepare reply")
        else:
            st.warning("Please enter email content")

# -------------------------
# KPI INTERPRETER
# -------------------------
elif app_mode == "KPI Interpreter":
    st.header("KPI Interpreter")

    revenue = st.number_input("Revenue (€)", value=100000)
    growth = st.slider("Growth %", -50, 100, 10)

    if st.button("Analyse KPIs"):
        if growth > 20:
            insight = "Strong growth — consider scaling operations."
        elif growth > 0:
            insight = "Moderate growth — maintain current strategy."
        else:
            insight = "Declining performance — review cost structure."

        st.subheader("Results")
        st.write("Revenue: €" + str(revenue))
        st.write("Growth: " + str(growth) + "%")
        st.write("Insight: " + insight)

# -------------------------
# DECISION COPILOT
# -------------------------
elif app_mode == "Decision Copilot":
    st.header("Decision Copilot")

    notes = st.text_area("Enter meeting notes or bullet points:")

    if st.button("Generate Decision Summary"):
        if notes:
            st.subheader("Key Decisions")
            st.write("- Decision 1: ... based on notes")
            st.write("- Decision 2: ... based on notes")

            st.subheader("Recommended Actions")
            st.write("- Action 1: ...")
            st.write("- Action 2: ...")
        else:
            st.warning("Please enter some notes")
            