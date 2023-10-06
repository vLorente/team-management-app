from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.team import TeamCreate, TeamResponse, TeamUpdate
from app.db.crud.crud_team import crud_team
from app.db.setup import get_session
from app.serializer.team import prepare_team
from app.enums.exceptions import HttpMsgExceptions


router = APIRouter()


@router.get('', response_model=List[TeamResponse],
            status_code=status.HTTP_200_OK)
async def read_teams(skip: int = 0, limit: int = 100,
                     session: AsyncSession = Depends(get_session)) -> List[TeamResponse]: # noqa
    results = await crud_team.get_multi(session, skip=skip, limit=limit)
    response: List[TeamResponse] = [prepare_team(x) for x in results]
    return response


@router.get('/{team_id}', response_model=TeamResponse, status_code=status.HTTP_200_OK)
async def read_team(team_id: str,
                    session: AsyncSession = Depends(get_session)) -> TeamResponse:
    result = await crud_team.get(session, team_id)

    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=HttpMsgExceptions.ITEM_NOT_FOUND.value)

    return prepare_team(result)


@router.post('', response_model=TeamResponse, status_code=status.HTTP_201_CREATED)
async def create_team(team: TeamCreate,
                      session: AsyncSession = Depends(get_session)) -> TeamResponse:
    try:
        result = await crud_team.create(session, payload=team)

        return prepare_team(result)
    except Exception as e:
        await session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Error creando el equipo: {str(e)}'
        )


@router.patch('/{team_id}', response_model=TeamResponse, status_code=status.HTTP_200_OK)
async def update_team(team_id: str, team: TeamUpdate,
                      session: AsyncSession = Depends(get_session)) -> TeamResponse:
    db_team = await crud_team.get(session, team_id)
    if not db_team:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=HttpMsgExceptions.ITEM_NOT_FOUND.value)

    result = await crud_team.update(session, db_team, team)

    return prepare_team(result)
