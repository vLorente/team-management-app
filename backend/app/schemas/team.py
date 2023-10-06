# from typing import List
from pydantic import BaseModel, UUID4


# Shared properties
class TeamBase(BaseModel):
    name: str
    location: str


# Properties to reveive on item creation
class TeamCreate(TeamBase):
    pass


# Properties to receive on item update
class TeamUpdate(TeamBase):
    pass


# Properties shared by models stored in DB
class TeamInDBBase(TeamBase):
    id: UUID4
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
