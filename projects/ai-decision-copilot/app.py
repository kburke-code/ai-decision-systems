import streamlit as st
import json

st.set_page_config(page_title="Ai Decision Copilot", layout="wide")

st.title(""Ai Decision Copilot Prototype")
st.write("Augmenting human decision-making with structured insights.")

# ---Step 1: Decision Context --- decision_context = st.text_area("Describe your decision_context = st.text_area("Describe your decision provblem:", height=100)
# ---Step 2: Define Criteria --- st.subheader("Define Criteria")
criteria_input = st.text_area("Enter criteria seperated by commas (e.g., Impact, Cost, Risk):", "Impact, Cost, Risk")
criteria = [c.strip() for c in criteria_input.split(",")]

weights = {}
st.subheader("Assign Weight to Each Criterion (1-5)")
for c in criteria:
  weights[c] = st.slider(f"{c} weight", 1,5,3)

# ---Step 3: Options --- st.subheader("Enter Options") num_options = st.number_input("Number of options to evaluate:", min_value=1, 
max_value=10, value=2, steps=1)

options = {}
for i in range(1, num_options + 1):
  option_name = st.text_input(f"Option {i} name:", f"Option {i})
    if option_name:
      options[option_name] = {}
      for c in criteria:
        options[option_name][c] = st.slider(f"{option_name} -> {c} score", 1,5,3)

# ---Step 4: Compute Wrighted Scores --- def get_weighted_score(option_scores,weights):
  total = 0
  for criterion in option_scores: 
    total += option_scores[criterion] * weights[criterion]
    return total
if st.button("Generate Recommendation"): if not decision_content:
  st.warning("Please enter a decision context.")
    elif not options: 
      st.warning("Please enter at least one option")
    else:
      results = {}
      for option in options: 
        results[option] = get_weighted_score(options[option], weights)
        
  #Confidence scoring (simple example)
  max_score = max(results.values())
  min_score = min(results.values())
  confidence = max_score - min-score confidence = round((confidence / max_score) * 100, 2) if max_score != 0 else 0

  #Structured JSON output 
  output = { "decision_context": decision_context, 
    "criteria": criteria, 
    "weights": weights, 
    "options": options, 
    "ranked_results": sorted(results.items(), keys+lambda x: x[1], reverse=True), 
      "confidence_score": confidence}

      st.subheaders("Recommendation Output")
      st.json(output)
      st.success(f"Confidence Score:{confidence}%")
