from pydantic import BaseModel


class ArtistInfoData(BaseModel):
    name: str
    about: str


class AudioInfoData(BaseModel):
    name: str
    track_length_ms: int
    playback_track_id: int
    artist: ArtistInfoData


class SongData(BaseModel):
    name: str
    artist_user_id: int
    data: bytes


class CreateSongResponse(BaseModel):
    song_id: int


class ListSong(BaseModel):
    song_name: str


class DuplicatedSong(BaseModel):
    song_name: str
    region_code: str
