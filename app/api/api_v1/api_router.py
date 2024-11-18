from fastapi import APIRouter
from app.api.api_v1.endpoints import auth, freelancers, clients, projects, invoices

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(freelancers.router, prefix="/freelancers", tags=["freelancers"])
api_router.include_router(clients.router, prefix="/clients", tags=["clients"])
api_router.include_router(projects.router, prefix="/projects", tags=["projects"])
api_router.include_router(invoices.router, prefix="/invoices", tags=["invoices"])
