from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from ..models import Service
from ..schemas import ServiceCreate, ServiceBase

async def get_services(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(Service).offset(skip).limit(limit))
    return result.scalars().all()

async def get_service(db: AsyncSession, service_id: int):
    result = await db.execute(select(Service).filter(Service.id == service_id))
    return result.scalars().first()

async def create_service(db: AsyncSession, service: ServiceCreate):
    db_service = Service(**service.dict())
    db.add(db_service)
    await db.commit()
    await db.refresh(db_service)
    return db_service

async def update_service(db: AsyncSession, service_id: int, service: ServiceBase):
    db_service = await get_service(db, service_id)
    for key, value in service.dict().items():
        setattr(db_service, key, value)
    await db.commit()
    await db.refresh(db_service)
    return db_service

async def delete_service(db: AsyncSession, service_id: int):
    db_service = await get_service(db, service_id)
    await db.delete(db_service)
    await db.commit()
    return db_service
