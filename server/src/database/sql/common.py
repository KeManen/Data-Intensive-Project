from contextlib import contextmanager
from typing import ContextManager

from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker, Session


class ConnectionManager:

    def __init__(self, db_address: str, base_model):
        self.engine = create_engine(db_address, echo=False)
        self.session = sessionmaker()
        self.session.configure(bind=self.engine)
        base_model.metadata.create_all(self.engine)

    @contextmanager
    def session(self) -> ContextManager[Session]:
        context_session = self.session()
        try:
            context_session.expire_on_commit = False
            yield context_session
        except SQLAlchemyError:
            context_session.rollback()
        else:
            context_session.commit()
        finally:
            context_session.close()
