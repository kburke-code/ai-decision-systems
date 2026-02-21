# Simple Decision Copilot Prototype

def get_weighted_score(option_scores,
weights):
  total = 0
  for criterion in option_score:
    total += option_scores[criterion] *
weights[criterion]
  return total

def main():
  print("AI Decision Copilot Prototype")
  print("-----------------------------")

  criteria = ["Impact", "Cost", "Risk"]
  weights = {}

print("\nAssign weights (1-5 importance 
scale):
  for c in criteria:
    weights[c] = int(input(f"{c} weight:"))
    options = {}
    num_options = int(input("\nHow many options to evaluate? "))

  for i in range(num_options):
    name = input(f"\nOption {i+1} name:")
    options[name] = {}

  for c in criteria: 
      score = int(input(f"{c} score
      (1-5): "))

  print("\nCalculating results...\n")

  results = {}
  for option in options:
    results [option] = 
get_weighted_score(options[option], weights)

  ranked = sorted(results.items(),
key=lambda x: x[1], reverseTrue)

  print("Recommended Ranking:")
  for r in ranked: 
    print(f"{r[0]} -> Score: {[1]}")

If__name__=="__main__":main()
    
