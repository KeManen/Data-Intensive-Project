from sqlalchemy.orm import declared_attr, Mapped, mapped_column


class DbModelBase:

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    @declared_attr
    def __tablename__(self):
        return self.__name__
