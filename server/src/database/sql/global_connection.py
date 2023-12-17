from logging import getLogger

from sqlalchemy import select

from database.sql.common import ConnectionManager
from models.database.global_models import GlobalModel, Currency, Region, UserLogin, GlobalSong

_logger = getLogger("main.sql.global_connection")

_logger.debug("Creating global postgresql connection")
connection_manager = ConnectionManager("postgresql://root:pass@data_global:5432/data_global", GlobalModel)


def test_db():
    with connection_manager.session() as session:
        _logger.debug("Testing global postgresql database")
        currency = Currency(name="Euro", code="EUR", rate_to_usd=108000)
        region = Region(name="Europe", currency_id=currency.id, currency=currency)
        session.add(region)
        session.commit()
        _logger.debug(session.scalar(select(Region).where(Region.id == region.id)))
        session.delete(region)
        _logger.debug("Test over")


def init_regions():
    with connection_manager.session() as session:
        euro = get_currency_from_name("Euro") or Currency(name="Euro", code="EUR", rate_to_usd=1.08)
        if get_region_from_name("eu") is None:
            session.add(Region(name="eu", currency=euro))

        dollar = get_currency_from_name("Dollar") or Currency(name="Dollar", code="USD", rate_to_usd=1)
        if get_region_from_name("us") is None:
            session.add(Region(name="us", currency=dollar))

        session.commit()


def create_user_login(user_name: str, password_hash: str, region_id: int) -> UserLogin:
    with connection_manager.session() as session:
        session.add(UserLogin(user_name=user_name, password_hash_salt=password_hash, region_id=region_id))
        session.commit()
        return get_user_login(user_name)


def get_user_login(user_name: str) -> UserLogin:
    with connection_manager.session() as session:
        return session.scalar(select(UserLogin).where(UserLogin.name == user_name))


def get_region(region_id: int) -> Region:
    with connection_manager.session() as session:
        return session.scalar(select(Region).where(Region.id == region_id))


def get_region_from_name(region_name: str) -> Region:
    with connection_manager.session() as session:
        return session.scalar(select(Region).where(Region.name == region_name))


def get_currency(currency_id: int) -> Currency:
    with connection_manager.session() as session:
        return session.scalar(select(Currency).where(Currency.id == currency_id))


def get_currency_from_name(currency_name: str) -> Currency:
    with connection_manager.session() as session:
        return session.scalar(select(Currency).where(Currency.name == currency_name))


def insert_song(song_name: str, region_id: int, primary_region: bool) -> GlobalSong:
    with connection_manager.session() as session:
        new_song = GlobalSong(name=song_name, region_id=region_id, is_primary_region=primary_region)
        session.add(new_song)
        session.commit()
        return new_song


def get_relevant_song(song_name: str, region_id: int) -> GlobalSong:
    with connection_manager.session() as session:
        local_song = session.scalar(select(GlobalSong)
                                    .where(GlobalSong.name == song_name and GlobalSong.region_id == region_id))
        if local_song is not None:
            return local_song

        primary_song = session.scalar(select(GlobalSong)
                                      .where(GlobalSong.name == song_name and GlobalSong.is_primary_region))
        return primary_song
