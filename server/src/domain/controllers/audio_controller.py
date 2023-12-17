from models.api.audio import SongData


async def get_audio_data(audio_id):
    yield NotImplementedError


async def post_audio_data():
    yield NotImplementedError


async def delete_audio_data(audio_data_id):
    yield NotImplementedError


async def get_audio_info(audio_id):
    yield NotImplementedError


async def post_audio_info():
    yield NotImplementedError


async def delete_audio_info(audio_data_id):
    yield NotImplementedError


async def post_song(region_id: int, song_data: SongData) -> int:
    pass
