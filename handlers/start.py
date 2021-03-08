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

Saya adalah bot music voice call group untuk groupchat khusus yang sudah diberi izin oleh boi.

Berikut kontak owner dan jangan lupa join ke groupchatnya ya xixixi.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚒ OWNER BOT", url="https://t.me/boi999"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "HUNTER'S", url="https://t.me/hunterspmc"
                    ),
                    InlineKeyboardButton(
                        "TEMAN ONLINE", url="https://t.me/initemanonline"
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
