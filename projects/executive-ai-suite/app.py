import streamlit as st

# ---------------------------
# CONFIGURATION
# ---------------------------
DEMO_MODE = True
st.set_page_config(page_title="Executive AI Suite", layout="wide")
st.title("Executive AI Suite")

# ---------------------------
# DEMO RESPONSE FUNCTION
# ---------------------------
def generate_demo_response(prompt, tool):
    if tool == "Decision Copilot":
        return f"""
Key Decision:
Option A is recommended.

Rationale:
- Aligns best with your criteria
- Lower risk profile
- Faster execution

Next Steps:
- Validate with stakeholders
- Execute within 2 weeks
"""
    elif tool == "Inbox Copilot":
        return f"""
Summary:
The email requests an update.

Suggested Reply:
Thanks for your message. I will review and respond shortly.

Actions:
- Review request
- Prepare response
"""
    elif tool == "KPI Interpreter":
        return f"""
Performance Insight:
Growth is positive but below target.

Observations:
- Revenue is increasing
- Growth not yet at expectations

Recommendation:
- Investigate constraints
- Adjust strategy as needed
"""
    elif tool == "Research Copilot":
        return f"""
Research Brief:
Company {prompt[:20]} is showing strong innovation in its sector.

Key Points:
- Market share growth
- Strategic partnerships
- Competitive risks
"""
    elif tool == "Strategy Memo":
        return f"""
Strategy Memo:
Focus on market expansion and operational efficiency.

Highlights:
- Strengthen partnerships
- Invest in digital capabilities
- Monitor competitors
"""
    elif tool == "Calendar Copilot":
        return f"""
Calendar Insight:
You have 3 overlapping meetings. Consider rescheduling.

Suggestions:
- Move non-critical meeting to afternoon
- Block focus time
"""
    else:
        return "Demo response will appear here."

# ---------------------------
# SIDEBAR NAVIGATION
# ---------------------------
tool = st.sidebar.selectbox(
    "Choose a tool",
    [
        "Decision Copilot",
        "Inbox Copilot",
        "KPI Interpreter",
        "Research Copilot",
        "Strategy Memo",
        "Calendar Copilot"
    ]
)

# ---------------------------
# DECISION COPILOT
# ---------------------------
if tool == "Decision Copilot":
    st.header("Decision Copilot")
    decision = st.text_input("What decision are you making?")
    options = st.text_area("Options")
    criteria = st.text_area("Criteria")
    if st.button("Generate Decision Matrix", key="decision_btn"):
        result = generate_demo_response("", "Decision Copilot")
        st.write(result)

# ---------------------------
# INBOX COPILOT
# ---------------------------
elif tool == "Inbox Copilot":
    st.header("Inbox Copilot")
    email = st.text_area("Paste email or note")
    if st.button("Generate Response", key="inbox_btn"):
        result = generate_demo_response(email, "Inbox Copilot")
        st.write(result)

# ---------------------------
# KPI INTERPRETER
# ---------------------------
elif tool == "KPI Interpreter":
    st.header("KPI Interpreter")
    revenue = st.number_input("Revenue", value=100000)
    growth = st.number_input("Growth %", value=5)
    if st.button("Interpret KPI", key="kpi_btn"):
        prompt = f"Revenue: {revenue}, Growth: {growth}%"
        result = generate_demo_response(prompt, "KPI Interpreter")
        st.write(result)

# ---------------------------
# RESEARCH COPILOT
# ---------------------------
elif tool == "Research Copilot":
    st.header("Research Copilot")
    company_name = st.text_input("Company Name")
    if st.button("Generate Research Brief", key="research_btn"):
        result = generate_demo_response(company_name, "Research Copilot")
        st.write(result)

# ---------------------------
# STRATEGY MEMO
# ---------------------------
elif tool == "Strategy Memo":
    st.header("Strategy Memo")
    topic = st.text_input("Strategy Topic")
    if st.button("Generate Memo", key="strategy_btn"):
        result = generate_demo_response(topic, "Strategy Memo")
        st.write(result)

# ---------------------------
# CALENDAR COPILOT
# ---------------------------
elif tool == "Calendar Copilot":
    st.header("Calendar Copilot")
    meetings = st.text_area("Enter your meeting schedule")
    if st.button("Optimize Calendar", key="calendar_btn"):
        result = generate_demo_response(meetings, "Calendar Copilot")
        st.write(result)