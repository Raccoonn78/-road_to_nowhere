import os

HELLO_MESSAGE="Всем привет, это сервер RACCOON!" # не забудь про app.config['JSON_AS_ASCII'] = False
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///db/data.db") # DATABASE_URL д.б. проброшено из Docker Compose
SQLALCHEMY_TRACK_MODIFICATIONS = False
PATH_TO_LOGGER="py_log.log"
SECRET_KEY="123qweasd"