import logging
from config import bot_token
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from handlers import start, menu, button_tap, handle_expense, unknown
from database import init_db
from keyboards import error_handler

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    # Initialization data base
    conn = init_db()

    # Check if the bot token is set
    if not bot_token:
        logger.error("TELEGRAM_BOT_TOKEN is not set!")
        return

    # Create an Application instance
    application = Application.builder().token(bot_token).build()

    # Register command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("menu", menu))
    application.add_handler(CallbackQueryHandler(button_tap))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_expense))
    application.add_handler(MessageHandler(filters.COMMAND, unknown))

    # Register error handler
    application.add_error_handler(error_handler)

    # Start the bot with run_polling
    logger.info("Starting bot polling...")
    application.run_polling()

if __name__ == '__main__':
    main()