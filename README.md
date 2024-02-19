# Django Telegram Service

This Django project is a Telegram service that allows users to interact with a Telegram bot through a Django-based web application. The project integrates with the Telegram Bot API to send and receive messages, enabling seamless communication between users and the bot.

## Features

- **Telegram Bot Integration**: Connects to the Telegram Bot API to send and receive messages.
- **Web Interface**: Provides a Django-based web interface for users to interact with the Telegram bot.
- **User Authentication**: Supports user authentication to ensure secure access to the service.
- **Message Logging**: Logs messages exchanged between users and the bot for analytics and debugging purposes.

## Requirements

- Python 3.x
- Django
- Django REST Framework

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/tyrohansen/django_telegram_bot
    ```

2. Navigate to the project directory:

    ```bash
    cd django_telegram_bot
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Configure your Telegram bot:
   
   - Create a new bot using the BotFather on Telegram.
   - Obtain the bot token.
   - Update the `TELEGRAM_TOKEN` variable in `.env` with your bot token.

5. Apply migrations:

    ```bash
    python manage.py migrate
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

7. Access the web interface at `http://127.0.0.1:8000/`.

## Usage

1. Register/Login to the web interface using your credentials.
2. Start a conversation with your Telegram bot by searching for its username on Telegram.
3. Interact with the bot through the web interface.
4. Messages exchanged between users and the bot will be logged for analysis.

## Configuration

- `TELEGRAM_TOKEN`: Token provided by the BotFather for accessing the Telegram Bot API.
- `DEBUG`: Set to `True` for development, `False` for production.
- Additional Django settings can be configured in `.env` as per project requirements.

## Contributing

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.