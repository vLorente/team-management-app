from uuid import uuid4
from pydantic import UUID4


def new_uuid() -> UUID4:
    return str(uuid4())
