from pyrogram.types import InlineKeyboardButton
import config
from AnonXMusic import app

def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="➕ Create Your Group",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="⚙️ Bot Settings",
                callback_data="settings_back_helper",
            )
        ],
        [
            InlineKeyboardButton(
                text="👑 Owner",
                user_id=config.OWNER_ID,
            ),
            InlineKeyboardButton(
                text="📣 Updates Channel",
                url=config.SUPPORT_CHANNEL,
            ),
        ],
        [
            InlineKeyboardButton(
                text="💬 Support Chat",
                url=config.SUPPORT_CHAT,
            ),
        ],
        [
            InlineKeyboardButton(
                text="⭐ Source Code",
                url="https://github.com/xbitcode/music.git",
            ),
        ],
    ]
    return buttons
