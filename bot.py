import sqlite3, requests
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler

TOKEN = "8767090768:AAExsDNaR98Ap_Aq9TmvOu_hStEq5JFD75k"
API_KEY = "167d8ae06c970abb07868848853f1692dc734c06"

async def start(u, c):
    kb = [[InlineKeyboardButton("📺 مشاهدة فيديو", callback_data='w')], [InlineKeyboardButton("💰 رصيدي", callback_data='b')]]
    await u.message.reply_text("🔥 بوت أرينة فيديو جاهز!", reply_markup=InlineKeyboardMarkup(kb))

async def h(u, c):
    q = u.callback_query
    await q.answer()
    if q.data == 'w':
        r = requests.get(f"https://shrinkme.io/api?api={API_KEY}&url=https://t.me/share/url?url={q.from_user.id}")
        link = r.json().get('shortenedUrl', "https://shrinkme.io/")
        await q.message.reply_text(f"🔗 تخطى الرابط لربح النقاط:\n{link}")
    elif q.data == 'b':
        await q.message.reply_text(f"💰 سيتم عرض رصيدك هنا فور اكتمال التخطي.")

if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(h))
    app.run_polling()
