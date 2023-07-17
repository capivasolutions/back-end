import os
from dotenv import load_dotenv

load_dotenv()


class Environment:
    """
        Environment is the main access port to .env variables.
    """
    DATABASE_PORT = os.getenv('DATABASE_PORT')
    DATABASE_NAME = os.getenv('DATABASE_NAME')
    DATABASE_HOST = os.getenv('DATABASE_HOST')
    DATABASE_USER = os.getenv('DATABASE_USER')
    DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')

    CLASSIFIER_URL = os.getenv('CLASSIFIER_URL')
