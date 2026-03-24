def generate_demo_response(prompt, tool):
    if tool == "Decision Copilot":
        return """
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
        return """
Summary:
The email requests an update.

Suggested Reply:
Thanks for your message. I will review and respond shortly.

Actions:
- Review request
- Prepare response
"""
    elif tool == "KPI Interpreter":
        return """
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
        return """
Strategy Memo:
Focus on market expansion and operational efficiency.

Highlights:
- Strengthen partnerships
- Invest in digital capabilities
- Monitor competitors
"""
    elif tool == "Calendar Copilot":
        return """
Calendar Insight:
You have 3 overlapping meetings. Consider rescheduling.

Suggestions:
- Move non-critical meeting to afternoon
- Block focus time
"""
    else:
        return "Demo response will appear here."


def plan_tasks(goal):
    goal_lower = goal.lower()

    scores = {
        "KPI Interpreter": 0,
        "Research Copilot": 0,
        "Strategy Memo": 0,
        "Decision Copilot": 0,
        "Inbox Copilot": 0,
        "Calendar Copilot": 0,
    }

    if any(word in goal_lower for word in ["kpi", "performance", "metrics"]):
        scores["KPI Interpreter"] += 2

    if any(word in goal_lower for word in ["market", "research", "analysis"]):
        scores["Research Copilot"] += 2

    if any(word in goal_lower for word in ["strategy", "growth", "plan"]):
        scores["Strategy Memo"] += 2

    if any(word in goal_lower for word in ["decide", "decision", "choose"]):
        scores["Decision Copilot"] += 2

    if any(word in goal_lower for word in ["email", "inbox"]):
        scores["Inbox Copilot"] += 2

    if any(word in goal_lower for word in ["calendar", "meeting", "schedule"]):
        scores["Calendar Copilot"] += 2

    if all(score == 0 for score in scores.values()):
        scores["Research Copilot"] = 1
        scores["Strategy Memo"] = 1

    sorted_tools = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return [tool for tool, score in sorted_tools if score > 0][:3]


def explain_plan(goal, tasks):
    goal_lower = goal.lower()
    reasons = []

    if any(word in goal_lower for word in ["board", "executive", "leadership"]):
        reasons.append("Detected executive/board-level context")

    if any(word in goal_lower for word in ["decide", "decision", "choose"]):
        reasons.append("Decision-making intent identified")

    if any(word in goal_lower for word in ["growth", "strategy", "plan"]):
        reasons.append("Strategic planning requirement detected")

    if any(word in goal_lower for word in ["email", "inbox"]):
        reasons.append("Communication/inbox management identified")

    if any(word in goal_lower for word in ["kpi", "performance", "metrics"]):
        reasons.append("Performance analysis required")

    if any(word in goal_lower for word in ["calendar", "meeting", "schedule"]):
        reasons.append("Calendar optimisation required")

    if not reasons:
        reasons.append("General business analysis requested")

    return reasons


def calculate_confidence(goal, tasks):
    goal_lower = goal.lower()
    score = 0

    if any(word in goal_lower for word in ["board", "executive", "leadership"]):
        score += 30

    if any(word in goal_lower for word in ["decide", "decision", "choose"]):
        score += 25

    if any(word in goal_lower for word in ["strategy", "growth", "plan"]):
        score += 20

    if any(word in goal_lower for word in ["email", "inbox"]):
        score += 15

    if any(word in goal_lower for word in ["kpi", "performance", "metrics"]):
        score += 20

    if any(word in goal_lower for word in ["calendar", "meeting", "schedule"]):
        score += 15

    score += len(tasks) * 5
    return min(score, 100)


def refine_plan(goal, tasks):
    goal_lower = goal.lower()
    refined_tasks = tasks.copy()

    if any(word in goal_lower for word in ["strategy", "growth", "expand"]):
        if "Research Copilot" not in refined_tasks:
            refined_tasks.append("Research Copilot")

    if any(word in goal_lower for word in ["decide", "decision", "choose"]):
        if "Strategy Memo" not in refined_tasks:
            refined_tasks.append("Strategy Memo")

    if any(word in goal_lower for word in ["board", "executive", "leadership"]):
        for tool in ["KPI Interpreter", "Research Copilot", "Strategy Memo"]:
            if tool not in refined_tasks:
                refined_tasks.append(tool)

    return refined_tasks[:5]


def run_agent(goal, session_state):
    initial_tasks = plan_tasks(goal)
    tasks = refine_plan(goal, initial_tasks)

    outputs = []
    for task in tasks:
        response = generate_demo_response(goal, task)
        outputs.append(f"### {task}\n{response}")

    reasoning = explain_plan(goal, tasks)
    confidence = calculate_confidence(goal, tasks)

    final_output = f"""
## Executive Summary

### Planned Tasks
{chr(10).join([f"- {t}" for t in tasks])}

### Confidence
{confidence}%

### Reasoning
{chr(10).join([f"- {r}" for r in reasoning])}

---

## Detailed Output

{chr(10).join(outputs)}

---

## Recommended Actions
- Prioritise highest impact initiatives
- Align stakeholders on next steps
- Execute with clear ownership and timelines
"""

    session_state.memory.append({
        "goal": goal,
        "tasks": tasks,
        "output": final_output,
    })

    return tasks, final_output