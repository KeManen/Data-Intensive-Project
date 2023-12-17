from logging import getLogger

from typing import ContextManager

from sqlalchemy.orm import Session, select


from database.sql.common import ConnectionManager
from models.database.regional_models import RegionalModel, RegionalUser

_logger = getLogger("main.sql.regional_connection")

_logger.debug("Creating regional postgresql connections")
eu_connection_manager = ConnectionManager("postgresql://root:pass@data_eu:5432/data_eu", RegionalModel)
us_connection_manager = ConnectionManager("postgresql://root:pass@data_us:5432/data_us", RegionalModel)


def test_db():
    with eu_connection_manager.session() as session:
        _logger.debug("Testing regional postgresql database")
        _logger.debug("Test over")
    with us_connection_manager.session() as session:
        _logger.debug("Testing regional postgresql database")
        _logger.debug("Test over")


def _get_region_session(region_name:str) -> ContextManager[Session]:
    match region_name:
        case 'eu':
            return eu_connection_manager.session()
        case 'us':    
            return us_connection_manager.session()

def get_user(region_name:str, user_name:str) -> RegionalUser:
    with _get_region_session(region_name) as session:
        return session.scalar(select(RegionalUser).where(RegionalUser.name == user_name))

def create_user(region_name:str, user_data: RegionalUser) -> RegionalUser:
    with _get_region_session(region_name) as session:
        session.add(user_data)
        session.commit()
    return get_user(region_name)

def delete_user(region_name:str, user_data: RegionalUser):
    with _get_region_session(region_name) as session:
        session.delete(user_data)
        session.commit()