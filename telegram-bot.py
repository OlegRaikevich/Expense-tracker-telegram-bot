import logging
import os
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.constants import ParseMode
from telegram.ext import Application, ContextTypes, CommandHandler, filters, CallbackContext, MessageHandler, CallbackQueryHandler



bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
# bot = Bot(token=bot_token)

logger = logging.getLogger(__name__)

# Menu text
MENU = "<b>Expanse tracker</b>\n\nWhat you would like to do?"

# Button labels
BUTTONS = {
   'RECORD_EXPENSE':'Record expenses',
   'SHOW_WEEK':'Show expenses per week',
   'SHOW_MONTH':'Show expenses per month',
   'SHOW_AVERAGE':'Show average expenses amount per day'

}

# Inline keyboard markup
MENU_MARKUP = InlineKeyboardMarkup([
    [InlineKeyboardButton(BUTTONS['RECORD_EXPENSE'], callback_data='record')],
    [InlineKeyboardButton(BUTTONS['SHOW_WEEK'], callback_data='show_week')],
    [InlineKeyboardButton(BUTTONS['SHOW_MONTH'], callback_data='show_month')],
    [InlineKeyboardButton(BUTTONS['SHOW_AVERAGE'], callback_data='show_average')]
])

# Start command: Displays the main menu
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text="Hello! Welcome to the Expense Tracker Bot.",
        reply_markup=MENU_MARKUP,
        parse_mode=ParseMode.HTML
    )

# Menu command: Re-displays the menu
async def menu(update: Update, context: CallbackContext) -> None:
    """
    Sends the inline keyboard menu to the user.
    """
    await update.message.reply_text(
        MENU,
        parse_mode=ParseMode.HTML,
        reply_markup=MENU_MARKUP
    )

# Handler for inline button presses
async def button_tap(update: Update, context: CallbackContext) -> None:
    """
    Handles inline button presses from the menu.
    """
    data = update.callback_query.data

    if data == 'record':
        await update.callback_query.message.reply_text(
            "Please enter the amount of your expense:"
        )
        # Here you can set a state to expect the user to input an expense amount
        # You could set a state in the context.user_data for later use
        context.user_data['awaiting_expense'] = True

    elif data == 'show_week':
        await update.callback_query.message.reply_text("Showing expenses for the week...")

    elif data == 'show_month':
        await update.callback_query.message.reply_text("Showing expenses for the month...")

    elif data == 'show_average':
        await update.callback_query.message.reply_text("Showing average daily expenses...")

    await update.callback_query.answer()

# Function to handle user input (expenses)
async def handle_expense(update: Update, context: CallbackContext) -> None:
    """
    Handles the user input after they select "Record expense".
    """
    if context.user_data.get('awaiting_expense'):
        try:
            # Get the user's expense input
            expense = float(update.message.text)
            # For now, we just reply with the recorded expense
            await update.message.reply_text(f"Recorded expense: {expense} units")

            # Clear the 'awaiting_expense' state
            context.user_data['awaiting_expense'] = False

            # Here you would eventually store the data in the database
            # For example: `save_expense_to_db(user_id, expense, datetime.now())`

        except ValueError:
            await update.message.reply_text("Please enter a valid number.")

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

# Error handling
async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.error(msg="Exception while handling update:", exc_info=context.error)

def main() -> None:
    # Check if the bot token is set
    if not bot_token:
        logger.error("TELEGRAM_BOT_TOKEN is not set!")
        return

    # Create an Application instance
    application = Application.builder().token(bot_token).build()

    # Register command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("menu", menu))
    application.add_handler(MessageHandler(filters.COMMAND, unknown))
    application.add_handler(CallbackQueryHandler(button_tap))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_expense))

    # Register error handler
    application.add_error_handler(error_handler)

    # Start the bot with run_polling
    logger.info("Starting bot polling...")
    application.run_polling()

if __name__ == '__main__':
    main()