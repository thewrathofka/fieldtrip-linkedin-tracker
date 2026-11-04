---
description: Reads the shared Webinar Leads Notion page, then checks your LinkedIn inbox (read-only) for conversations with anyone on its lead lists. Marks who connected and replied, @mentions you on new replies, and logs the run. Never sends anything on LinkedIn.
---

Run the workflow in `${CLAUDE_PLUGIN_ROOT}/skills/fieldtrip-linkedin-tracker/SKILL.md`.

Read the whole SKILL.md before doing anything else in this run. It has the hard rules, the fixed Notion IDs, the database properties, and the steps.

Pass whatever the user typed after the command as `$ARGUMENTS`: empty = a normal run; "add more" / "add leads" / a CSV path = add a new lead list first, then a normal run.

Always read the Notion page first (lead lists, Webinar Leads, Run log), then work out who is running it. The plugin is shared, so never assume a specific person.

Hard rule: never send anything on LinkedIn, and only open inbox threads with people on the lead lists.
