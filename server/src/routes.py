from logging import getLogger

from application import application

_logger = getLogger("main.routes")
app = application


@app.get("/")
async def root():
    _logger.debug("Root called")


# User
@app.get("/user/{user_id}")
async def get_user(user_id: int):
    raise NotImplementedError


@app.post("/user")
async def post_user():
    raise NotImplementedError


@app.delete("/user/{user_id}")
async def delete_user(user_id: int):
    raise NotImplementedError


# Audio info
@app.get("/audio_info/{audio_info_id}")
async def get_audio_info(audio_info: int):
    raise NotImplementedError


@app.post("/audio_info")
async def post_audio_info():
    raise NotImplementedError


@app.delete("/audio_info/{audio_info_id}")
async def delete_audio_info(audio_info: int):
    raise NotImplementedError


# Audio data
@app.get("/audio_data/{audio_data_id}")
async def get_audio_data(audio_data: int):
    raise NotImplementedError


@app.post("/audio_data")
async def post_audio_data():
    raise NotImplementedError


@app.delete("/audio_data/{audio_data_id}")
async def delete_audio_info(audio_data: int):
    raise NotImplementedError


# Audio collection
@app.get("/audio_collection/{audio_collection_id}")
async def get_audio_collection(audio_collection_id: int):
    raise NotImplementedError


@app.post("/audio_collection")
async def post_audio_collection():
    raise NotImplementedError


@app.delete("/audio_collection/{audio_collection_id}")
async def delete_audio_collection(audio_collection_id: int):
    raise NotImplementedError


# Audio collection member
@app.post("/audio_collection_member")
async def post_audio_collection_member():
    raise NotImplementedError


@app.delete("/audio_collection_member/{audio_collection_member_id}")
async def delete_audio_collection_member(audio_collection_member_id: int):
    raise NotImplementedError