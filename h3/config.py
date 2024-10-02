from dotenv import load_dotenv

load_dotenv()

from os import environ

SECRET_KEY = environ.get("SECRET_KEY", "labas grybas be ragu")

SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
SQLALCHEMY_ENGINE_OPTIONS = {
    "pool_size": 2,
    "max_overflow": 1,
    # 'echo_pool': 'debug'
}
SQLALCHEMY_ECHO = environ.get("SQLALCHEMY_ECHO", default=False)

# from dotenv import load_dotenv
# from os import environ
# from pathlib import Path
# load_dotenv()
#
# JWT_SECRET_KEY = environ.get("JWT_SECRET_KEY", "random-secret-key-very-random-please-change")
# JWT_ACCESS_TOKEN_EXPIRES = environ.get("JWT_ACCESS_TOKEN_EXPIRES", 3600)

