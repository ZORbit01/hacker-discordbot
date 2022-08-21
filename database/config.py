from database.local_conf import (
    host,
    database,
    port,
    password,
    user,
)

TORTOISE_ORM = {
    "connections": {
        # Dict format for connection
        "default": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "host": host,
                "port": port,
                "user": user,
                "password": password,
                "database": database,
            },
        },
        # Using a DB_URL string
        "default": f"postgres://{user}:{password}@{host}:{port}/{database}",
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
