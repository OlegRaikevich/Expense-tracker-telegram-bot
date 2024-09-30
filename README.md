# 🐳 Expense Tracker Telegram Bot

A Telegram bot for tracking your expenses, built using Python, Docker, SQLite, and Kubernetes. This bot allows users to record expenses, view expenses over time, and calculate daily averages.

## 📑 Table of Contents
1. [Overview](#overview)
2. [Architecture](#architecture)
3. [Getting Started](#getting-started)
4. [Makefile Explanation](#makefile-explanation)
5. [Technologies Used](#technologies-used)

## 🌟 Overview

The Expense Tracker Telegram Bot provides a simple way for users to track their expenses through a Telegram interface. Key features include:
- Recording expenses
- Viewing expenses for the week and month
- Calculating average daily expenses
- Storing data locally using SQLite

The bot is containerized using Docker for easy deployment and management. The infrastructure can be managed with Kubernetes for scaling and orchestration.

## 🏗️ Architecture

The architecture of the bot consists of the following components:

- **Telegram Bot API**: The bot interacts with users through Telegram's API.
- **SQLite Database**: Used to store expense data locally.
- **Python**: The main programming language used to build the bot, utilizing libraries such as `python-telegram-bot` for handling Telegram interactions.
- **Docker**: Containerizes the application to ensure consistent and isolated execution across different environments.
- **GitLab CI/CD**: Automates the build, testing, and deployment processes, ensuring consistent delivery of new features and updates to the bot.


### Architecture Diagram
                 +---------------+
                 |   Telegram     |
                 |      User      |
                 +-------+-------+
                         |
                         v
                 +-------+-------+
                 |  Telegram Bot  |
                 |     (Python)   |
                 +-------+-------+
                         |
                         v
                 +-------+-------+
                 |    SQLite     |
                 |   Database    |
                 +-------+-------+
                         |
                         v
                     Docker
                         |
                         v
                 +-------+-------+
                 |    GitLab CI/CD|
                 +-------+-------+



## 🚀 Getting Started

### Prerequisites

- Python 3.12
- Docker
- A Telegram bot token (get it from [BotFather](https://core.telegram.org/bots#botfather))

### Local Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/expense-tracker-bot.git
   cd expense-tracker-bot

2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment:**
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the bot:**
   ```bash
   python main_bot.py
   ```

### Running with Docker

1. **Build the Docker image:**
   ```bash
   docker build -t expense-tracker-bot .
   ```

2. **Run the container:**
   ```bash
   docker run -d --name expense-tracker-bot -p 5000:5000 expense-tracker-bot
   ```

## 📄 Makefile Explanation

The Makefile includes various commands to simplify development tasks:

- **`make start`**: Activates the Python virtual environment and runs the bot locally.
- **`make install`**: Installs the required dependencies in the virtual environment.
- **`make init-db`**: Initializes the SQLite database used by the bot.
- **`make start-logging`**: Runs the bot in the background and logs output to `bot.log`.
- **`make stop`**: Stops the running bot process.
- **`make lint`**: Checks the code quality using `flake8`.
- **`make update-deps`**: Updates the Python dependencies.

To run a Makefile command, use:
```bash
make <command>
```

For example, to start the bot: `make start`

## 🛠️ Technologies Used

- **Programming Language**: Python
- **Framework**: `python-telegram-bot`
- **Database**: SQLite
- **Containerization**: Docker
- **CI/CD**: GitLab CI/CD
