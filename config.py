import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

db_path = os.environ.get('DATABASE_URL')

if db_path is None:
    db_path = f'sqlite:///{BASE_DIR / "base.db"})'
else:
    db_path = db_path.replace("://", "ql://", 1)


class Config:
    SQLALCHEMY_DATABASE_URI = db_path
    TEST_DATABASE_URI = f'sqlite:///{BASE_DIR / "test.db"}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Зачем эта настройка: https://flask-sqlalchemy-russian.readthedocs.io/ru/latest/config.html#id2
    DEBUG = True
    PORT = 5000
    SECRET_KEY = "My secret key =)"
    RESTFUL_JSON = {
        'ensure_ascii': False,
    }
    LANGUAGES = ['en', 'ru']
