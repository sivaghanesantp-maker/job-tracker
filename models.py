from sqlalchemy import Column, Integer, String, Date
from database import Base

class Job(Base):
    # 1. Tell SQLAlchemy what to name the table in PostgreSQL
    __tablename__ = "jobs"

    # 2. Define the columns of our table
    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String, nullable=False)
    job_title = Column(String, nullable=False)
    status = Column(String, default="Applied")  # e.g., Applied, Interviewing, Offered, Rejected
    application_date = Column(Date, nullable=True)
    job_url = Column(String, nullable=True)
    notes = Column(String, nullable=True)
