from uuid import uuid4

import peewee as pw
from peewee_aio.model import AIOModel

from Botapp import bot


@bot.db.register
class Customer(AIOModel):
    telegram_id = pw.CharField(unique=True)
    user_password = pw.CharField(null=True)
    liked_film = pw.CharField(null=True)
    favorite_genre = pw.CharField(null=True)

    def __repr__(self):
        return f"<User: {self.telegram_id}>"

    @classmethod
    async def create_with_telegram_id(cls, telegram_id):
        return await cls.create(
            telegram_id=telegram_id,
            user_password=str(uuid4()),
            pc_token=str(uuid4())
        )
