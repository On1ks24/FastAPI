from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from ..database import get_db
from ..schemas import OrderCreate, OrderBase, Order
from ..crud import get_orders, get_order, create_order, update_order, delete_order
from typing import List

router = APIRouter()

@router.post("/", response_model=Order)
async def create_order(order: OrderCreate, db: AsyncSession = Depends(get_db)):
    return await create_order(db=db, order=order)

@router.get("/", response_model=List[Order])
async def read_orders(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    orders = await get_orders(db, skip=skip, limit=limit)
    return orders

@router.get("/{order_id}", response_model=Order)
async def read_order(order_id: int, db: AsyncSession = Depends(get_db)):
    db_order = await get_order(db, order_id=order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order

@router.put("/{order_id}", response_model=Order)
async def update_order(order_id: int, order: OrderBase, db: AsyncSession = Depends(get_db)):
    db_order = await update_order(db, order_id=order_id, order=order)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order

@router.delete("/{order_id}", response_model=Order)
async def delete_order(order_id: int, db: AsyncSession = Depends(get_db)):
    db_order = await delete_order(db, order_id=order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order
