import os
import asyncio
from typing import Optional

import discord


class DiscordLogger:
    """Discord チャンネルや DM にメッセージを送るラッパー."""

    def __init__(self, token: str, channel_id: int):
        self.token = token
        self.channel_id = channel_id
        self.client = discord.Client(intents=discord.Intents.default())

    async def _send(self, message: str):
        await self.client.wait_until_ready()
        channel = self.client.get_channel(self.channel_id)
        if channel:
            await channel.send(message)
        await self.client.close()

    def send_message(self, message: str):
        async def runner():
            await self._send(message)

        self.client.loop.create_task(runner())
        self.client.run(self.token)

    async def _send_dm(self, user_id: int, message: str):
        await self.client.wait_until_ready()
        user = await self.client.fetch_user(user_id)
        if user:
            await user.send(message)
        await self.client.close()

    def send_dm(self, user_id: int, message: str):
        async def runner():
            await self._send_dm(user_id, message)

        self.client.loop.create_task(runner())
        self.client.run(self.token)


def send_discord_message(message: str,
                         token: Optional[str] = None,
                         channel_id: Optional[int] = None):
    token = token or os.getenv("DISCORD_BOT_TOKEN")
    channel_id = channel_id or int(os.getenv("DISCORD_CHANNEL_ID", "0"))
    logger = DiscordLogger(token, channel_id)
    logger.send_message(message)


def send_discord_dm(message: str,
                    user_id: int,
                    token: Optional[str] = None):
    token = token or os.getenv("DISCORD_BOT_TOKEN")
    logger = DiscordLogger(token, 0)
    logger.send_dm(user_id, message)
