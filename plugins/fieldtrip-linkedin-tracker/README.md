# fieldtrip-linkedin-tracker

Webinar-lead LinkedIn tracker for Fieldtrip. One shared Notion page and database ("Webinar Leads LinkedIn Tracking" in the inBeat workspace); each lead belongs to one user (`Users`: Kat, Mirella).

## Using it

```
/fieldtrip-linkedin-tracker                                  # reconcile my inbox
/fieldtrip-linkedin-tracker import ~/Downloads/registrants.csv  # import a webinar
```

**Import** asks for the webinar name and date, the campaign names (pre-event, attended, no show), and whose LinkedIn will reach out. It asks before spending ColdIQ credits. Output: `[Webinar] attended.csv` and `[Webinar] no show.csv` in HeyReach's import format, attached at the top of the Notion page, plus a row per lead in the database.

**Reconcile** reads your inbox overview, opens only threads with people on your lead list, ticks `Connected?` / `Replied?`, and @mentions you on the row when someone replies.

## Safety

- **Read-only on LinkedIn, enforced by code.** `hooks/linkedin_guard.py` runs before every LinkedIn MCP call and refuses anything that isn't one of: `get_inbox`, `get_conversation`, `search_conversations`, `get_person_profile`, `get_my_profile`, `get_session_status`, `close_session`. `send_message`, `connect_with_person`, searches and everything else are blocked.
- The guard matches any MCP tool with "linkedin" in its name, so while this plugin is installed it also keeps other LinkedIn MCP servers read-only.
- Conversations with people who aren't on the lead list are never opened.
- ColdIQ lookups cost credits, so it always asks first.
- On any LinkedIn CAPTCHA, checkpoint or login problem, it stops and hands off.

## Adding a teammate

1. Add their first name as an option in the `Users` property.
2. Add their Notion email → option line under "Users" in `skills/fieldtrip-linkedin-tracker/SKILL.md`.
