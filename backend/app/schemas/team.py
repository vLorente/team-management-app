# from typing import List
from pydantic import BaseModel


# Shared properties
class TeamBase(BaseModel):
    name: str = None
    location: str


# Properties to reveive on item creation
class TeamCreate(TeamBase):
    pass


# Properties to receive on item update
class TeamUpdate(TeamBase):
    pass


# Properties shared by models stored in DB
class TeamInDBBase(TeamBase):
    id: str
    name: str
    location: str

    class Config:
        from_attributes = True


# Properties to return to client
class TeamResponse(TeamInDBBase):
    pass


# Properties stored in DB
class TeamInDB(TeamInDBBase):
    pass
