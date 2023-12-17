from database.nosql import mongo_connection
from database.sql import global_connection, regional_connection
from models.api.audio import DuplicatedSong
from models.database.global_models import GlobalSong


def calculate_new_duplicates() -> list[DuplicatedSong]:
    duplicated_songs = []
    all_songs = global_connection.get_all_songs()
    song_regions = _build_song_regions(all_songs)
    for song_group in song_regions:
        duplicates = _calculate_duplicates(song_group)
        duplicated_songs.extend(duplicates)
    return duplicated_songs


def _build_song_regions(all_songs: list[GlobalSong]) -> {int: set[int]}:
    song_regions: {str: (int, list[GlobalSong])} = {}
    for song in all_songs:
        if song.name not in song_regions:
            song_regions[song.name] = []
        if song.is_primary_region:
            song_regions[song.name].insert(0, song)
        else:
            song_regions[song.name].append(song)
    return song_regions


def _calculate_duplicates(songs: list[GlobalSong]) -> list[DuplicatedSong]:
    duplicated: list[DuplicatedSong] = []
    already_duplicated = (song.region.name for song in songs)
    song_data: bytes | None = None
    for region in regional_connection.get_song_duplication_regions(songs[0]):
        if region not in already_duplicated:
            if song_data is None:
                song_data = mongo_connection.get_song(songs[0].region, songs[0].id)
            region_id = global_connection.get_region_from_name(region).id
            global_connection.insert_song(songs[0].name, region_id, False)
            mongo_connection.save_song(region, songs[0].id, song_data)
            duplicated.append(DuplicatedSong(name=songs[0].name, region_code=region))
    return duplicated
