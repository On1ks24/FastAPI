from fastapi import FastAPI
from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel
from fastapi.security import OAuth2PasswordBearer
from .database import engine, Base
from .routers import brand_router, car_router, customer_car_router, service_router, order_router, user_router, order_service_router, auth_router

app = FastAPI(
    title="My API",
    description="API for managing brands, cars, customer cars, services, orders, users, and order services",
    version="1.0.0",
    openapi_url="/api/v1/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
)

Base.metadata.create_all(bind=engine)

app.include_router(brand_router, prefix="/brands", tags=["brands"])
app.include_router(car_router, prefix="/cars", tags=["cars"])
app.include_router(customer_car_router, prefix="/customer_cars", tags=["customer_cars"])
app.include_router(service_router, prefix="/services", tags=["services"])
app.include_router(order_router, prefix="/orders", tags=["orders"])
app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(order_service_router, prefix="/order_services", tags=["order_services"])
app.include_router(auth_router, prefix="/auth", tags=["auth"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app.openapi_schema = {
    "openapi": "3.0.0",
    "info": {
        "title": "My API",
        "version": "1.0.0",
    },
    "components": {
        "securitySchemes": {
            "OAuth2PasswordBearer": {
                "type": "oauth2",
                "flows": {
                    "password": {
                        "tokenUrl": "token",
                        "scopes": {},
                    },
                },
            },
        },
    },
    "security": [{"OAuth2PasswordBearer": []}],
}
