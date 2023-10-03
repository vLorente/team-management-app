from typing import List
from fastapi import APIRouter, Depends, status
# from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.team import TeamResponse
from app.db.crud.crud_team import team
from app.db.setup import async_session
from app.serializer.team import prepare_team


router = APIRouter()


@router.get('', response_model=List[TeamResponse], status_code=status.HTTP_200_OK)
def read_teams() -> List[TeamResponse]:
    results = team.get_multi(Depends[async_session])
    results = [prepare_team(x) for x in results]
    return results
