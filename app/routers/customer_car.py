from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from ..database import get_db
from ..schemas import CustomerCarCreate, CustomerCarBase, CustomerCar
from ..crud import get_customer_cars, get_customer_car, create_customer_car, update_customer_car, delete_customer_car
from typing import List

router = APIRouter()

@router.post("/", response_model=CustomerCar)
async def create_customer_car(customer_car: CustomerCarCreate, db: AsyncSession = Depends(get_db)):
    return await create_customer_car(db=db, customer_car=customer_car)

@router.get("/", response_model=List[CustomerCar])
async def read_customer_cars(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    customer_cars = await get_customer_cars(db, skip=skip, limit=limit)
    return customer_cars

@router.get("/{customer_car_id}", response_model=CustomerCar)
async def read_customer_car(customer_car_id: int, db: AsyncSession = Depends(get_db)):
    db_customer_car = await get_customer_car(db, customer_car_id=customer_car_id)
    if db_customer_car is None:
        raise HTTPException(status_code=404, detail="CustomerCar not found")
    return db_customer_car

@router.put("/{customer_car_id}", response_model=CustomerCar)
async def update_customer_car(customer_car_id: int, customer_car: CustomerCarBase, db: AsyncSession = Depends(get_db)):
    db_customer_car = await update_customer_car(db, customer_car_id=customer_car_id, customer_car=customer_car)
    if db_customer_car is None:
        raise HTTPException(status_code=404, detail="CustomerCar not found")
    return db_customer_car

@router.delete("/{customer_car_id}", response_model=CustomerCar)
async def delete_customer_car(customer_car_id: int, db: AsyncSession = Depends(get_db)):
    db_customer_car = await delete_customer_car(db, customer_car_id=customer_car_id)
    if db_customer_car is None:
        raise HTTPException(status_code=404, detail="CustomerCar not found")
    return db_customer_car
