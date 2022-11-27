import os
import discord
from keep_alive import keep_alivel

class client(discord.Client):
  async def on_ready(self):
    print(f"Logged on as {self.user}!")

  async def on_message(self, message):
    print(f"Message from {message.author}: {message.content}")

intents = discord.Intents.default()
intents.message_content = True

client = client(intents=intents)

keep_alive()
client.run(os.getenv("TOKEN"))