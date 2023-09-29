from typing import List
from fastapi import APIRouter, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.team import TeamResponse


router = APIRouter()


@router.get('', response_model=TeamResponse, status_code=status.HTTP_200_OK)
def read_teams(
    session: AsyncSession,
    skip: int = 0,
    limit: int = 100,
) -> List[TeamResponse]:
    pass
