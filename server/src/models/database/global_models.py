from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from models.database.common import DbModelBase


class GlobalModel(DbModelBase, DeclarativeBase):
    pass


class Currency(GlobalModel):
    name: Mapped[str] = mapped_column(String(32))
    code: Mapped[str] = mapped_column(String(3))
    rate_to_usd: Mapped[int] = mapped_column()


class Region(GlobalModel):
    name: Mapped[str] = mapped_column(String(64))
    currency_id: Mapped[int] = mapped_column(ForeignKey("Currency.id"))
    currency: Mapped["Currency"] = relationship(lazy="joined")


class UserLogin(GlobalModel):
    name: Mapped[str] = mapped_column(String(64), unique=True)
    password_hash_salt: Mapped[str] = mapped_column(String(128))
    region_id: Mapped[int] = mapped_column(ForeignKey("Region.id"))

    region: Mapped["Region"] = relationship(lazy="joined")


class GlobalSong(GlobalModel):
    name: Mapped[str] = mapped_column(String(128))
    region_id: Mapped[int] = mapped_column(ForeignKey("Region.id"))
    region: Mapped["Region"] = relationship(lazy="joined")
    is_primary_region: Mapped[bool] = mapped_column()
