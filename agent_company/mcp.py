"""Minimal MCP server example."""
import os
from .agent import AIWorker
from .discord_client import send_discord_message, send_discord_dm


class MCP:
    def __init__(self):
        self.agent = AIWorker(role=os.getenv("AGENT_ROLE", "Default agent"))

    def handle_task(self, prompt: str):
        response = self.agent.run(prompt)
        send_discord_message(f"[{self.agent.role}] {response}")
        return response

    def assign_task(self, user_id: int, task: str):
        send_discord_dm(f"[{self.agent.role}] {task}", user_id)


def main():
    prompt = os.getenv("AGENT_PROMPT", "Say hello")
    mcp = MCP()
    result = mcp.handle_task(prompt)
    print(result)


if __name__ == "__main__":
    main()
