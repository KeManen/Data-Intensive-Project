import datetime
import secrets
from logging import getLogger

import bcrypt

from database.sql.global_connection import get_user_login, create_user_login, get_region_from_name
from models.database.global_models import UserLogin

_logger = getLogger("authentication")

_tokens: {str, (UserLogin, datetime.datetime)} = {}


def salt_and_hash(password: str) -> str:
    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    return hashed.decode(encoding="utf-8")


def validate(password: str, candidate: str) -> bool:
    return bcrypt.checkpw(password.encode("utf-8"), candidate.encode("utf-8"))


def _create_token(user_login: UserLogin) -> str:
    session_token = secrets.token_urlsafe(16)
    _tokens[session_token] = (user_login, datetime.datetime.now())
    return session_token


def login(user_name: str, password: str) -> str:
    user_login = get_user_login(user_name)
    assert user_login is not None, f"Could not find user with name {user_name}"
    if validate(password, user_login.password_hash_salt):
        return _create_token(user_login)
    raise Exception(f"Invalid password for user {user_name}")


def create_user(user_name: str, password: str, region_name: str) -> str:
    _logger.debug(f"Getting region {region_name}")
    region = get_region_from_name(region_name)
    _logger.debug(f"Creating login data...")
    user_login = create_user_login(user_name, password, region.id)
    return _create_token(user_login)


def validate_header(header_token: str) -> UserLogin:
    assert header_token in _tokens, "Invalid session!"
    return _tokens[header_token][0]


def clear_tokens(invalid_token_duration: datetime.timedelta = datetime.timedelta(hours=2)):
    for token, data in _tokens.items():
        if datetime.datetime.now() - data[1] > invalid_token_duration:
            _tokens.pop(token)
