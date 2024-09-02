start:
	( \
		source venv/telegram-bot/bin/activate; \
		pip install -r requirements.txt; \
		python telegram_bot_main.py; \
	)
	