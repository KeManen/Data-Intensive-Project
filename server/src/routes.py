from logging import getLogger

from application import application
from database.nosql import mongo_connection
from database.sql import global_connection
from database.sql import regional_connection
from models.test import Test


from controllers.user_controller import get_user as controller_user_get
from controllers.user_controller import post_user as controller_user_post
from controllers.user_controller import delete_user as controller_user_delete

from controllers.audio_controller import get_audio_info as controller_audio_info_get
from controllers.audio_controller import post_audio_info as controller_audio_info_post
from controllers.audio_controller import delete_audio_info as controller_audio_info_delete

from controllers.audio_controller import get_audio_data as controller_audio_data_get
from controllers.audio_controller import post_audio_data as controller_audio_data_post
from controllers.audio_controller import delete_audio_data as controller_audio_data_delete

from controllers.audio_collection_controller import get_audio_collection as controller_audio_collection_get
from controllers.audio_collection_controller import post_audio_collection as controller_audio_collection_post
from controllers.audio_collection_controller import delete_audio_collection as controller_audio_collection_delete
from controllers.audio_collection_controller import post_audio_collection_member as controller_audio_collection_member_post
from controllers.audio_collection_controller import delete_audio_collection_member as controller_audio_collection_member_delete


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


# User
@app.get("/user/{user_id}")
async def get_user(user_id: int):
    _logger.debug("Get user called %d", user_id)
    return await controller_user_get(user_id)


@app.post("/user")
async def post_user():
    _logger.debug("User post called")
    return await controller_user_post()


@app.delete("/user/{user_id}")
async def delete_user(user_id: int):
    _logger.debug("User delete called for %d", user_id)
    return await controller_user_delete()


# Audio info
@app.get("/audio_info/{audio_info_id}")
async def get_audio_info(audio_info: int):
    _logger.debug("Get audio info called %d", audio_info)
    return await controller_audio_info_get(audio_info)


@app.post("/audio_info")
async def post_audio_info():
    _logger.debug("Post audio info")
    return await controller_audio_info_post()


@app.delete("/audio_info/{audio_info_id}")
async def delete_audio_info(audio_info: int):
    _logger.debug("Delete audio info called %d", audio_info)
    return await controller_audio_info_delete(audio_info)

# Audio data
@app.get("/audio_data/{audio_data_id}")
async def get_audio_data(audio_data: int):
    _logger.debug("Get audio data called %d", audio_data)
    return await controller_audio_data_get(audio_data)

@app.post("/audio_data")
async def post_audio_data():
    _logger.debug("Post audio data called")
    return await controller_audio_data_post()


@app.delete("/audio_data/{audio_data_id}")
async def delete_audio_info(audio_data: int):
    _logger.debug("Delete audio data %d", audio_data)
    return await controller_audio_data_delete


# Audio collection
@app.get("/audio_collection/{audio_collection_id}")
async def get_audio_collection(audio_collection_id: int):
    _logger.debug("Get audio collection %d", audio_collection_id)
    return await controller_audio_collection_get(audio_collection_id)


@app.post("/audio_collection")
async def post_audio_collection():
    _logger.debug("Post audio collection")
    return await controller_audio_collection_post()


@app.delete("/audio_collection/{audio_collection_id}")
async def delete_audio_collection(audio_collection_id: int):
    _logger.debug("Get audio collection")
    return await controller_audio_collection_delete(audio_collection_id)


# Audio collection member
@app.post("/audio_collection_member")
async def post_audio_collection_member():
    _logger.debug("Post audio collection member")
    return await controller_audio_collection_member_post()


@app.delete("/audio_collection_member/{audio_collection_member_id}")
async def delete_audio_collection_member(audio_collection_member_id: int):
    _logger.debug("Delete audio collection member %d", audio_collection_member_id)
    return await controller_audio_collection_member_delete(audio_collection_member_id)