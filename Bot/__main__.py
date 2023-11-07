import argparse
import asyncio


from Bot import bot


def argsParser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-run", required=False, action="store_true")
    parser.add_argument("-env", nargs="?", type=str, default="develop")
    parser.add_argument("-init_db", required=False, action="store_true")

    return parser


if __name__ == "__main__":
    parser = argsParser()
    namespace = parser.parse_args()

    if namespace.run:
        bot.run()

    if namespace.init_db:
        asyncio.run(bot.db.create_tables())