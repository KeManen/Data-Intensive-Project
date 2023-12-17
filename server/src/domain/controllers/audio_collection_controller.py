from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from domain.authentication import validate_header

from models.api.audio_collections import AudioInfoData, CollectionAudioInfoData


async def get_audio_collection(audio_collection_id: int, token:str) -> JSONResponse:
    user_login = validate_header(token)
    playlist = CollectionAudioInfoData(name="PlaylistName", picture_file_id=69, is_private=False, owner_user_id=69,
                            songs=[0, 1, 2, 3, 4, 5])
    json_data = jsonable_encoder(playlist)
    return JSONResponse(content=json_data)


async def post_audio_collection(audio_collection_data: CollectionAudioInfoData, token:str):
    user_login = validate_header(token)
    yield NotImplementedError


async def delete_audio_collection(audio_collection_id: int, token: str):
    user_login = validate_header(token)
    yield NotImplementedError


async def post_audio_collection_member(audio_collection_data: AudioInfoData, token:str):
    user_login = validate_header(token)
    yield NotImplementedError


async def delete_audio_collection_member(member_id: int, token:str):
    user_login = validate_header(token)
    yield NotImplementedError
