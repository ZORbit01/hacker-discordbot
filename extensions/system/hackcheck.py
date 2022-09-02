import hikari
import lightbulb
from utils.const import VERIFIED_ROLE_ID,HACK_CHECK_TOKEN
from hackcheck import Hackcheck
from itertools import islice

def chunks(data, SIZE=10):
    it = iter(data)
    for i in range(0, len(data), SIZE):
        yield {k:data[k] for k in islice(it, SIZE)}

hc = Hackcheck(HACK_CHECK_TOKEN)
hackcheck_plugin = lightbulb.Plugin("hackcheck",'check breached_data')
@hackcheck_plugin.command
@lightbulb.option(
    "email",
    type=str,
    required=False,
    description="search for email"
)
@lightbulb.option(
    "username",
    type=str,
    required=False,
    description="search for username"
)
@lightbulb.option(
    "password",
    type=str,
    required=False,
    description="search for password"
)
@lightbulb.add_checks(lightbulb.has_roles(VERIFIED_ROLE_ID))
@lightbulb.command("hackcheck", "check in hackcheck.com breached data", pass_options=True,auto_defer=True)
@lightbulb.implements(lightbulb.SlashCommand)
async def hackcheck(ctx:lightbulb.Context,email:str,username:str,password:str):
    if email :
        embd = hikari.Embed(
            title="RESULTS OF : {}".format(email),
            color=ctx.author.accent_colour,
        )
        result = hc.lookup_email(email)
        i=0
        for r in result:
            if i==50 :
                break
            try :
                embd.add_field(name="username",value=r.username or "Na")
                embd.add_field(name="password",value=r.password or "Na")
                embd.add_field(name="ip",value=r.ip or "Na")
                embd.add_field(name="phone",value=r.phone or "Na")
                embd.add_field(name=str(i),value="=========")
            except :
                pass
            i+=1
        await ctx.respond(embed=embd)
        return 
    if username :
        embd = hikari.Embed(
            title="RESULTS OF : {}".format(username),
            color=ctx.author.accent_colour,
        )
        result = hc.lookup_username(username)
        i=0
        for r in result:
            if i==50 :
                break
            try :
                embd.add_field(name="email",value=r.email or "Na")
                embd.add_field(name="password",value=r.password or "Na")
                embd.add_field(name="ip",value=r.ip or "Na")
                embd.add_field(name="phone",value=r.phone or "Na")
                embd.add_field(name="source", value=r.source or "Na",inline=True)
                embd.add_field(name=str(i),value="===============")
            except :
                pass
            i+=1
        await ctx.respond(embed=embd)
        return 
    if password :
        embd = hikari.Embed(
            title="RESULTS OF : {}".format(password),
            color=ctx.author.accent_colour,
        )
        result = hc.lookup_password(password)
        i=0
        for r in result:
            if i==50 :
                break
            try :
                embd.add_field(name="email",value=r.email or "Na")
                embd.add_field(name="username",value=r.username or "Na")
                embd.add_field(name="ip",value=r.ip or "Na")
                embd.add_field(name="phone",value=r.phone or "Na")
                embd.add_field(name="source", value=r.source or "Na",inline=True)
                embd.add_field(name=str(i),value="===============")
            except :
                pass
            i+=1
        await ctx.respond(embed=embd)
        return 
    else :
        await ctx.respond("Error habibi you need to choose a field")


def load(bot):
    bot.add_plugin(hackcheck_plugin)


def unload(bot):
    bot.remove_plugin(hackcheck_plugin)
