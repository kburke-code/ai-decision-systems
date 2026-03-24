import streamlit as st

from agents import generate_demo_response, run_agent
from state import init_state
from styles import load_styles

# ---------------------------
# PAGE CONFIG
# ---------------------------
st.set_page_config(page_title="Executive AI Suite", layout="wide")

# ---------------------------
# INIT
# ---------------------------
init_state()
load_styles()

# ---------------------------
# SIDEBAR
# ---------------------------
st.sidebar.title("Executive AI Suite")
st.sidebar.markdown("### Tools")

tool = st.sidebar.radio(
    "Select a module:",
    [
        "Home",
        "Executive Agent",
        "Decision Copilot",
        "Research Copilot",
        "Strategy Memo",
        "Inbox Copilot",
        "KPI Interpreter",
        "Calendar Copilot",
    ],
)

st.sidebar.markdown("---")
st.sidebar.caption("Built for executive decision-making")

# ---------------------------
# HOME
# ---------------------------
if tool == "Home":
    st.title("Executive AI Suite")
    st.caption("AI-powered decision support for modern leaders")

    st.markdown("""
Welcome to your AI-powered decision system.

### What this does:
- Break down complex problems
- Generate strategy insights
- Support executive decisions
- Automate workflows

👉 Select a tool from the left to begin
""")

# ---------------------------
# EXECUTIVE AGENT
# ---------------------------
elif tool == "Executive Agent":
    st.header("Executive Agent")
    goal = st.text_area("What do you want to achieve?")

    if st.button("Run Agent", key="agent_btn"):
        if not goal.strip():
            st.warning("Please enter a goal before running the agent.")
        else:
            tasks, output = run_agent(goal, st.session_state)
            st.session_state.last_agent_result = {
                "tasks": tasks,
                "output": output,
            }

    if st.session_state.last_agent_result:
        col1, col2 = st.columns([1, 2])

        with col1:
            st.subheader("Planned Tasks")
            for t in st.session_state.last_agent_result["tasks"]:
                st.markdown(f"- {t}")

        with col2:
            st.subheader("Executive Brief")
            st.markdown(
                f'<div class="card">{st.session_state.last_agent_result["output"]}</div>',
                unsafe_allow_html=True,
            )

    if st.session_state.memory:
        st.subheader("Recent Activity")
        for item in reversed(st.session_state.memory[-3:]):
            st.markdown(
                f"""
                <div class="card">
                    <strong>Goal:</strong> {item['goal']}
                    <div class="small-text">
                        Tasks: {", ".join(item['tasks'])}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

# ---------------------------
# DECISION COPILOT
# ---------------------------
elif tool == "Decision Copilot":
    st.header("Decision Copilot")
    decision = st.text_input("What decision are you making?")
    options = st.text_area("Options")
    criteria = st.text_area("Criteria")

    if st.button("Generate Decision Matrix", key="decision_btn"):
        if not decision.strip():
            st.warning("Please describe the decision first.")
        else:
            output = generate_demo_response(decision, "Decision Copilot")
            st.write(output)

# ---------------------------
# INBOX COPILOT
# ---------------------------
elif tool == "Inbox Copilot":
    st.header("Inbox Copilot")
    email = st.text_area("Paste email or note")

    if st.button("Generate Response", key="inbox_btn"):
        if not email.strip():
            st.warning("Please paste an email or note first.")
        else:
            output = generate_demo_response(email, "Inbox Copilot")
            st.write(output)

# ---------------------------
# KPI INTERPRETER
# ---------------------------
elif tool == "KPI Interpreter":
    st.header("KPI Interpreter")
    revenue = st.number_input("Revenue", value=100000)
    growth = st.number_input("Growth %", value=5)

    if st.button("Interpret KPI", key="kpi_btn"):
        prompt = f"Revenue: {revenue}, Growth: {growth}%"
        output = generate_demo_response(prompt, "KPI Interpreter")
        st.write(output)

# ---------------------------
# RESEARCH COPILOT
# ---------------------------
elif tool == "Research Copilot":
    st.header("Research Copilot")
    company_name = st.text_input("Company Name")

    if st.button("Generate Research Brief", key="research_btn"):
        if not company_name.strip():
            st.warning("Please enter a company name.")
        else:
            output = generate_demo_response(company_name, "Research Copilot")
            st.write(output)

# ---------------------------
# STRATEGY MEMO
# ---------------------------
elif tool == "Strategy Memo":
    st.header("Strategy Memo")
    topic = st.text_input("Strategy Topic")

    if st.button("Generate Memo", key="strategy_btn"):
        if not topic.strip():
            st.warning("Please enter a strategy topic.")
        else:
            output = generate_demo_response(topic, "Strategy Memo")
            st.write(output)

# ---------------------------
# CALENDAR COPILOT
# ---------------------------
elif tool == "Calendar Copilot":
    st.header("Calendar Copilot")
    meetings = st.text_area("Enter your meeting schedule")

    if st.button("Optimize Calendar", key="calendar_btn"):
        if not meetings.strip():
            st.warning("Please enter your schedule.")
        else:
            output = generate_demo_response(meetings, "Calendar Copilot")
            st.write(output)

            def init_state():
    import streamlit as st

    if "memory" not in st.session_state:
        st.session_state.memory = []

    if "last_agent_result" not in st.session_state:
        st.session_state.last_agent_result = None