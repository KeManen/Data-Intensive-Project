from pydantic import BaseModel

class ArtistInfoData(BaseModel):
    name:str
    about:str

class AudioInfoData(BaseModel):
    name:str
    track_length_ms: int
    playback_track_id: int
    artist: ArtistInfoData

class AudioData(AudioInfoData):
    data: bytes
