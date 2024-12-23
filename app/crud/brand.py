from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from ..models import Brand
from ..schemas import BrandCreate, BrandBase

async def get_brands(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(Brand).offset(skip).limit(limit))
    return result.scalars().all()

async def get_brand(db: AsyncSession, brand_id: int):
    result = await db.execute(select(Brand).filter(Brand.id == brand_id))
    return result.scalars().first()

async def create_brand(db: AsyncSession, brand: BrandCreate):
    db_brand = Brand(**brand.dict())
    db.add(db_brand)
    await db.commit()
    await db.refresh(db_brand)
    return db_brand

async def update_brand(db: AsyncSession, brand_id: int, brand: BrandBase):
    db_brand = await get_brand(db, brand_id)
    for key, value in brand.dict().items():
        setattr(db_brand, key, value)
    await db.commit()
    await db.refresh(db_brand)
    return db_brand

async def delete_brand(db: AsyncSession, brand_id: int):
    db_brand = await get_brand(db, brand_id)
    await db.delete(db_brand)
    await db.commit()
    return db_brand
