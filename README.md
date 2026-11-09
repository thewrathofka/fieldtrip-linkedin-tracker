# fieldtrip-linkedin-tracker (Claude Code marketplace)

A one-plugin Claude Code marketplace for Fieldtrip: the **`/fieldtrip-linkedin-tracker`** webinar-lead LinkedIn tracker.

Each run:

1. Reads the shared Notion page **"Webinar Leads LinkedIn Tracking"** (inBeat workspace): the lead lists at the top, the Webinar Leads database, and the Run log (to see when the last run was).
2. If a lead list has only the raw export, finds LinkedIn URLs with ColdIQ (after asking, since it costs credits) and builds HeyReach-ready CSVs: `[Webinar] attended.csv` and `[Webinar] no show.csv`.
3. Adds anyone from the lead lists who isn't in the database yet, marking whether their LinkedIn was found (`LinkedIn enriched successfully?`).
4. Reads **your** LinkedIn inbox, read-only, and opens only conversations with people on those lead lists.
5. Marks who connected and who replied, copies the full conversation onto each connected lead's page (refreshed every run), @mentions you on new replies, and writes a Run log row.

It never sends anything on LinkedIn. People send connection requests and messages themselves (or through HeyReach).

## Install (each person, once)

In an interactive `claude` terminal:

```
/plugin marketplace add thewrathofka/fieldtrip-linkedin-tracker
/plugin install fieldtrip-linkedin-tracker@fieldtrip-linkedin-tracker
```

Restart Claude Code (or reload plugins) so the bundled `linkedin` MCP server starts, then run `/fieldtrip-linkedin-tracker`. On your first run it asks who you are, checks your LinkedIn is connected, and adds you to the `Users` list.

### What each person needs

- Access to the inBeat Notion workspace.
- Their own LinkedIn login for the bundled LinkedIn MCP.
- The ColdIQ connector, if they'll add lead lists that only have the raw export.
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
