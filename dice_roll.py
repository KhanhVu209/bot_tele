import random
from telegram import Update

async def roll(update: Update, context) -> None:
    # Tạo một số ngẫu nhiên từ 1 đến 100
    random_number = random.randint(1, 100)
    await update.message.reply_text(f'You rolled: {random_number}')
