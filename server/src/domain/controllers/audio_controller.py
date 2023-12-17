from fastapi.responses import StreamingResponse, JSONResponse

from domain.authentication import validate_header

from models.api.audio import AudioInfoData, ArtistInfoData, SongData
from models.database.regional_models import Song
from database.nosql import mongo_connection
from database.sql import global_connection, regional_connection

async def _audio_data_streamer(data:bytes):
    for byte in data:
        yield byte

async def get_audio_data_stream(audio_data_name:str, token:str) -> StreamingResponse:
    audio_data = await get_audio_data(audio_data_name, token)
    return StreamingResponse(_audio_data_streamer(audio_data))

async def get_audio_data(audio_data_name:str, token:str) -> bytes:
    user_login = validate_header(token)
    audioData = _get_song_bytes(user_login.region.id, audio_data_name)
    return audioData


async def post_audio_data(audio_data:SongData, token:str):
    user_login = validate_header(token)
    return _post_song(user_login.region.id, audio_data, user_login.id)


async def delete_audio_data(audio_data_name: str, token:str):
    user_login = validate_header(token)
    mongo_connection.remove_song(user_login.region_id, audio_data_name)

#AudioInfos is out of scope for this prototype.
async def get_audio_info(audio_data_name: str, token:str) -> AudioInfoData:
    user_login = validate_header(token)
    song = regional_connection.get_song(user_login.region_id, audio_data_name)
    yield NotImplementedError


async def post_audio_info(audio_data:AudioInfoData,token:str):
    user_login = validate_header(token)
    yield NotImplementedError


async def delete_audio_info(audio_data_name: str, token:str):
    user_login = validate_header(token)
    globalSong = global_connection.get_relevant_song(audio_data_name, user_login.region.id)
    global_connection.remove_song(globalSong)
    yield NotImplementedError


async def _post_song(region_id: int, song_data: SongData, user_id: int) -> int:
    global_connection.insert_song(song_data.name, region_id, True)
    region_name = global_connection.get_region(region_id).name
    song = regional_connection.insert_song(region_name, song_data.name, len(song_data.data), user_id)
    mongo_connection.save_song(region_name, song.id, song_data.data)
    return song.id


async def _get_song_bytes(region_id: int, song_name: str) -> bytes:
    most_relevant_song = global_connection.get_relevant_song(song_name, region_id)
    region = global_connection.get_region(most_relevant_song.region_id)
    region_song_file_id = regional_connection.get_song(region.name, song_name).id
    regional_connection.add_play(region, most_relevant_song.id)
    return mongo_connection.get_song(region.name, region_song_file_id)
