import os

from pyrogram import Client
from modconfig import Config
from peewee_aio.manager import Manager


class Bot(Client):
    def __init__(self, env=None):
        env = env or os.environ.get("ENV", "develop")
        self.cfg = Config(f"{__name__}.config.{env}")
        self.ENV = env
        self.db = Manager(self.cfg.PEEWEE_CONNECTION)
        self.web_list = {
            "RUS": ["https://www.kinopoisk.ru","https://rezka.ag","https://go3.tv/ru/"],
            "ENG": ["https://www.plex.tv","https://www.justwatch.com","https://www.yidio.com","https://go3.tv/en/"],
            "EST": ["https://go3.tv","https://viaplay.ee","https://cinemaclub.eu"],
        }
        super().__init__(
            self.cfg.TELEGRAM_BOT_NAME,
            bot_token=self.cfg.PYROGRAM_BOT_TOKEN,
            api_id=self.cfg.TELEGRAM_API_ID,
            api_hash=self.cfg.TELEGRAM_API_HASH,
            plugins=dict(root="Botapp/handlers")
        )


bot = Bot()
