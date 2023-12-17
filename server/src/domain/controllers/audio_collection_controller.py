from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel


class JSONPlaylist(BaseModel):
    name: str
    picture_file_id: int
    is_private: bool
    owner_user_id: int
    songs: list[int]


async def get_audio_collection(audio_collection_id: int) -> JSONResponse:
    playlist = JSONPlaylist(name="PlaylistName", picture_file_id=69, is_private=False, owner_user_id=69,
                            songs=[0, 1, 2, 3, 4, 5])
    json_data = jsonable_encoder(playlist)
    return JSONResponse(content=json_data)


async def post_audio_collection():
    yield NotImplementedError


async def delete_audio_collection(audio_collection_id: int):
    yield NotImplementedError


async def post_audio_collection_member():
    yield NotImplementedError


async def delete_audio_collection_member(member_id: int):
    yield NotImplementedError
