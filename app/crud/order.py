from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from ..models import Order
from ..schemas import OrderCreate, OrderBase

async def get_orders(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(Order).offset(skip).limit(limit))
    return result.scalars().all()

async def get_order(db: AsyncSession, order_id: int):
    result = await db.execute(select(Order).filter(Order.id == order_id))
    return result.scalars().first()

async def create_order(db: AsyncSession, order: OrderCreate):
    db_order = Order(**order.dict())
    db.add(db_order)
    await db.commit()
    await db.refresh(db_order)
    return db_order

async def update_order(db: AsyncSession, order_id: int, order: OrderBase):
    db_order = await get_order(db, order_id)
    for key, value in order.dict().items():
        setattr(db_order, key, value)
    await db.commit()
    await db.refresh(db_order)
    return db_order

async def delete_order(db: AsyncSession, order_id: int):
    db_order = await get_order(db, order_id)
    await db.delete(db_order)
    await db.commit()
    return db_order
