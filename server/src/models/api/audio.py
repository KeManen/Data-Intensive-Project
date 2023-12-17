from pydantic import BaseModel


class SongData(BaseModel):
    name: str
    artist_user_id: int
    data: bytes


class CreateSongResponse(BaseModel):
    song_id: int
