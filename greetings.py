from telegram import Update

# Hàm xử lý lệnh /hello
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

# Hàm xử lý lệnh /bye
async def bye(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Bye {update.effective_user.first_name}')

# Hàm xử lý lệnh /vu_quoc_khanh
async def reply_to_vu_quoc_khanh(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Trả lời cho VŨ QUỐC KHÁNH")
