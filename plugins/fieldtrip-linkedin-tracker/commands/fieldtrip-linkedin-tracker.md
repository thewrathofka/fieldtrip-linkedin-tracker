---
description: Fieldtrip webinar-lead LinkedIn tracker. No argument = reconcile your LinkedIn inbox (read-only) against the shared Notion database. A CSV path or "import" = turn a webinar registrant export into HeyReach-ready attended / no show CSVs and add the leads to Notion.
---

Run the workflow in `${CLAUDE_PLUGIN_ROOT}/skills/fieldtrip-linkedin-tracker/SKILL.md`.

Read the whole SKILL.md before doing anything else in this run. It has the hard rules, fixed Notion IDs, database schema, and the steps for both parts.

Pass whatever the user typed after the command as `$ARGUMENTS`: empty = reconcile (Part B); a CSV path or "import" = import a webinar (Part A).

Resolve who is running it (Notion identity + LinkedIn `get_my_profile`) every run; the plugin is shared, so never assume a specific person.

Hard rule: this command never sends anything on LinkedIn, and only opens inbox threads with people on the lead list.
