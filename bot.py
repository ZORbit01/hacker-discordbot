import os

import hikari
import lightbulb

from utils.const import GUILDS, INTENTS, TOKEN, PREFIX
from lightbulb.ext import tasks
import aiohttp
import concurrent.futures
import miru
from hikari.permissions import Permissions

bot = lightbulb.BotApp(
    TOKEN,
    default_enabled_guilds=GUILDS,
    prefix=PREFIX,
)

miru.load(bot)
tasks.load(bot)


@bot.listen()
async def on_starting(event: hikari.StartingEvent) -> None:
    """when bot start"""
    bot.d.aio_session = aiohttp.ClientSession()
    bot.d.process_pool = concurrent.futures.ProcessPoolExecutor()


@bot.listen()
async def on_stopping(event: hikari.StoppingEvent) -> None:
    """trigger when bot shutdown"""
    await bot.d.aio_session.close()
    bot.d.process_pool.shutdown(wait=True)


bot.load_extensions_from("./extensions/", must_exist=True, recursive=True)


@bot.listen(lightbulb.CommandErrorEvent)
async def on_error(event):
    if isinstance(event.exception, lightbulb.MissingRequiredPermission):
        await event.context.respond(
            "Unable to excute this command, maybe you don't have permissions",
            reply=True,
            delete_after=5,
        )
        return True
    if isinstance(event.exception, lightbulb.NotEnoughArguments):
        await event.context.respond(
            "Error please check command arguments", reply=True, delete_after=5
        )
        return True
    if isinstance(event.exception, lightbulb.CommandInvocationError):
        await event.context.respond(
            "Command invocation error", reply=True, delete_after=5
        )
        raise event.exception

        # return True


bot.run()
