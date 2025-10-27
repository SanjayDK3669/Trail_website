import os
from urllib.parse import quote_plus
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

class Config:
    DB_USER = os.getenv("DB_USER")
    DB_PASS = quote_plus(os.getenv("DB_PASS", ""))
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "3306")
    DB_NAME = os.getenv("DB_NAME")

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}?charset=utf8mb4"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "*")
    SECRET_KEY = os.getenv("SECRET_KEY", "change-me-to-a-secure-random-value")
