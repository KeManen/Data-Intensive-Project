from logging import getLogger

from sqlalchemy import select

from database.sql.common import ConnectionManager
from models.global_models import GlobalModel, Currency, Region, UserLogin

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


def create_user_login(user_name: str, password_hash: str, region_id: int) -> UserLogin:
    with connection_manager.session() as session:
        session.add(UserLogin(user_name=user_name, password_hash_salt=password_hash, region_id=region_id))
        session.commit()
        return get_user_login(user_name)


def get_user_login(user_name: str) -> UserLogin:
    with connection_manager.session() as session:
        return session.scalar(select(UserLogin).where(UserLogin.name == user_name))
