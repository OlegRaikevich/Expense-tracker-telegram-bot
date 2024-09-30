import sqlite3
from datetime import datetime, timedelta


# Initialization database
def init_db():
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS expenses (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER NOT NULL,
                        amount REAL NOT NULL,
                        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                      )''')
    conn.commit()
    return conn


# Save expenses
def save_expense(user_id, amount):
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses (user_id, amount) VALUES (?, ?)",
                   (user_id, amount))
    conn.commit()


# Getting expenses for period
def get_expenses_for_period(user_id, period):
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    if period == 'week':
        start_date = datetime.now() - timedelta(days=7)
    elif period == 'month':
        start_date = datetime.now() - timedelta(days=30)

    cursor.execute("SELECT SUM(amount) FROM expenses WHERE user_id = ? AND timestamp >= ?",
                   (user_id, start_date))
    result = cursor.fetchone()[0]
    return result if result else 0


def get_average_expense(user_id):
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT DATE(timestamp)), SUM(amount) FROM expenses WHERE user_id = ?",
                   (user_id,))

    days, total = cursor.fetchone()
    return total / days if days else 0
