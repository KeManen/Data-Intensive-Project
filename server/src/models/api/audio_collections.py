from pydantic import BaseModel


class JSONPlaylist(BaseModel):
    name: str
    picture_file_id: int
    is_private: bool
    owner_user_id: int
    songs: list[int]
