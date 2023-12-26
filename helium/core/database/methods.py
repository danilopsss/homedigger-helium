from collections import namedtuple
from helium.core.database.database import get_session


ModelPair = namedtuple("ModelPair", ["db_model", "schema"])


def save_model_to_db(function) -> dict:
    def wrapper(*args, **kwargs):
        data: ModelPair = function(*args, **kwargs)
        with get_session() as session:
            try:
                session.begin()
                session.add(data.db_model)
                session.commit()
            except Exception as e:
                raise e
        return data.schema

    return wrapper
