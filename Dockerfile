# Base image
FROM python:3.12

# Set the working directory inside the container
WORKDIR /app/telegram-bot

# Copy the local files to the working directory inside the container
COPY . /app/telegram-bot

# Install the application dependecies
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "main_bot.py"]
