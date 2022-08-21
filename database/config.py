try :
    from database.local_conf import (
        host,
        database,
        port,
        password,
        user,
    )
except :
    pass
import os

TORTOISE_ORM = {
    "connections": {
        # Dict format for connection
        "default": os.getenv("DATABASE_URL",f"postgres://{user}:{password}@{host}:{port}/{database}"),
    },
    "apps": {
        "database": {
            "models": ["database.models", "aerich.models"],
            # If no default_connection specified, defaults to 'default'
            "default_connection": "default",
        },
    },
    "use_tz": False,
    "timezone": "UTC",
}
