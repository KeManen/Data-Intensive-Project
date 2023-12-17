from logging import getLogger

from sqlalchemy import select

from typing import ContextManager

from sqlalchemy.orm import Session

from database.sql.common import ConnectionManager
from database.sql.global_connection import get_region, get_region_from_name
from models.database.global_models import Region, GlobalSong, UserLogin
from models.database.regional_models import RegionalModel, Song, SongPlay, RegionalUser, AccountType

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


def init_clients():
    for region, client in _clients.items():
        with client.session() as session:
            try:
                region_id = get_region_from_name(region).id
                session.add(AccountType(identifier="Normal", id=1, price=999, region_id=region_id))
                session.commit()
                _logger.debug(f"Added base account type for region {region}")
            except Exception as _:
                pass



def test_db():
    with eu_connection_manager.session() as session:
        _logger.debug("Testing regional postgresql database")
        _logger.debug("Test over")
    with us_connection_manager.session() as session:
        _logger.debug("Testing regional postgresql database")
        _logger.debug("Test over")


def insert_song(region: Region, name: str, track_length_ms: int, user_id: int) -> Song:
    client = _get_client(region.name)
    with client.session() as session:
        song = Song(name=name, track_length_ms=track_length_ms, artist_user_id=user_id, region_id=region.id)
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


def get_user(region_name: str, user_name: str) -> RegionalUser:
    with _get_client(region_name).session() as session:
        return session.scalar(select(RegionalUser).where(RegionalUser.name == user_name))


def create_user(region_name: str, user_data: RegionalUser) -> RegionalUser:
    with _get_client(region_name).session() as session:
        session.add(user_data)
        session.commit()
    return get_user(region_name, user_data.name)


def delete_user(region_name: str, user_data: RegionalUser):
    with _get_client(region_name).session() as session:
        session.delete(user_data)
        session.commit()


def get_song_duplication_regions(song: GlobalSong) -> list[str]:
    regions = []
    for region_name, client in _clients.items():
        with client.session() as session:
            play_count = len(session.scalars(select(SongPlay).where(SongPlay.global_song_id == song.id)).all())
            if play_count >= 5:
                regions.append(region_name)
    return regions


def create_regional_user(global_user: UserLogin):
    regional_user = RegionalUser(name=global_user.name, id=global_user.id, account_type_id=1,
                                 region_id=global_user.region_id)
    client = _get_client(get_region(global_user.region_id).name)
    with client.session() as session:
        session.add(regional_user)
        session.commit()
    _logger.debug(f"Created user {regional_user}")
