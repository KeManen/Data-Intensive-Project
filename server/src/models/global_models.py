import decimal

from sqlalchemy import String, DECIMAL, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from models.common import DbModelBase


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
