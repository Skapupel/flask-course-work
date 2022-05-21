# Flask/Telebot course work

[![Python 3.10.4](https://img.shields.io/badge/python-3.10.4-blue.svg)](https://www.python.org/downloads/release/python-3104/)

**Made by Skapupel**


## Usage


### Install the dependencies:

```
pip install -r requirements.txt
```

### File .env should be created in the project folder with the following variables:

```
TELEGRAM_TOKEN=<your_token> # Your Telegram bot token
SECRET_KEY=<your_secret_key> # Random string
DATABASE_URI=<your_database_uri> # Your database uri, example: postgresql://user:password@host:port/database [Note: Database should exist]
```

### Create the database tables:

```
flask db init
flask db migrate
flask db upgrade
```

### Then you can run the app with:

```
python app.py
```