from tortoise.models import Model
from tortoise import fields


class User(Model):
    id = fields.IntField(pk=True)
    discord_id = fields.BigIntField(unique=True)
    username = fields.CharField(max_length=255)
    is_bot = fields.BooleanField(default=False)
    created_at = fields.DatetimeField(null=True)
    avatar_url = fields.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.pk}:{self.discord_id},{self.username},{self.is_bot},{self.created_at},{self.avatar_url}"


class Member(User):
    joined_at = fields.DatetimeField()


class VerificationRoom(Model):
    user = fields.ForeignKeyField(
        "database.User", related_name="verification_room", on_delete="CASCADE"
    )
    verification_flag = fields.CharField(max_length=255)

    class Meta:
        unique_together = ("user", "verification_flag")
