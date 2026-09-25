def parse_meeting(title: str, text: str):
    summary = f"Summary of '{title}': Reviewed Q3 engineering roadmap and aligned on autonomous agent architectures."
    decisions = [
        "Approved migration to SQLite-Vec for edge vector search.",
        "Established weekly Tuesday multi-agent sprint reviews."
    ]
    actions = [
        {"assignee": "Bilal (Erha Lead)", "task": "Deploy production vector index benchmarks", "deadline": "Friday"},
        {"assignee": "QA Team", "task": "Execute end-to-end regression tests across all 50 repos", "deadline": "Next Monday"}
    ]
    email = (
        f"Subject: Minutes & Action Items: {title}\n\n"
        "Hi Team,\n\nThank you for attending today's session. Here is our recap:\n\n"
        f"- {decisions[0]}\n- {decisions[1]}\n\n"
        "Action Items:\n"
        f"1. {actions[0]['assignee']}: {actions[0]['task']} (Due: {actions[0]['deadline']})\n"
        f"2. {actions[1]['assignee']}: {actions[1]['task']} (Due: {actions[1]['deadline']})\n\n"
        "Best,\nAI Meeting Coordinator"
    )
    return summary, decisions, actions, email
