import os
from dotenv import load_dotenv

if os.path.exists("config.env"):
    load_dotenv("config.env")
else:
    load_dotenv()


def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


class Config(object):
    API_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "tg_bot")
    DATABASE_URL = os.environ.get("DATABASE_URL", None)
    OWNER_ID = int(os.environ.get("OWNER_ID"))
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "0"))
    WEB_SERVER = is_enabled(os.environ.get("WEB_SERVER", "False"), False)
    THUMBNAILS = list(map(str, os.environ.get("THUMBNAILS", "").split()))

    # Constants
    CANCEL_DATA = {}
    PROCESS_DATA = {}


class Script(object):
    START_MESSAGE = (
        " {mention}\n\nSend any link or set of links in a txt file to download them."
    )
    DEV_MESSAGE = """ðŸ‘‹ Hey there, I'm ð„ŸâƒðŸ¬ðŸ‡µÊ€ÉªÊá´€ð„ŸâƒðŸ¬ â€“ your go-to Telegram bot developer!

ðŸ¤– Love having bots that do the heavy lifting for you? That's my jam! I'm all about crafting super cool and custom Telegram bots that make your life a breeze.

âœ¨ **What I Do**

- **Bot Magic:** From automating tasks to interactive games, I create bots that do it all. Seriously, ask me anything!
- **Tailored to You:** Your bot, your rules. I'll whip up a bot that's as unique as you are.
- **Chill Vibes:** I keep your data super safe, so you can relax and enjoy the bot party.
- **Always Improving:** Telegram evolves, and my bots grow with it. I'm here to keep things fresh and fab.

Ready for your own bot buddy? Ping me on [Telegram](https://telegram.me/Reason_Someone) or check out me on [GitHub](https://github.com/The_real_xTaR). Wanna hire me? Find me on [Fiverr](https://www.fiverr.com/The_real_xTaR)!

Let's bot up and have some fun! ðŸ¤˜"""
    HELP_MESSAGE = os.environ.get("HELP_MESSAGE", "Help message")
    PROGRESS_MESSAGE = """**â•”â•â•â•â•â° Uploading â±â•â•â
â•‘â•­â”âž£
â•‘â”£âª¼  Progress:-  {percentage}%
â•‘â”£ 
â•‘â”£âª¼ {progress}
â•‘â”£
â•‘â”£âª¼ã€Š{finished} of {total}ã€‹
â•‘â”£ 
â•‘â”£âª¼ Speed:- {speed}/s
â•‘â”£ 
â•‘â”£âª¼ ETA:- {eta} 
â•‘â•°â”âž£
â•šâ•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â**"""
    NEW_USER_MESSAGE = """#NewUser

ðŸ†” User ID: `{user_id}`
ðŸ‘¤ User: {mention}
"""
    DOWNLOADING = """ðŸ“¥ á´…á´á´¡É´ÊŸá´á´€á´…ÉªÉ´É¢ ðŸ“¥ :- {start_index}/{end_index}

ðŸ“ Name Â» {link_no}) Â» {name}

Original Index: {orginal_start_index}/{orginal_end_index}

[ð„ŸâƒðŸ¬ðŸ‡µÊ€ÉªÊá´€ð„ŸâƒðŸ¬](https://t.me/Reason_Someone)"""

    DEFAULT_CAPTION = """[ðŸ“] File_ID : {file_index}

ð–¤“ ð“Éªá´›ÊŸá´‡  : {file_name}

ðŸ—ƒ ð’ð¢ð³ðž : {file_size}

ðŸ“š Bá´€á´›á´„Êœ Ná´€á´á´‡ : {batch_name}

Dá´á´¡É´ÊŸá´á´€á´…á´‡á´… BÊ : [ð„ŸâƒðŸ¬ðŸ‡µÊ€ÉªÊá´€ð„ŸâƒðŸ¬](https://t.me/ReaSon_SomeOne_Bot)"""


    CAPTION_CB = """**Set Caption

âž¢ Available Variables ðŸ‘‡**

â”ŒðŸŽ´ ððšð¦ðž : `{file_name}`
â”œðŸ—ƒ ð’ð¢ð³ðž : `{file_size}`
â”œâš™ï¸ ð„ð±ð­ðžð§ð¬ð¢ð¨ð§ : `{file_extension}`
â”œðŸ§­ ðƒð®ð«ðšð­ð¢ð¨ð§ : `{file_duration}`
â”œðŸ–‡ ð‹ð¢ð§ð¤ : `{file_url}`
â”œðŸ”¢ ðˆð§ððžð± : `{file_index}`
â”œðŸ—³ ððšð­ðœð¡ ððšð¦ðž : `{batch_name}`

==============================

âž¢ Current:
`{current_caption}`

==============================

âž¢ **Default:**
`{default_caption}`

âž¢ **Status:** {status}"""
