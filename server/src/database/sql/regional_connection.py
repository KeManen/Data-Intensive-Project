from logging import getLogger

from sqlalchemy import select

from typing import ContextManager

from sqlalchemy.orm import Session

from database.sql.common import ConnectionManager
from models.database.global_models import Region
from models.database.regional_models import RegionalModel, Song, SongPlay, RegionalUser

_logger = getLogger("main.sql.regional_connection")

_logger.debug("Creating regional postgresql connections")
eu_connection_manager = ConnectionManager("postgresql://root:pass@data_eu:5432/data_eu", RegionalModel)
us_connection_manager = ConnectionManager("postgresql://root:pass@data_us:5432/data_us", RegionalModel)


_clients = {
    "eu": eu_connection_manager,
    "us": us_connection_manager
}


def _get_client(region_name: str) -> ConnectionManager:
    assert region_name in _clients, f"Could not find connection manager for region {region_name}"
    return _clients.get(region_name)


def test_db():
    with eu_connection_manager.session() as session:
        _logger.debug("Testing regional postgresql database")
        _logger.debug("Test over")
    with us_connection_manager.session() as session:
        _logger.debug("Testing regional postgresql database")
        _logger.debug("Test over")


def insert_song(region_name: str, name: str, track_length_ms: int, user_id: int) -> Song:
    client = _get_client(region_name)
    with client.session() as session:
        song = Song(name=name, track_length_ms=track_length_ms, artist_user_id=user_id)
        session.add(song)
        session.commit()
        return session.scalar(select(Song).where(Song.name == song.name))


def get_song(region_name: str, song_name: str) -> Song:
    client = _get_client(region_name)
    with client.session() as session:
        return session.scalar(select(Song).where(Song.name == song_name))


def add_play(region_name: str, user_id: int, global_song_id: int):
    client = _get_client(region_name)
    play = SongPlay(user_id=user_id, global_song_id=global_song_id)
    with client.session() as session:
        session.add(play)
        session.commit()


def get_user(region_name:str, user_name:str) -> RegionalUser:
    with _get_client(region_name).session() as session:
        return session.scalar(select(RegionalUser).where(RegionalUser.name == user_name))

def create_user(region_name:str, user_data: RegionalUser) -> RegionalUser:
    with _get_client(region_name).session() as session:
        session.add(user_data)
        session.commit()
    return get_user(region_name)

def delete_user(region_name:str, user_data: RegionalUser):
    with _get_client(region_name).session() as session:
        session.delete(user_data)
        session.commit()