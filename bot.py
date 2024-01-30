from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from greetings import hello, bye, reply_to_vu_quoc_khanh
from dice_roll import roll  # Thêm import cho module roll

# Thay token bot vào đây
app = ApplicationBuilder().token('6149777169:AAE0CzsEBq8yBMgF1-SgrTeXmEfJSLU3C5s').build()

# Đăng ký các handler cho các lệnh
app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("bye", bye))
app.add_handler(CommandHandler("vu_quoc_khanh", reply_to_vu_quoc_khanh))  # Đăng ký lệnh mới
app.add_handler(CommandHandler("roll", roll))

# Khởi chạy bot với phương thức polling
app.run_polling()
