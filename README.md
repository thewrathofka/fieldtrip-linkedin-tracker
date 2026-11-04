# fieldtrip-linkedin-tracker (Claude Code marketplace)

A one-plugin Claude Code marketplace for Fieldtrip: the **`/fieldtrip-linkedin-tracker`** webinar-lead LinkedIn tracker.

It does two things:

1. **Import a webinar.** Takes a registrant export (Riverside CSV), splits it into attended and no show, finds missing LinkedIn URLs with the ColdIQ connector, writes HeyReach-ready CSVs (`[Webinar] attended.csv`, `[Webinar] no show.csv`), attaches them to the shared Notion page, and adds every lead to the shared Notion database.
2. **Reconcile your inbox.** Reads your LinkedIn inbox (read-only), opens only threads with people on the lead list, and marks who connected and who replied. When someone replies, it @mentions you on their row.

It never sends anything on LinkedIn. People send connection requests and messages themselves (or through HeyReach).

## Install (each person, once)

In an interactive `claude` terminal:

```
/plugin marketplace add thewrathofka/fieldtrip-linkedin-tracker
/plugin install fieldtrip-linkedin-tracker@fieldtrip-linkedin-tracker
```

Restart Claude Code (or reload plugins) so the bundled `linkedin` MCP server starts. Run it with `/fieldtrip-linkedin-tracker`.

### What each person needs

- Access to the inBeat Notion workspace (the "Webinar Leads LinkedIn Tracking" page).
- Their own LinkedIn login for the bundled LinkedIn MCP.
- The ColdIQ connector, for import runs.
- `uv` / `uvx` and `python3` installed.

## Layout

```
fieldtrip-linkedin-tracker/                         ← marketplace repo
├── .claude-plugin/marketplace.json
└── plugins/
    └── fieldtrip-linkedin-tracker/                 ← the plugin
        ├── .claude-plugin/plugin.json
        ├── .mcp.json                               ← LinkedIn MCP (reads only)
        ├── hooks/hooks.json                        ← registers the read-only guard
        ├── hooks/linkedin_guard.py                 ← blocks every non-read LinkedIn tool
        ├── commands/fieldtrip-linkedin-tracker.md
        ├── README.md
        └── skills/fieldtrip-linkedin-tracker/SKILL.md
```

See [`plugins/fieldtrip-linkedin-tracker/README.md`](plugins/fieldtrip-linkedin-tracker/README.md) for details.
