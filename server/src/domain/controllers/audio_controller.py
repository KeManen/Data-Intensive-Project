from fastapi.responses import StreamingResponse

from authentication import validate_header

from ...models.api.audio import AudioInfoData, ArtistInfoData, AudioData
from ...models.database.regional_models import Song

async def _audio_data_streamer(data:bytes):
    for byte in data:
        yield byte

async def get_audio_data(audio_data_id:int, token:str) -> StreamingResponse:
    user_login = validate_header(token)

    return StreamingResponse(_audio_data_streamer())


async def post_audio_data(audio_data:AudioData, token:str):
    user_login = validate_header(token)
    yield NotImplementedError


async def delete_audio_data(audio_data_id: int, token:str):
    user_login = validate_header(token)
    yield NotImplementedError


async def get_audio_info(audio_data_id: int, token:str):
    user_login = validate_header(token)

    yield NotImplementedError


async def post_audio_info(audio_data:AudioData,token:str):
    user_login = validate_header(token)
    yield NotImplementedError


async def delete_audio_info(audio_data_id: int, token:str):
    user_login = validate_header(token)
    yield NotImplementedError
