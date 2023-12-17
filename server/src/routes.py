from logging import getLogger

from application import application
from database.nosql import mongo_connection
from database.sql import global_connection
from database.sql import regional_connection
from domain import authentication
from domain.controllers import user_controller
from domain.controllers import audio_controller
from domain.controllers import audio_collection_controller
from models.api.login import LoginData, LoginResponse, SignupData
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
    token = authentication.create_user(signup_data.user_name, signup_data.password, signup_data.region_id)
    return LoginResponse(auth_token=token)


@app.post("/login")
async def login(login_data: LoginData) -> LoginResponse:
    token = authentication.login(login_data.user_name, login_data.password)
    return LoginResponse(auth_token=token)


# User
@app.get("/user/{user_id}")
async def get_user(user_id: int):
    _logger.debug("Get user called %d", user_id)
    return await user_controller.get_user(user_id)


@app.post("/user")
async def post_user():
    _logger.debug("User post called")
    return await user_controller.post_user()


@app.delete("/user/{user_id}")
async def delete_user(user_id: int):
    _logger.debug("User delete called for %d", user_id)
    return await user_controller.delete_user()


# Audio info
@app.get("/audio_info/{audio_info_id}")
async def get_audio_info(audio_info: int):
    _logger.debug("Get audio info called %d", audio_info)
    return await audio_controller.get_audio_info(audio_info)


@app.post("/audio_info")
async def post_audio_info():
    _logger.debug("Post audio info")
    return await audio_controller.post_audio_info()


@app.delete("/audio_info/{audio_info_id}")
async def delete_audio_info(audio_info: int):
    _logger.debug("Delete audio info called %d", audio_info)
    return await audio_controller.delete_audio_info(audio_info)


# Audio data
@app.get("/audio_data/{audio_data_id}")
async def get_audio_data(audio_data: int):
    _logger.debug("Get audio data called %d", audio_data)
    return await audio_controller.get_audio_data(audio_data)


@app.post("/audio_data")
async def post_audio_data():
    _logger.debug("Post audio data called")
    return await audio_controller.post_audio_data()


@app.delete("/audio_data/{audio_data_id}")
async def delete_audio_info(audio_data: int):
    _logger.debug("Delete audio data %d", audio_data)
    return await audio_controller.delete_audio_data(audio_data)


# Audio collection
@app.get("/audio_collection/{audio_collection_id}")
async def get_audio_collection(audio_collection_id: int):
    _logger.debug("Get audio collection %d", audio_collection_id)
    return await audio_collection_controller.get_audio_collection(audio_collection_id)


@app.post("/audio_collection")
async def post_audio_collection():
    _logger.debug("Post audio collection")
    return await audio_collection_controller.post_audio_collection()


@app.delete("/audio_collection/{audio_collection_id}")
async def delete_audio_collection(audio_collection_id: int):
    _logger.debug("Get audio collection")
    return await audio_collection_controller.delete_audio_collection(audio_collection_id)


# Audio collection member
@app.post("/audio_collection_member")
async def post_audio_collection_member():
    _logger.debug("Post audio collection member")
    return await audio_collection_controller.post_audio_collection_member()


@app.delete("/audio_collection_member/{audio_collection_member_id}")
async def delete_audio_collection_member(audio_collection_member_id: int):
    _logger.debug("Delete audio collection member %d", audio_collection_member_id)
    return await audio_collection_controller.delete_audio_collection_member(audio_collection_member_id)


@app.on_event("startup")
async def init():
    mongo_connection.init_db()
