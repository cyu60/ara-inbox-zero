# Ara Inbox Zero

Single-agent example from the [Ara Hackathon Tour 2026](https://github.com/cyu60/ara-ai-computer) — triage email, draft replies in your voice, flag urgent, and summarize long threads, all running on the [Ara](https://ara.so) agentic operating system.

**Links:** [Ara docs](https://docs.ara.so/introduction) · [Ara Hackathon Tour](https://github.com/cyu60/ara-ai-computer) · [DayDreamers](https://daydreamers.live)

Part of the **Aragrams** — reference projects built by [DayDreamers](https://daydreamers.live) to show what's possible with agent-first development.

## What it does

Forward, paste, or describe emails in natural language. The agent:

- Triages incoming mail into urgent / reply-needed / FYI / archive buckets
- Flags time-sensitive or high-stakes threads so nothing important slips
- Summarizes long back-and-forth threads into a few tight bullets
- Hands off to a reply-drafter that writes responses in your voice, ready to paste
- Keeps a running state of what's handled vs. still open on the sandbox filesystem

No rules to configure, no filters to maintain — talk to the agent like an assistant who actually reads your inbox.

## Architecture

```
Browser (index.html)
   ↓
/api/run (Vercel serverless function)
   ↓
Ara API (api.ara.so) — Bearer ARA_RUNTIME_KEY
   ↓
inbox-zero subagent running in a sandboxed Python runtime
```

## Local dev

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install ara-sdk
export ARA_ACCESS_TOKEN=<your_token>

python3 app.py setup                           # registers the app → returns APP_ID
python3 app.py deploy --on-existing update     # pushes the agent definition
python3 app.py run --workflow inbox-zero --message "Triage this thread: <paste email>"
```

## Deploy

This repo is wired to Vercel. On push to `main`:

1. Vercel builds the static frontend + `api/run.js` edge function.
2. The function proxies `/api/run` calls to `https://api.ara.so/v1/apps/<APP_ID>/run` using `ARA_RUNTIME_KEY`.
3. The Ara runtime spins up the `inbox-zero` sandbox on demand.

## License

MIT
