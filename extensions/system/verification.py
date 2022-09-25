import hikari
import lightbulb
from hikari.permissions import Permissions
from database.models import User, VerificationRoom
from hikari.events import MemberCreateEvent
from secrets import token_hex
from tortoise import run_async
import base64
from utils.const import VERIFICATION_ROOM_ID,UNVERIFIED_ROLE_ID,VERIFIED_ROLE_ID

verfication_plugin = lightbulb.Plugin("verfication")


def flag_game_generator(user_name: str) -> str:
    code = token_hex(16)
    flag = user_name + "_" + "flag{" + code + "}"
    return flag


def encrypt_flag(flag: str) -> str:
    flag_bytes = flag.encode("ascii")
    base64_bytes = base64.b64encode(flag_bytes)
    encoded_flag = base64_bytes.decode("ascii")
    return encoded_flag


@verfication_plugin.listener(MemberCreateEvent)
async def put_in_verification_room(event):
    print(event.user)
    discord_user = event.member
    await discord_user.add_role(role=UNVERIFIED_ROLE_ID)
    user = User(
        discord_id=discord_user.id,
        username=discord_user.username,
        created_at=discord_user.created_at,
        avatar_url=discord_user.avatar_url,
        is_bot=discord_user.is_bot,
    )

    if await User.exists(discord_id=user.discord_id):
        searched_user = await User.get(discord_id=user.discord_id)
        if await VerificationRoom.exists(user=searched_user):
            room =await VerificationRoom.get(user=searched_user)
            flag = room.verification_flag
        else :
            flag = flag_game_generator(user.username)
            await VerificationRoom(
                user=user,
                verification_flag=flag,
            ).save()
        encrypted_flag = encrypt_flag(flag)

    else:
        await user.save()

        # put in verfication room
        flag = flag_game_generator(user.username)
        print(flag)
        await VerificationRoom(
            user=user,
            verification_flag=flag,
        ).save()

        # generate encoded flag
        encrypted_flag = encrypt_flag(flag)

    await verfication_plugin.app.rest.create_message(
        VERIFICATION_ROOM_ID,
        "Hello! "
        + discord_user.mention
        + " decrypt this message in order to verify your self:\n```"
        + encrypted_flag
        + "``` \n put the flag as parameter in ``/verify some_text{flag}``",
        user_mentions=[user.discord_id],
    )

@verfication_plugin.command
@lightbulb.option(
    "flag",
    "put here the verification flag",
    type=str,
    required=True,
)
@lightbulb.add_checks(lightbulb.has_roles(UNVERIFIED_ROLE_ID))
@lightbulb.command("verify", "verify your self", pass_options=True)
@lightbulb.implements(lightbulb.SlashCommand)
async def verify(ctx:lightbulb.Context,flag:str):
    discord_user = ctx.member
    if ctx.channel_id != VERIFICATION_ROOM_ID:
        return
    
    user = await User.get(discord_id=discord_user.id)
    
    room = await VerificationRoom.get(user=user)
    correct_flag = room.verification_flag

    if(flag == correct_flag):
        await ctx.respond("Win Win !!!",delete_after=5)
        await discord_user.add_role(role=VERIFIED_ROLE_ID)
        await discord_user.remove_role(role=UNVERIFIED_ROLE_ID)
    else:
        await ctx.respond("nop! try again",delete_after=5)
    
    

def load(bot):
    bot.add_plugin(verfication_plugin)


def unload(bot):
    bot.remove_plugin(verfication_plugin)
