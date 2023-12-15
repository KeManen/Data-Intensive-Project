from logging import getLogger

from pymongo import MongoClient

client = MongoClient("mongodb://root:pass@127.0.0.1:27017/")
_logger = getLogger("main.nosql.mongo_connection")


def test_db():
    _logger.debug("testing database")
    _logger.debug(client.list_database_names())
    _logger.debug("test over")
