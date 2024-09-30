from telegram import Update
from telegram.ext import ContextTypes
from keyboards import MENU, MENU_MARKUP
from database import save_expense, get_average_expense, get_expenses_for_period


# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hello! Weclome to the Expense Tracker Bot",
        reply_markup=MENU_MARKUP
    )


# Menu command hendler
async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        MENU,
        reply_markup=MENU_MARKUP
    )


# Buttons tap handler
async def button_tap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = update.callback_query.data

    if data == 'record':
        await update.callback_query.message.reply_text(
            "Please enter the amount of your expense:"
        )
        context.user_data['awaiting_expense'] = True

    elif data == 'show_week':
        expenses = get_expenses_for_period(update.effective_user.id, 'week')
        await update.callback_query.message.reply_text(f"Expenses for the week: {expenses}")

    elif data == 'show_month':
        expenses = get_expenses_for_period(update.effective_user.id, 'month')
        await update.callback_query.message.reply_text(f"Expenses for the month: {expenses}")

    elif data == 'show_average':
        average = get_average_expense(update.effective_user.id)
        await update.callback_query.message.reply_text(f"Average daily expense: {average}")

    await update.callback_query.answer()


# Expenses record handler
async def handle_expense(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.user_data.get('awaiting_expense'):
        try:
            expense = float(update.message.text)
            save_expense(update.effective_user.id, expense)
            await update.message.reply_text(f"Recorded expense: {expense} units")
            context.user_data['awaiting_expense'] = False
        except ValueError:
            await update.message.reply_text("Please enter a valid number.")


# Unknown command handler
async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")
