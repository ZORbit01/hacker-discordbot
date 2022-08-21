import os

TORTOISE_ORM = {
    "connections": {
        # Dict format for connection
        "default": os.getenv("DATABASE_URL")
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
