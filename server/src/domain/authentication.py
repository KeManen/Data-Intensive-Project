import datetime
import secrets

import bcrypt

from database.sql.global_connection import get_user_login, create_user_login
from models.global_models import UserLogin

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


def create_user(user_name: str, password: str, region_id: int) -> str:
    user_login = create_user_login(user_name, password, region_id)
    return _create_token(user_login)


def clear_tokens(invalid_token_duration: datetime.timedelta = datetime.timedelta(hours=2)):
    for token, data in _tokens.items():
        if datetime.datetime.now() - data[1] > invalid_token_duration:
            _tokens.pop(token)
