import streamlit as st


def load_styles():
    st.markdown("""
        <style>
        .card {
            padding: 1.5rem;
            border-radius: 12px;
            background-color: #1E1E1E;
            margin-bottom: 1rem;
        }

        .small-text {
            color: #888;
            font-size: 0.9rem;
        }
        </style>
    """, unsafe_allow_html=True)