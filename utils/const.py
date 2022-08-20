import os
from hikari import Intents
from dotenv import load_dotenv

TOKEN = os.getenv("DISCORD_TOKEN")

PREFIX = [
    "!",
]

# INTENTS = (
#     Intents.GUILDS
#     | Intents.GUILD_MEMBERS
#     | Intents.GUILD_MESSAGES
#     | Intents.GUILD_VOICE_STATES
#     | Intents.MESSAGE_CONTENT
# )
INTENTS = Intents.ALL
GUILDS = ("1010072179968323684",)


GLOBAL_COLOR = 0x00FFFF


VERIFIED_ROLE_ID = 1010103979369300059
