import hikari
import lightbulb
import datetime
from hikari.permissions import Permissions

purge_plugin = lightbulb.Plugin("purge", "delete messages")
purge_plugin = lightbulb.Plugin("say", "send message from bot to a specific channel")
purge_plugin.add_checks(
    lightbulb.checks.has_guild_permissions(hikari.Permissions.MANAGE_MESSAGES),
    lightbulb.checks.bot_has_guild_permissions(hikari.Permissions.MANAGE_MESSAGES),
    lightbulb.guild_only,

)

DELETE_MESSAGES = Permissions.MANAGE_MESSAGES






@purge_plugin.command()
@lightbulb.option(
    "user",
    "select user to delete his messages",
    type=hikari.Member,
    default=None,
    required=False,
)
@lightbulb.option(
    "count", "count of messages you want to delete", type=int, required=True
)
@lightbulb.app_command_permissions(DELETE_MESSAGES, dm_enabled=False)
@lightbulb.command("purge", "delete messages", pass_options=True)
@lightbulb.implements(lightbulb.SlashCommand)
async def purge(
    ctx: lightbulb.Context, count: int, user: hikari.Member, auto_defer=True
):
    channel = ctx.channel_id
    bulk_delete_limit = datetime.datetime.now(
        datetime.timezone.utc
    ) - datetime.timedelta(days=14)
    if user is not None  :
        iterator = (
            ctx.bot.rest.fetch_messages(channel)
            .filter(lambda message: message.author.id == user.id)
            .limit(count)
            .take_while(lambda message: message.created_at > bulk_delete_limit)
        )
    else :
        iterator = (
            ctx.bot.rest.fetch_messages(channel)
            .limit(count)
            .take_while(lambda message: message.created_at > bulk_delete_limit)
        )

    await ctx.respond(f"**deleting  messages**", delete_after=5)
    if iterator:
        async for messages in iterator.chunk(100):
            await ctx.bot.rest.delete_messages(channel, messages)
        await ctx.respond(f"**Messages has been deleted successfully**", delete_after=5)
    else:
        await ctx.respond(f"Could not find any messages ")


def load(bot):
    bot.add_plugin(purge_plugin)


def unload(bot):
    bot.remove_plugin(purge_plugin)
