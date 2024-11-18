from sqlalchemy.orm import Session
from app.models.user import User  # Example of a model to pre-load data
from app.core.security import get_password_hash

def init_db(db: Session) -> None:
    """
    Initialize the database with default data.
    """
    # Check if an admin user already exists
    admin_user = db.query(User).filter(User.email == "admin@example.com").first()
    if not admin_user:
        admin_user = User(
            email="admin@example.com",
            hashed_password=get_password_hash("admin"),
            is_superuser=True,
            is_active=True,
        )
        db.add(admin_user)
        db.commit()
        db.refresh(admin_user)
