from dotenv import load_dotenv
import os


def get_from_env(key):
    dotenv_path = '.env'
    load_dotenv(dotenv_path)
    return os.environ.get(key)