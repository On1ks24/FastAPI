from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from ..models import Car
from ..schemas import CarCreate, CarBase

async def get_cars(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(Car).offset(skip).limit(limit))
    return result.scalars().all()

async def get_car(db: AsyncSession, car_id: int):
    result = await db.execute(select(Car).filter(Car.id == car_id))
    return result.scalars().first()

async def create_car(db: AsyncSession, car: CarCreate):
    db_car = Car(**car.dict())
    db.add(db_car)
    await db.commit()
    await db.refresh(db_car)
    return db_car

async def update_car(db: AsyncSession, car_id: int, car: CarBase):
    db_car = await get_car(db, car_id)
    for key, value in car.dict().items():
        setattr(db_car, key, value)
    await db.commit()
    await db.refresh(db_car)
    return db_car

async def delete_car(db: AsyncSession, car_id: int):
    db_car = await get_car(db, car_id)
    await db.delete(db_car)
    await db.commit()
    return db_car
