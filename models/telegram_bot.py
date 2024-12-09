# from telegram import Update
# from telegram.ext import (
#     Application,
#     CommandHandler,
#     MessageHandler,
#     filters,
#     ContextTypes,
# )
#
# # Токен вашего бота
# BOT_TOKEN = "7619675110:AAH70F0DgkHSByjdarLSKP5e4AQtJaTs-Rs"
#
# # Команда /start
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text("Привет! Я бот на polling. Чем могу помочь?")
#
# # Обработка текстовых сообщений
# async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     user_message = update.message.text
#     await update.message.reply_text(f"Ты сказал: {user_message}")
#
# # Функция запуска бота
# def start_bot():
#     # Создаём приложение
#     application = Application.builder().token(BOT_TOKEN).build()
#
#     # Регистрируем обработчики
#     application.add_handler(CommandHandler("start", start))
#     application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
#
#     # Запускаем polling
#     print("Бот запущен с использованием polling!")
#     application.run_polling()
#
# if __name__ == "__main__":
#     start_bot()