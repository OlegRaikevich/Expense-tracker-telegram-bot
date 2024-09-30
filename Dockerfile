# Base image
FROM python:3.12

# Set the working directory inside the container
WORKDIR /app/telegram-bot

# Copy only the requirements file first
COPY requirements.txt .

# Install the application dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the local files to the working directory inside the container
COPY . .

# Create a non-root user and switch to it
RUN useradd -m botuser
USER botuser

EXPOSE 5000

CMD ["python", "main_bot.py"]
