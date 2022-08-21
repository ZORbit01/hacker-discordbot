from tortoise import Tortoise
import asyncio
import asyncpg
from database.config import TORTOISE_ORM


async def init():
    # Here we create a SQLite DB using file "db.sqlite3"
    #  also specify the app name of "models"
    #  which contain models from "app.models"
    await Tortoise.init(config=TORTOISE_ORM)
    await Tortoise.generate_schemas()


from tortoise import run_async


run_async(init())
