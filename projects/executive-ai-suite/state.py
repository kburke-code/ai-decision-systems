import streamlit as st


def init_state():
    if "memory" not in st.session_state:
        st.session_state.memory = []

    if "last_agent_result" not in st.session_state:
        st.session_state.last_agent_result = None