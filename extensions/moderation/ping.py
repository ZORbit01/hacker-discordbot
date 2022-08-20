import hikari
import lightbulb
from hikari.permissions import Permissions

ping_plugin = lightbulb.Plugin("ping")


@ping_plugin.command
@lightbulb.command("bomb", "sweet ascension of doom !")
@lightbulb.implements(lightbulb.SlashCommand, lightbulb.PrefixCommand)
async def ping(ctx: lightbulb.Context) -> None:
    await ctx.respond("sweet ascension of doom !", flags=hikari.MessageFlag.EPHEMERAL)


def load(bot):
    bot.add_plugin(ping_plugin)


def unload(bot):
    bot.remove_plugin(ping_plugin)
