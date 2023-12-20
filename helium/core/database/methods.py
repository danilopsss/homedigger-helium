from homedigger.core.database import get_session


def save_model_to_db(function):
    def wrapper(*args, **kwargs):
        data = function(*args, **kwargs)
        with get_session() as session:
            session.begin()
            session.add(data)
            session.commit()
        return data
    return wrapper
