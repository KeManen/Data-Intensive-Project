from logging import getLogger

from sqlalchemy import select

from database.sql.common import ConnectionManager
from models.regional_models import RegionalModel


_logger = getLogger("main.sql.regional_connection")

_logger.debug("Creating europe postgresql connection")
connection_manager = ConnectionManager("postgresql://root:pass@data_eu:5432/data_eu", RegionalModel)


def test_db():
    with connection_manager.session() as session:
        _logger.debug("Testing regional postgresql database")
        _logger.debug("Test over")
