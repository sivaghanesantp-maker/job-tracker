from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 1. Define our Database URL
# Format: postgresql://username:password@hostname:port/database_name
# Note: Since Docker is mapping port 5433 on your computer to 5432 in the container, we use 5433 here!
DATABASE_URL = "postgresql+psycopg2://my_user:my_secure_password@localhost:5433/job_tracker_database"

# 2. Create the Database Engine
engine = create_engine(DATABASE_URL)

# 3. Create a Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Create a Base class
# All our database tables (Models) will inherit from this Base class so SQLAlchemy knows about them.
Base = declarative_base()

# 5. Helper function to get a database connection session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
