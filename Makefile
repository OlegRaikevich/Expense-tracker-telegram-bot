start: # Activate the virtual environment and start the application locally
	. venv/telegram-bot/bin/activate && pip install -r requirements.txt
	python main_bot.py

install: # Install requirements in virtual environment
	. venv/telegram-bot/bin/activate && pip install -r requirements.txt

init-db: # Initialize the database
	python -c 'from database import init_db; init_db()'

start-logging: # Start application with logging
	. venv/telegram-bot/bin/activate && nohup python main_bot.py > bot.log 2>&1 &

stop: # Stop the running application
	pkill -f main_bot.py || echo "Bot is not running."

lint: # Check code quality using Flake8
	. venv/telegram-bot/bin/activate && flake8 --exclude=venv .

update-deps: # Update all dependencies to the latest versions
	. venv/telegram-bot/bin/activate && pip install --upgrade -r requirements.txt
