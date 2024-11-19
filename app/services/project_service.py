from sqlalchemy.orm import Session
from app.models.project import Project
from app.schemas.project import ProjectCreate
import logging

logger = logging.getLogger(__name__)


def get_project(db: Session, project_id: int):
    return db.query(Project).filter(Project.id == project_id).first()

def get_projects(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Project).offset(skip).limit(limit).all()

def create_project(db: Session, project: ProjectCreate):
    try:
        db_project = Project(
            name=project.name,
            field=project.field,
            description=project.description,
            budget=project.budget
        )
        db.add(db_project)
        db.commit()
        db.refresh(db_project)
        return db_project
    except Exception as e:
        logger.error(f"Error creating project: {e}")
        db.rollback()
        raise
