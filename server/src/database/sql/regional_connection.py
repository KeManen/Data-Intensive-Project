from logging import getLogger

from sqlalchemy import select

from database.sql.common import ConnectionManager
from models.regional_models import RegionalModel


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
