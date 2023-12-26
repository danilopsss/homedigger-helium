from collections import namedtuple


_status = namedtuple("Status", ["message", "code"])


class ApiResponse:
    CREATED = _status("CREATED", 201)
