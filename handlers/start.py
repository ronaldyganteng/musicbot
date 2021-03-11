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

Dirancang khusus untuk menemanimu bergalau ria, berdendang, hingga berdangdut di voice call groups.
Bot ini sering patah patah dikit kalau di vcg, jadi gausa protes.

Cara pakai bot ini ya tinggal masukin aja ke grupmu, jangan lupa masukin userbot asistennya juga.
Tapi izin dulu lah ajg ke owner bot ini biar berkah sekalian diajarin cara pakenya :))

*DISCLAIMER: BOT INI TIDAK MEMERLUKAN JABATAN ADMIN, JADI TINGGAL PAKE AJA.
HATI - HATI JIKA BOT INI MENYALAHGUNAKAN JABATAN ADMIN!

Berikut dibawah ini adalah cara pakainya.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "CARA MENGGUNAKANNYA", url="https://telegra.ph/Cara-Menggunakan-BoI-Music-Bot-boimusic-bot-03-09"
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
        "Hai, mau nyari lagu ya?",
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
