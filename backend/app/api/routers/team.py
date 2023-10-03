from typing import List
from fastapi import APIRouter, Depends, status

from app.schemas.team import TeamCreate, TeamResponse, TeamUpdate
from app.db.crud.crud_team import crud_team
from app.db.setup import async_session
from app.serializer.team import prepare_team


router = APIRouter()


@router.get('', response_model=List[TeamResponse],
            status_code=status.HTTP_200_OK)
async def read_teams(skip: int = 0, limit: int = 100) -> List[TeamResponse]:
    results = await crud_team.get_multi(Depends[async_session], skip=skip, limit=limit)
    results = [prepare_team(x) for x in results]
    return results


@router.get('/{team_id}', response_model=TeamResponse, status_code=status.HTTP_200_OK)
async def read_team(team_id: str) -> TeamResponse:
    result = await crud_team.get(Depends(async_session), team_id)

    return prepare_team(result)


@router.post('', response_model=TeamResponse, status_code=status.HTTP_201_CREATED)
async def create_team(team: TeamCreate) -> TeamResponse:
    result = await crud_team.create(Depends(async_session), team)

    return prepare_team(result)


@router.patch('/{team_id}', response_model=TeamResponse, status_code=status.HTTP_200_OK)
async def update_team(team_id: str, team: TeamUpdate) -> TeamResponse:
    db_team = await crud_team.get(Depends(async_session), team_id)
    result = await crud_team.update(Depends(async_session), db_team, team)

    return prepare_team(result)
