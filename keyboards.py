from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# Text menu
MENU = "<b>Expense Tracker</b>\n\nWhat would you like to do?"

# Menu buttons
BUTTONS = {
    'RECORD_EXPENSE': 'Record expenses',
    'SHOW_WEEK': 'Show expenses per week',
    'SHOW_MONTH': 'Show expenses per month',
    'SHOW_AVERAGE': 'Show average expenses per day'
}

# Markup menu
MENU_MARKUP = InlineKeyboardMarkup([
    [InlineKeyboardButton(BUTTONS['RECORD_EXPENSE'], callback_data='record')],
    [InlineKeyboardButton(BUTTONS['SHOW_WEEK'], callback_data='show_week')],
    [InlineKeyboardButton(BUTTONS['SHOW_MONTH'], callback_data='show_month')],
    [InlineKeyboardButton(BUTTONS['SHOW_AVERAGE'], callback_data='show_average')]
])


# Error handler
async def error_handler(update: object, context: object) -> None:
    print(f"Eror: {context.error}")
