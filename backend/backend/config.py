import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    # Secret key for security (sessions, tokens)
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")

    # Database configuration (PostgreSQL)
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

    # Disable modification tracking (improves performance)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # OpenAI API Key (AI recommendations)
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    # SendGrid API Key (email notifications)
    SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
