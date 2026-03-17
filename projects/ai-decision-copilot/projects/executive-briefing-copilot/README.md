$projects = @(
"projects\ai-decision-copilot",
"projects\board-meeting-copilot",
"projects\executive-briefing-copilot",
"projects\executive-research-copilot"
)

foreach ($proj in $projects) {
    Copy-Item "C:\path\to\demo_template.py" "$proj\app.py" -Force
}