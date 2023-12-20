import os
import sqlalchemy

from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker


def __get_url():
    return "postgresql://%s:%s@%s/%s" % (
        os.environ.get("POSTGRES_USER", "POSTGRES_USER"),
        os.environ.get("POSTGRES_PASSWORD", "POSTGRES_PASSWORD"),
        os.environ.get("POSTGRES_HOST", "database"),
        os.environ.get("POSTGRES_DB", "POSTGRES_DB"),
    )

def __db_session():
    db_url = __get_url()
    engine = sqlalchemy.create_engine(db_url)
    return sessionmaker(bind=engine, autoflush=True)()


@contextmanager
def get_session():
    with __db_session() as session:
        yield session
