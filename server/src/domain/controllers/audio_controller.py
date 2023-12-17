from fastapi.responses import StreamingResponse, JSONResponse
from logging import getLogger


from domain.authentication import validate_header

from models.api.audio import SongData, ListSong
from database.nosql import mongo_connection
from database.sql import global_connection, regional_connection

_logger = getLogger("main.audio_controller")

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


def post_audio_data(audio_data: SongData, user_id: int, region_id: int):
    return _post_song(region_id, audio_data, user_id)


async def delete_audio_data(audio_data_name: str, token:str):
    user_login = validate_header(token)
    mongo_connection.remove_song(user_login.region_id, audio_data_name)

def _post_song(region_id: int, song_data: SongData, user_id: int) -> int:
    global_connection.insert_song(song_data.name, region_id, True)
    region = global_connection.get_region(region_id)
    song = regional_connection.insert_song(region, song_data.name, len(song_data.data), user_id)
    mongo_connection.save_song(region.name, song.id, song_data.data)
    return song.id


async def _get_song_bytes(region_id: int, song_name: str) -> bytes:
    most_relevant_song = global_connection.get_relevant_song(song_name, region_id)
    region = global_connection.get_region(most_relevant_song.region_id)
    region_song_file_id = regional_connection.get_song(region.name, song_name).id
    regional_connection.add_play(region, most_relevant_song.id)
    return mongo_connection.get_song(region.name, region_song_file_id)


def get_songs(search_text: str) -> list[ListSong]:
    songs = global_connection.get_songs(search_text)
    _logger.debug(f"{[song.name for song in songs]}")
    return [ListSong(song_name=song.name) for song in songs]
