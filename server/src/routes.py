from logging import getLogger
from typing import Annotated
from fastapi import Header
from fastapi.responses import StreamingResponse, Response
from starlette.requests import Request

from application import application
from database.nosql import mongo_connection
from database.sql import global_connection
from database.sql import regional_connection
from domain import authentication, duplication
from domain.controllers import user_controller
from domain.controllers import audio_controller
from models.api.login import LoginData, LoginResponse, SignupData
from models.api.user import UserData
from models.api.audio import SongData, ListSong, DuplicatedSong
from models.test import Test

_logger = getLogger("main.routes")
app = application


@app.get("/")
async def root():
    _logger.debug("Root called")
    return Test(message="Hello world")


@app.get("/dbtest")
async def test_database():
    _logger.debug("Testing all database connections:")
    mongo_connection.test_db()
    global_connection.test_db()
    regional_connection.test_db()


@app.post("/signup")
async def sign_up(signup_data: SignupData) -> LoginResponse:
    _logger.debug("Creating user account")
    token = authentication.create_user(signup_data.user_name, signup_data.password, signup_data.region_name)
    return LoginResponse(auth_token=token)


@app.post("/login")
async def login(login_data: LoginData) -> LoginResponse:
    _logger.debug(f"Logging in with {login_data}")
    token = authentication.login(login_data.user_name, login_data.password)
    return LoginResponse(auth_token=token)


@app.get("/songs")
async def get_songs(name: str, token: Annotated[str | None, Header()] = None) -> list[ListSong]:
    user = authentication.validate_header(token)
    return audio_controller.get_songs(name)


@app.get("/devtool")
async def calculate_data_duplication() -> list[DuplicatedSong]:
    return duplication.calculate_new_duplicates()


# User
@app.get("/user/{user_name}")
async def get_user(user_name: str, token: Annotated[str | None, Header()] = None) -> UserData:
    _logger.debug("Get user called %d", user_name)
    return await user_controller.get_user(user_name, token)


@app.post("/user")
async def post_user(user_data: UserData, token: Annotated[str | None, Header()] = None) -> Response:
    _logger.debug("User post called")
    return await user_controller.post_user(user_data, token)


@app.delete("/user/{user_name}")
async def delete_user(user_name: int, token: Annotated[str | None, Header()] = None) -> Response:
    _logger.debug("User delete called for %d", user_name)
    return await user_controller.delete_user(user_name, token)


# Audio data
@app.get("/audio_data_stream/{audio_data_name}")
async def get_audio_data_stream(audio_data_id: str, token: Annotated[str | None, Header()] = None) -> StreamingResponse:
    _logger.debug("Get audio data stream called %d", audio_data_id)
    return await audio_controller.get_audio_data_stream(audio_data_id, token)


@app.get("/audio_data/{audio_data_name}")
async def get_audio_data(audio_data_id: str, token: Annotated[str | None, Header()] = None) -> bytes:
    _logger.debug("Get audio data called %d", audio_data_id)
    return audio_controller.get_audio_data(audio_data_id, token)


@app.post("/audio_data")
async def post_audio_data(audio_data: SongData, token: Annotated[str | None, Header()] = None) -> Response:
    _logger.debug("Post audio data called")
    user = authentication.validate_header(token)
    return audio_controller.post_audio_data(audio_data, user.id, user.region_id)


@app.delete("/audio_data/{audio_data_name}")
async def delete_audio_info(audio_data_name: str, token: Annotated[str | None, Header()] = None) -> Response:
    _logger.debug("Delete audio data %d", audio_data_name)
    return await audio_controller.delete_audio_data(audio_data_name, token)


@app.on_event("startup")
async def init():
    mongo_connection.init_db()
    global_connection.init_regions()
    regional_connection.init_clients()
