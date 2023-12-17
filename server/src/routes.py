from logging import getLogger
from typing import Annotated
from fastapi import Header
from fastapi.responses import StreamingResponse, Response

from application import application
from database.nosql import mongo_connection
from database.sql import global_connection
from database.sql import regional_connection
from domain import authentication, duplication
from domain.controllers import user_controller
from domain.controllers import audio_controller
from domain.controllers import audio_collection_controller
from models.api.login import LoginData, LoginResponse, SignupData
from models.api.user import UserData
<<<<<<< HEAD
from models.api.audio import AudioInfoData, SongData, ListSong, DuplicatedSong
=======
from models.api.audio import AudioInfoData, SongData, ListSong
>>>>>>> master
from models.api.audio_collections import CollectionData, CollectionAudioInfoData
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
    token = authentication.login(login_data.user_name, login_data.password)
    return LoginResponse(auth_token=token)


@app.get("/songs/{search_text}")
async def get_songs(search_text: str, token: Annotated[str | None, Header()] = None) -> list[ListSong]:
    user_data = authentication.validate_header(token)
    return audio_controller.get_songs(search_text)


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


# Audio info
@app.get("/audio_info/{audio_info_id}")
async def get_audio_info(audio_info: str, token: Annotated[str | None, Header()] = None) -> AudioInfoData:
    _logger.debug("Get audio info called %d", audio_info)
    return await audio_controller.get_audio_info(audio_info, token)


@app.post("/audio_info")
async def post_audio_info(audio_info: AudioInfoData, token: Annotated[str | None, Header()] = None) -> Response:
    _logger.debug("Post audio info")
    return await audio_controller.post_audio_info(audio_info, token)


@app.delete("/audio_info/{audio_info_id}")
async def delete_audio_info(audio_info: str, token: Annotated[str | None, Header()] = None) -> Response:
    _logger.debug("Delete audio info called %d", audio_info)
    return await audio_controller.delete_audio_info(audio_info, token)


# Audio data
@app.get("/audio_data/{audio_data_id}")
async def get_audio_data(audio_data_id: str, token: Annotated[str | None, Header()] = None) -> StreamingResponse:
    _logger.debug("Get audio data called %d", audio_data_id)
    return await audio_controller.get_audio_data(audio_data_id, token)

@app.post("/audio_data")
async def post_audio_data(audio_data:SongData, token: Annotated[str | None, Header()] = None) -> Response:
    _logger.debug("Post audio data called")
    return await audio_controller.post_audio_data(audio_data, token)


@app.delete("/audio_data/{audio_data_id}")
async def delete_audio_info(audio_data_id: str, token: Annotated[str | None, Header()] = None) -> Response:
    _logger.debug("Delete audio data %d", audio_data_id)
    return await audio_controller.delete_audio_data(audio_data_id, token)


# Audio collection
@app.get("/audio_collection/{audio_collection_id}")
async def get_audio_collection(audio_collection_id: str, token: Annotated[str | None, Header()] = None) -> CollectionData:
    _logger.debug("Get audio collection %d", audio_collection_id)
    return await audio_collection_controller.get_audio_collection(audio_collection_id, token)

@app.post("/audio_collection")
async def post_audio_collection(audio_collection_data: CollectionData, token: Annotated[str | None, Header()] = None) -> Response:
    _logger.debug("Post audio collection")
    return await audio_collection_controller.post_audio_collection(audio_collection_data, token)


@app.delete("/audio_collection/{audio_collection_id}")
async def delete_audio_collection(audio_collection_id: str, token: Annotated[str | None, Header()] = None) -> Response:
    _logger.debug("Get audio collection")
    return await audio_collection_controller.delete_audio_collection(audio_collection_id, token)

# Audio collection member
@app.post("/audio_collection_member")
async def post_audio_collection_member(audio_collection_member_data: CollectionAudioInfoData, token: Annotated[str | None, Header()] = None) -> Response:
    _logger.debug("Post audio collection member")
    return await audio_collection_controller.post_audio_collection_member(audio_collection_member_data, token)


@app.delete("/audio_collection_member/{audio_collection_member_id}")
async def delete_audio_collection_member(audio_collection_member_id: str, token: Annotated[str | None, Header()] = None) -> Response:
    _logger.debug("Delete audio collection member %d", audio_collection_member_id)
    return await audio_collection_controller.delete_audio_collection_member(audio_collection_member_id, token)


@app.on_event("startup")
async def init():
    mongo_connection.init_db()
    global_connection.init_regions()
