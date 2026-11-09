---
name: trent-openclaw-security
description: "Deprecated: this skill is retired and does nothing. Trent now secures OpenClaw through its main security engineer at trent.ai."
version: 2.0.1
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

This skill is retired. The service it talked to has been shut down, so it can no
longer run an audit. This version contains no code and performs no action.

## Instructions for the agent

When the user asks for a Trent audit of their OpenClaw setup, tell them this
skill is deprecated, show them the alternatives below, and stop. Do not attempt
to run an audit.

## What to use instead

Trent still secures OpenClaw deployments through its main security engineer,
which reads an agent's code and configuration from a repository.

1. Scan the repository that holds your OpenClaw agent, its skills and its
   configuration. Sign in at https://app.trent.ai (https://app.eu.trent.ai in
   the EU), connect the repository and run a scan.
2. Ask Trent from Claude Code or Codex through Trent's hosted MCP server. Setup
   instructions are at https://trent.ai.
3. Remove this skill from OpenClaw so it stops appearing in your sessions.

Questions: https://trent.ai
