# Agent Company

This repository contains a minimal skeleton for an AI‑driven company. The code is
written entirely in Python and includes the following modules:

- `agent_company/agent.py` – a basic `AIWorker` class that wraps OpenAI's API.
- `agent_company/mcp.py` – an example "MCP" server that coordinates a single
  agent and forwards its output to Discord.
- `agent_company/discord_client.py` – utilities for sending messages to a
  Discord channel via a bot.
- `agent_company/emailer.py` – a helper for sending emails via SMTP.
- `agent_company/forms.py` – a stub for creating Google Forms.

The implementation focuses on demonstrating how these components interact.
すべてのチャット履歴は Discord のチャンネルにのみ残し、データベースには保存しません。
Bot アカウントは一つだけ使用し、送信されるメッセージの先頭にエージェント名が付与されます。
Environment 変数で Discord や OpenAI、SMTP などの設定を行います。

Run the MCP example with:

```bash
python -m agent_company.mcp
```

This will invoke the agent using the `AGENT_PROMPT` environment variable and
send the result to the configured Discord channel.

エージェントから特定ユーザーへの DM を送る場合は `MCP.assign_task()` を利用してください。
