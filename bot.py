import logging
logging.basicConfig(level=logging.WARNING,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

import pyrogram, os

if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    app = pyrogram.Client(
        "bot",
        bot_token=os.environ.get("TOKEN","5442493323:AAG3s5FR0zCfB8yx8UuTVWf8FkzccJuzlmA"),
        api_id=int(os.environ.get("APP_ID",6534707)),
        api_hash=os.environ.get("API_HASH","4bcc61d959a9f403b2f20149cbbe627a"),
        plugins=plugins
    )
    app.run()
