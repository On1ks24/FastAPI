from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from ..models import CustomerCar
from ..schemas import CustomerCarCreate, CustomerCarBase

async def get_customer_cars(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(CustomerCar).offset(skip).limit(limit))
    return result.scalars().all()

async def get_customer_car(db: AsyncSession, customer_car_id: int):
    result = await db.execute(select(CustomerCar).filter(CustomerCar.id == customer_car_id))
    return result.scalars().first()

async def create_customer_car(db: AsyncSession, customer_car: CustomerCarCreate):
    db_customer_car = CustomerCar(**customer_car.dict())
    db.add(db_customer_car)
    await db.commit()
    await db.refresh(db_customer_car)
    return db_customer_car

async def update_customer_car(db: AsyncSession, customer_car_id: int, customer_car: CustomerCarBase):
    db_customer_car = await get_customer_car(db, customer_car_id)
    for key, value in customer_car.dict().items():
        setattr(db_customer_car, key, value)
    await db.commit()
    await db.refresh(db_customer_car)
    return db_customer_car

async def delete_customer_car(db: AsyncSession, customer_car_id: int):
    db_customer_car = await get_customer_car(db, customer_car_id)
    await db.delete(db_customer_car)
    await db.commit()
    return db_customer_car
