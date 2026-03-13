import streamlit as st

st.set_page_config(page_title="AI Decision Copilot", layout="wide")

st.title("AI Decision Copilot Prototype")
st.write("Structured decision support system.")

decision_context = st.text_area("Describe your decision problem:", height=100)

st.subheader("Define Criteria")
criteria_input = st.text_area("Enter criteria separated by commas:", "Impact, Cost, Risk")
criteria = [c.strip() for c in criteria_input.split(",")]

weights = {}
st.subheader("Assign Weight to Each Criterion (1-5)")
for c in criteria:
    weights[c] = st.slider(c + " weight", 1, 5, 3)

st.subheader("Enter Options")
num_options = st.number_input(
    "Number of options:",
    min_value=1,
    max_value=10,
    value=2,
    step=1
)

options = {}

for i in range(1, num_options + 1):
    option_name = st.text_input("Option " + str(i) + " name", "Option " + str(i))
    if option_name:
        options[option_name] = {}
        for c in criteria:
            options[option_name][c] = st.slider(option_name + " - " + c + " score", 1, 5, 3)

def get_weighted_score(option_scores, weights):
    total = 0
    for criterion in option_scores:
        total += option_scores[criterion] * weights[criterion]
    return total

if st.button("Generate Recommendation"):
    if not decision_context:
        st.warning("Please enter a decision context.")
    elif not options:
        st.warning("Please enter at least one option.")
    else:
        results = {}
        for option in options:
            results[option] = get_weighted_score(options[option], weights)

        max_score = max(results.values())
        min_score = min(results.values())

        if max_score != 0:
            confidence = round(((max_score - min_score) / max_score) * 100, 2)
        else:
            confidence = 0

        st.subheader("Recommendation Output")
        import pandas as pd

results_df = pd.DataFrame(
    sorted(results.items(), key=lambda x: x[1], reverse=True),
    columns=["Option", "Score"]
)

st.subheader("Ranked Results")
st.dataframe(results_df, use_container_width=True)
st.json(results)
st.success("Confidence Score: " + str(confidence) + "%")
top_option = results_df.iloc[0]["Option"]

st.subheader("AI Recommendation Summary")
st.write(
    f"Based on the weighted criteria, **{top_option}** performs strongest "
    f"against your defined priorities. The confidence score of {confidence}% "
    f"reflects the separation between the top and lowest scoring options."
)
