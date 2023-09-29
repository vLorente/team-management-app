# from typing import List
from pydantic import BaseModel


class TeamResponse(BaseModel):
    id: str
    name: str
    location: str
    # players: List[int]
