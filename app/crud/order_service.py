from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from ..models import OrderService
from ..schemas import OrderServiceCreate, OrderServiceBase

async def get_order_services(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(OrderService).offset(skip).limit(limit))
    return result.scalars().all()

async def get_order_service(db: AsyncSession, order_service_id: int):
    result = await db.execute(select(OrderService).filter(OrderService.id == order_service_id))
    return result.scalars().first()

async def create_order_service(db: AsyncSession, order_service: OrderServiceCreate):
    db_order_service = OrderService(**order_service.dict())
    db.add(db_order_service)
    await db.commit()
    await db.refresh(db_order_service)
    return db_order_service

async def update_order_service(db: AsyncSession, order_service_id: int, order_service: OrderServiceBase):
    db_order_service = await get_order_service(db, order_service_id)
    for key, value in order_service.dict().items():
        setattr(db_order_service, key, value)
    await db.commit()
    await db.refresh(db_order_service)
    return db_order_service

async def delete_order_service(db: AsyncSession, order_service_id: int):
    db_order_service = await get_order_service(db, order_service_id)
    await db.delete(db_order_service)
    await db.commit()
    return db_order_service
