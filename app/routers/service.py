from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from ..database import get_db
from ..schemas import ServiceCreate, ServiceBase, Service
from ..crud import get_services, get_service, create_service, update_service, delete_service
from typing import List

router = APIRouter()

@router.post("/", response_model=Service)
async def create_service(service: ServiceCreate, db: AsyncSession = Depends(get_db)):
    return await create_service(db=db, service=service)

@router.get("/", response_model=List[Service])
async def read_services(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    services = await get_services(db, skip=skip, limit=limit)
    return services

@router.get("/{service_id}", response_model=Service)
async def read_service(service_id: int, db: AsyncSession = Depends(get_db)):
    db_service = await get_service(db, service_id=service_id)
    if db_service is None:
        raise HTTPException(status_code=404, detail="Service not found")
    return db_service

@router.put("/{service_id}", response_model=Service)
async def update_service(service_id: int, service: ServiceBase, db: AsyncSession = Depends(get_db)):
    db_service = await update_service(db, service_id=service_id, service=service)
    if db_service is None:
        raise HTTPException(status_code=404, detail="Service not found")
    return db_service

@router.delete("/{service_id}", response_model=Service)
async def delete_service(service_id: int, db: AsyncSession = Depends(get_db)):
    db_service = await delete_service(db, service_id=service_id)
    if db_service is None:
        raise HTTPException(status_code=404, detail="Service not found")
    return db_service
