from fastapi import FastAPI
from app.api.api_v1.api_router import api_router  
from app.core.config import settings
from app.db.session import SessionLocal, engine
from app.models import user, freelancer, client, project, invoice
from app.db.base_class import Base  # Correcting the import path

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME)

# Include router
app.include_router(api_router)