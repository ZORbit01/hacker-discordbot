import hikari
import lightbulb
from hikari import Embed
from hikari.permissions import Permissions
from utils.const import GLOBAL_COLOR

say_plugin = lightbulb.Plugin("say", "send message from bot to a specific channel")
say_plugin.add_checks(
    lightbulb.checks.has_guild_permissions(hikari.Permissions.MANAGE_MESSAGES),
    lightbulb.checks.bot_has_guild_permissions(hikari.Permissions.MANAGE_MESSAGES),
    lightbulb.guild_only,

)

MANAGE_MESSAGES = Permissions.MANAGE_CHANNELS



@say_plugin.command()
@lightbulb.option("title", "message title", str, required=True)
@lightbulb.option("message", "text message to be sent", str, required=True)
@lightbulb.option("image_url", "image to be sent", str, required=False, default=None)
@lightbulb.option("channel", "channel where message to be sent", hikari.TextableChannel)
@lightbulb.app_command_permissions(MANAGE_MESSAGES, dm_enabled=False)
@lightbulb.command("say", "say message to channel", auto_defer=True, pass_options=True)
@lightbulb.implements(lightbulb.SlashCommand)
async def say(
    ctx: lightbulb.Context,
    title: str,
    message: str,
    image_url: str,
    channel: hikari.channels.GuildTextChannel,
):
    embed = Embed(title=title, description=message, color=GLOBAL_COLOR)
    if image_url is not None:
        embed.set_image(image_url)
    await say_plugin.app.rest.create_message(channel, embed=embed)
    await ctx.respond("message sent successfully", flags=hikari.MessageFlag.EPHEMERAL)


def load(bot):
    bot.add_plugin(say_plugin)


def unload(bot):
    bot.remove_plugin(say_plugin)
