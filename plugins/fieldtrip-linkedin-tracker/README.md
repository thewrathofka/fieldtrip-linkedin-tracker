# fieldtrip-linkedin-tracker

Webinar-lead LinkedIn tracker for Fieldtrip. Everything lives on one shared Notion page, "Webinar Leads LinkedIn Tracking" (inBeat workspace):

- **Lead lists** at the top: Name of Webinar, Name of Campaign, and the attached CSVs (raw export + HeyReach-ready).
- **Webinar Leads**: one row per person, with `Users` saying whose LinkedIn reaches out to them.
- **Run log**: one row per run. The newest one tells the next run where to pick up.

## Using it

```
/fieldtrip-linkedin-tracker             # normal run
/fieldtrip-linkedin-tracker add more    # add a new lead list first, then a normal run
```

A run reads the page, adds anyone new from the lead lists to the database, then checks your inbox for conversations with people on **any** lead list. It ticks `Connected?` / `Replied?`, sets the dates, @mentions you on new replies, and writes a Run log row.

**First run:** it asks who you are, checks that your LinkedIn is connected, and adds you to `Users`. If there's no lead list on the page yet, it asks you to add one.

**`LinkedIn enriched successfully?`** is Yes when the person is in the HeyReach-ready CSV (so they have a LinkedIn URL), No when they're only in the raw export.

## Safety

- **Read-only on LinkedIn, enforced by code.** `hooks/linkedin_guard.py` runs before every LinkedIn MCP call and refuses anything that isn't one of: `get_inbox`, `get_conversation`, `search_conversations`, `get_person_profile`, `get_my_profile`, `get_session_status`, `close_session`. `send_message`, `connect_with_person`, searches and everything else are blocked.
- The guard matches any MCP tool with "linkedin" in its name, so while this plugin is installed it also keeps other LinkedIn MCP servers read-only.
- Conversations with people who aren't on a lead list are never opened.
- On any LinkedIn CAPTCHA, checkpoint or login problem, it stops and hands off.
