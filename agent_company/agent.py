import os
import openai


class AIWorker:
    """Base class for AI agents."""

    def __init__(self, role: str):
        self.role = role
        self.model = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def run(self, prompt: str) -> str:
        """Run the agent with the given prompt."""
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "system", "content": self.role},
                      {"role": "user", "content": prompt}],
        )
        return response.choices[0].message["content"].strip()
