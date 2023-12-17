from pydantic import BaseModel
from models.api.audio import AudioInfoData

class CollectionAudioInfoData(AudioInfoData):
    order: int

class CollectionData(BaseModel):
    name: str
    picture_file_id: int
    is_private: bool
    owner_user_id: int
    songs: list[CollectionAudioInfoData]
