#!/usr/bin/env python3
"""Block every LinkedIn MCP tool except the read-only ones.

Claude Code runs this before any tool whose name matches the hook's matcher.
The full tool name depends on how the server was installed, for example
  mcp__plugin_fieldtrip-linkedin-tracker_linkedin__send_message
  mcp__linkedin__send_message
so we look only at the part after the last "__" and allow a short list of reads.
Anything else exits with code 2, which tells Claude Code to refuse the call.
"""
import json
import sys

ALLOWED = {
    "get_inbox",
    "get_conversation",
    "search_conversations",
    "get_person_profile",
    "get_my_profile",
    "get_session_status",
    "close_session",
}

try:
    tool_name = json.load(sys.stdin).get("tool_name", "")
except Exception:
    print("linkedin guard: could not read the tool call, blocking to be safe.", file=sys.stderr)
    sys.exit(2)

# Only judge LinkedIn MCP tools; leave everything else alone.
if not tool_name.startswith("mcp__") or "linkedin" not in tool_name.lower():
    sys.exit(0)

action = tool_name.rsplit("__", 1)[-1]
if action in ALLOWED:
    sys.exit(0)

print(
    f"Blocked '{action}': fieldtrip-linkedin-tracker is read-only on LinkedIn. "
    "Sending, connecting, searching and other actions are done by a person, not by Claude.",
    file=sys.stderr,
)
sys.exit(2)
