from flask import request
from ..schemas import UserAccessHistorySchema
from ..models.user_access_history import Events


def create_db_event(request: request, event: Events) -> dict:
    if not getattr(Events, event, None):
        raise ValueError(f"Event {event} is not a valid event")

    user_ah = UserAccessHistorySchema(
        event=event,
        ip=request.remote_addr,
        user_agent=request.headers["User-Agent"],
    ).model_dump()

    return {"access_history": [user_ah]}
