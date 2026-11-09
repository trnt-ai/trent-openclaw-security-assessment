# Trent OpenClaw Security Assessment — deprecated

**This skill is retired.** The service it talked to has been shut down, so the
audit it ran no longer works. The ClawHub listing is hidden and this repository is
archived. The last working release is tag `1.4.0`; its README, code and tests stay
in git history. Version 2.0.1 on ClawHub is a notice only: SKILL.md, LICENSE and
NOTICE, no code.

## What to use instead

Trent still secures OpenClaw deployments through its main security engineer,
which reads an agent's code and configuration from a repository.

1. **Scan your OpenClaw agent repository.** Sign in at [app.trent.ai](https://app.trent.ai)
   (or [app.eu.trent.ai](https://app.eu.trent.ai) in the EU), connect the GitHub
   repository that holds your agent, its skills and its configuration, and run a
   scan. Trent detects OpenClaw deployments and applies its OpenClaw-specific checks.
2. **Ask Trent from your coding agent.** Add Trent's hosted MCP server to Claude
   Code or Codex and use the `security_advisor` tool to review an OpenClaw config,
   skill or change:

   ```bash
   claude mcp add --transport http trent-us https://mcp.trent.ai/mcp     # outside the EU
   claude mcp add --transport http trent-eu https://mcp.eu.trent.ai/mcp  # in the EU
   ```

3. **Remove this skill** from your OpenClaw install:

   ```bash
   clawhub uninstall trentclaw
   ```

## License

Licensed under the [Apache License, Version 2.0](./LICENSE). Copyright 2025-2026 Trent AI.

## About Trent

Trent secures agentic systems across code, infrastructure, workflows, and runtime
behavior. Visit [trent.ai](https://trent.ai/?utm_source=github&utm_medium=referral&utm_campaign=trentclaw).
