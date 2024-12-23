from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from ..database import get_db
from ..schemas import CarCreate, CarBase, Car
from ..crud import get_cars, get_car, create_car, update_car, delete_car
from typing import List

router = APIRouter()

@router.post("/", response_model=Car)
async def create_car(car: CarCreate, db: AsyncSession = Depends(get_db)):
    return await create_car(db=db, car=car)

@router.get("/", response_model=List[Car])
async def read_cars(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    cars = await get_cars(db, skip=skip, limit=limit)
    return cars

@router.get("/{car_id}", response_model=Car)
async def read_car(car_id: int, db: AsyncSession = Depends(get_db)):
    db_car = await get_car(db, car_id=car_id)
    if db_car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return db_car

@router.put("/{car_id}", response_model=Car)
async def update_car(car_id: int, car: CarBase, db: AsyncSession = Depends(get_db)):
    db_car = await update_car(db, car_id=car_id, car=car)
    if db_car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return db_car

@router.delete("/{car_id}", response_model=Car)
async def delete_car(car_id: int, db: AsyncSession = Depends(get_db)):
    db_car = await delete_car(db, car_id=car_id)
    if db_car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return db_car
