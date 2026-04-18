from ara_sdk import App, run_cli, sandbox

app = App(
    "Ara Inbox Zero",
    project_name="ara-inbox-zero",
    description="Triage email, draft replies in your voice, flag what's urgent, summarize long threads.",
)


@app.subagent(
    id="inbox-zero",
    instructions="""You are an inbox triage agent running on the user's AI computer.
Flow:
1. User forwards, pastes, or connects a mailbox of emails.
2. Categorize each: urgent (needs user now), actionable (can be auto-drafted), FYI (summarize), noise (archive silently).
3. For actionable: hand off to reply-drafter with context.
4. For FYI: produce a one-line summary per thread.
5. For urgent: surface subject, sender, and a TL;DR of what's at stake.
6. Never miss a professor, recruiter, or VC email — use heuristics to upweight those.
Keep it tight — the user wants inbox zero, not inbox novella.""",
    handoff_to=["reply-drafter"],
    sandbox=sandbox(),
    channels={"api": True},
)
def inbox_zero(event=None):
    """Triage email, summarize threads, flag urgent."""


@app.subagent(
    id="reply-drafter",
    instructions="""You draft email replies on behalf of the user.
Match the tone of the thread. Keep it natural — no corporate speak.
Always present the draft for approval. If the user gives a one-line direction
like "say yes" or "decline politely", expand it into a proper email.
Never send without explicit approval.""",
    sandbox=sandbox(),
)
def reply_drafter(event=None):
    """Draft context-aware email replies."""


@app.local_entrypoint()
def local(input_payload):
    return {"ok": True, "app": "ara-inbox-zero", "input": input_payload}


if __name__ == "__main__":
    run_cli(app)
