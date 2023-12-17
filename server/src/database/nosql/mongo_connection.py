from logging import getLogger
from typing import Any, Mapping

from pymongo import MongoClient
from pymongo.database import Database
from pymongo.errors import CollectionInvalid

eu_client = MongoClient("mongodb://root:pass@mongo_eu:27017/")
us_client = MongoClient("mongodb://root:pass@mongo_us:27017/")
_logger = getLogger("main.nosql.mongo_connection")

_clients = {
    "eu": eu_client,
    "us": us_client
}


def get_database(region_name: str) -> Database[Mapping[str, Any] | Any]:
    client = _clients.get(region_name, None)
    if client is None:
        raise Exception(f"Could not find mongo db client for region {region_name}")
    return client.get_database("admin")


def test_db():
    _logger.debug("testing database")
    _logger.debug(eu_client.list_database_names())
    _logger.debug(us_client.list_database_names())
    _logger.debug(eu_client.get_database("admin").songs.find_one())
    _logger.debug("test over")


def save_song(region_name: str, song_id: int, song_data: bytes):
    database = get_database(region_name)
    database.songs.insert_one({"id": song_id, "bitstream": song_data})


def get_song(region_name: str, song_id: int) -> bytes:
    database = get_database(region_name)
    return database.songs.fetch_one({"id": song_id}).get("bitstream")


def init_db():
    _create_collections()


def _create_collections():
    for client in (eu_client, us_client):
        _create_collection(client)


def _create_collection(client: MongoClient):
    try:
        client.get_database("admin").create_collection("songs")
        _logger.debug(f"Created collection 'songs' for client {client}")
    except CollectionInvalid:
        _logger.debug(f"Collection 'songs' already exists for client {client}")