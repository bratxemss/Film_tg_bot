import peewee as pw
from peewee_aio.model import AIOModel

from Botapp import bot


@bot.db.register
class Customer(AIOModel):
    telegram_id = pw.CharField(unique=True)
    liked_film = pw.CharField(null=True)
    favorite_genre = pw.CharField(null=True)

    def __repr__(self):
        return f"<User: {self.telegram_id}>"
