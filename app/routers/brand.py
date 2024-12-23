from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from ..database import get_db
from ..schemas import BrandCreate, BrandBase, Brand
from ..crud import get_brands, get_brand, create_brand, update_brand, delete_brand
from typing import List

router = APIRouter()

@router.post("/", response_model=Brand)
async def create_brand(brand: BrandCreate, db: AsyncSession = Depends(get_db)):
    return await create_brand(db=db, brand=brand)

@router.get("/", response_model=List[Brand])
async def read_brands(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    brands = await get_brands(db, skip=skip, limit=limit)
    return brands

@router.get("/{brand_id}", response_model=Brand)
async def read_brand(brand_id: int, db: AsyncSession = Depends(get_db)):
    db_brand = await get_brand(db, brand_id=brand_id)
    if db_brand is None:
        raise HTTPException(status_code=404, detail="Brand not found")
    return db_brand

@router.put("/{brand_id}", response_model=Brand)
async def update_brand(brand_id: int, brand: BrandBase, db: AsyncSession = Depends(get_db)):
    db_brand = await update_brand(db, brand_id=brand_id, brand=brand)
    if db_brand is None:
        raise HTTPException(status_code=404, detail="Brand not found")
    return db_brand

@router.delete("/{brand_id}", response_model=Brand)
async def delete_brand(brand_id: int, db: AsyncSession = Depends(get_db)):
    db_brand = await delete_brand(db, brand_id=brand_id)
    if db_brand is None:
        raise HTTPException(status_code=404, detail="Brand not found")
    return db_brand
