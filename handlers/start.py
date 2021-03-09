from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 Halo, {message.from_user.first_name}!</b>

Saya adalah bot music voice call group!
Dirancang khusus untuk groupchat yang sudah diberi izin oleh Boi.
Berikut dibawah ini adalah kontak owner bot.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚒ OWNER BOT", url="https://t.me/boiii999"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "JOIN SINI", url="https://t.me/hunterspmc"
                    ),
                    InlineKeyboardButton(
                        "JOIN SINI", url="https://t.me/initemanonline"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "CARA MEMAKAINYA", url="https://telegra.ph/Cara-Menggunakan-BoI-Music-Bot-boimusic-bot-03-09"
                    )
                ]
            ]
        )
    )


@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "Hai, mau nyari lagu apa? coba ketik.",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Ya", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "Tidak ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
