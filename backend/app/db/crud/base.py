from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from pydantic import BaseModel

from app.db.setup import Base


ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type):
        self.model = model

    async def create(self,
                     session: AsyncSession, *,
                     payload: CreateSchemaType) -> ModelType:
        obj = self.model(**payload.model_dump())
        session.add(obj)
        await self.session.commit()
        await self.session.refresh(obj)
        return obj

    async def get(self, session: AsyncSession, id: Any) -> Optional[ModelType]:
        return await session.get(self.model, id)

    async def get_multi(self,
                        session: AsyncSession, *,
                        skip: int = 0,
                        limit: int = 100) -> List[ModelType]:
        query = select(self.model).offset(skip).limit(limit)
        result = await session.execute(query)
        return result.scalars().all()

    async def update(self,
                     session: AsyncSession,
                     db_obj: ModelType,
                     payload: Union[UpdateSchemaType, Dict[str, Any]]) -> ModelType:
        for key, value in payload.model_dump().items():
            setattr(db_obj, key, value)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj

    async def remove(self, session: AsyncSession, *, id: Any) -> ModelType | None:
        obj = await self.get(session, id)
        if obj:
            session.delete(obj)
            await session.commit()
            return obj
        return None
