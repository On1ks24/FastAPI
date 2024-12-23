from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from ..database import get_db
from ..schemas import OrderServiceCreate, OrderServiceBase, OrderService
from ..crud import get_order_services, get_order_service, create_order_service, update_order_service, delete_order_service
from typing import List

router = APIRouter()

@router.post("/", response_model=OrderService)
async def create_order_service(order_service: OrderServiceCreate, db: AsyncSession = Depends(get_db)):
    return await create_order_service(db=db, order_service=order_service)

@router.get("/", response_model=List[OrderService])
async def read_order_services(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    order_services = await get_order_services(db, skip=skip, limit=limit)
    return order_services

@router.get("/{order_service_id}", response_model=OrderService)
async def read_order_service(order_service_id: int, db: AsyncSession = Depends(get_db)):
    db_order_service = await get_order_service(db, order_service_id=order_service_id)
    if db_order_service is None:
        raise HTTPException(status_code=404, detail="OrderService not found")
    return db_order_service

@router.put("/{order_service_id}", response_model=OrderService)
async def update_order_service(order_service_id: int, order_service: OrderServiceBase, db: AsyncSession = Depends(get_db)):
    db_order_service = await update_order_service(db, order_service_id=order_service_id, order_service=order_service)
    if db_order_service is None:
        raise HTTPException(status_code=404, detail="OrderService not found")
    return db_order_service

@router.delete("/{order_service_id}", response_model=OrderService)
async def delete_order_service(order_service_id: int, db: AsyncSession = Depends(get_db)):
    db_order_service = await delete_order_service(db, order_service_id=order_service_id)
    if db_order_service is None:
        raise HTTPException(status_code=404, detail="OrderService not found")
    return db_order_service
