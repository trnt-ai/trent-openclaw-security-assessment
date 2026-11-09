---
name: trent-openclaw-security
description: "Deprecated: this skill no longer works. Trent now secures OpenClaw through its main security engineer at trent.ai. Install nothing; read the notice."
version: 2.0.0
homepage: https://trent.ai
user-invocable: true
tags:
  - trentai
  - trent
  - trentclaw
  - security
  - deprecated
---

# Trent OpenClaw Security Assessment — deprecated

This skill is retired. Its API endpoints have been removed and its API keys
revoked, so every phase of the audit now fails. Version 2.0.0 exists only to
tell you that; it runs nothing and sends nothing.

## Instructions for the agent

Do not run any script from this skill. When the user asks for a Trent audit of
their OpenClaw setup, tell them the skill is deprecated and show them the
"What to use instead" section below, then stop.

## What to use instead

Trent still secures OpenClaw deployments. The checks this skill ran now live in
Trent's main security engineer, which reads your agent's code and configuration
from a repository instead of from a local skill.

1. **Scan your OpenClaw agent repository.** Sign in at https://app.trent.ai
   (or https://app.eu.trent.ai in the EU), connect the GitHub repository that
   holds your agent, its skills and its configuration, and run a scan. Trent
   detects OpenClaw deployments and applies its OpenClaw-specific checks.
2. **Ask Trent from your coding agent.** Add Trent's hosted MCP server and use
   the `security_advisor` tool to review an OpenClaw config, skill or change:

   ```bash
   claude mcp add --transport http trent-us https://mcp.trent.ai/mcp     # outside the EU
   claude mcp add --transport http trent-eu https://mcp.eu.trent.ai/mcp  # in the EU
   ```

3. **Remove this skill** so it stops appearing in your sessions:

   ```bash
   clawhub uninstall trentclaw
   ```

Questions: https://trent.ai
