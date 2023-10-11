import os
from datetime import datetime
from aiogram import Bot, Dispatcher, types, executor


TOKEN = '6470407156:AAGOGzqAycRKjDsYefM-7sgL30ijQwbiEKA'

CHAT_ID = '-1001937475306'

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot=bot)

async def send_feedback(data):
    if len(data) >= 1:
        if data['created_at'] and data['name'] and data['phone'] and data['comment']:
            msg = f"<b>Новый запрос на обратную связь!!!</b> \n\n" \
                  f"Имя: <b>{data['name']}</b> \n" \
                  f"Телефон: <b>{data['phone']}</b> \n" \
                  f"Заказы: <b>{data['order']}</b> \n" \
                  f"Стоимость заказа: <b>{data['price']}</b> \n" \
                  f"Что вас интересует?: <b>{data['comment']}</b> \n" \
                  f"Начало заказа: <b>{data['start_of_order']}</b> \n" \
                  f"Окончание заказа: <b>{data['end_of_order']} </b> \n" \
                  f"Создан в: <b>{data['created_at']}</b> \n"
            await bot.send_message(CHAT_ID, msg)
            return True
        return False
