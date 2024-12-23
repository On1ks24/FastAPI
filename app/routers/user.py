from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from ..database import get_db
from ..schemas import UserCreate, UserBase, User
from ..crud import get_users, get_user, create_user, update_user, delete_user
from typing import List

router = APIRouter()

@router.post("/", response_model=User)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await create_user(db=db, user=user)

@router.get("/", response_model=List[User])
async def read_users(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    users = await get_users(db, skip=skip, limit=limit)
    return users

@router.get("/{user_id}", response_model=User)
async def read_user(user_id: int, db: AsyncSession = Depends(get_db)):
    db_user = await get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.put("/{user_id}", response_model=User)
async def update_user(user_id: int, user: UserBase, db: AsyncSession = Depends(get_db)):
    db_user = await update_user(db, user_id=user_id, user=user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.delete("/{user_id}", response_model=User)
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db)):
    db_user = await delete_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
