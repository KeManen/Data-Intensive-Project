from sqlalchemy import String, ForeignKey, LargeBinary
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from models.database.common import DbModelBase


class RegionalModel(DbModelBase, DeclarativeBase):
    region_id: Mapped[int] = mapped_column()


class AccountType(RegionalModel):
    identifier: Mapped[str] = mapped_column(String(16))
    price: Mapped[int] = mapped_column()


class PictureFile(RegionalModel):
    encoding: Mapped[str] = mapped_column(String(8))
    data: Mapped[bytes] = mapped_column(LargeBinary)


class RegionalUser(RegionalModel):
    name: Mapped[str] = mapped_column(String(64))
    account_type_id: Mapped[int] = mapped_column(ForeignKey("AccountType.id"))

    account_type: Mapped["AccountType"] = relationship(lazy="joined")
    albums: Mapped[list["Album"]] = relationship(back_populates="artist_user")


class AlbumSong(RegionalModel):
    song_id: Mapped[int] = mapped_column(ForeignKey("Song.id"))
    album_id: Mapped[int] = mapped_column(ForeignKey("Album.id"))
    order: Mapped[int] = mapped_column()
    primary_release: Mapped[bool] = mapped_column()

    song: Mapped["Song"] = relationship(lazy="joined")
    album: Mapped["Album"] = relationship(back_populates="songs")


class Song(RegionalModel):
    name: Mapped[str] = mapped_column(String(128))
    track_length_ms: Mapped[int] = mapped_column()
    artist_user_id: Mapped[int] = mapped_column(ForeignKey("RegionalUser.id"))


class SongPlay(RegionalModel):
    global_song_id: Mapped[int] = mapped_column()
    user_id: Mapped[int] = mapped_column(ForeignKey("RegionalUser.id"))


class Album(RegionalModel):
    name: Mapped[str] = mapped_column(String(128))
    picture_file_id: Mapped[int] = mapped_column(ForeignKey("PictureFile.id"))
    artist_user_id: Mapped[int] = mapped_column(ForeignKey("RegionalUser.id"))

    picture_file: Mapped["PictureFile"] = relationship(lazy="joined")
    artist_user: Mapped["RegionalUser"] = relationship(back_populates="albums")
    songs: Mapped[list["AlbumSong"]] = relationship(back_populates="album")


class PlaylistSong(RegionalModel):
    song_id: Mapped[int] = mapped_column(ForeignKey("Song.id"))
    playlist_id: Mapped[int] = mapped_column(ForeignKey("Playlist.id"))
    order: Mapped[int] = mapped_column()

    song: Mapped["Song"] = relationship(lazy="joined")
    playlist: Mapped["Playlist"] = relationship(back_populates="songs")


class Playlist(RegionalModel):
    name: Mapped[str] = mapped_column(String(128))
    picture_file_id: Mapped[int] = mapped_column(ForeignKey("PictureFile.id"))
    is_private: Mapped[bool] = mapped_column()
    owner_user_id: Mapped[int] = mapped_column(ForeignKey("RegionalUser.id"))

    owner_user: Mapped["RegionalUser"] = relationship(lazy="joined")
    songs: Mapped[list["PlaylistSong"]] = relationship(back_populates="playlist")
