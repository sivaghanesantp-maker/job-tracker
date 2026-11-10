from sqlalchemy.orm import Session
import models, schemas

# 1. Fetch all jobs from the database
def get_jobs(db: Session):
    return db.query(models.Job).all()

# 2. Save a new job to the database
def create_job(db: Session, job: schemas.JobCreate):
    db_job = models.Job(
        company_name=job.company_name,
        job_title=job.job_title,
        status=job.status,
        application_date=job.application_date,
        job_url=job.job_url,
        notes=job.notes
    )
    db.add(db_job)
    db.commit()      # Permanently save it!
    db.refresh(db_job) # Get the newly generated ID
    return db_job

# 3. Update an existing job's status
def update_job_status(db: Session, job_id: int, status: str):
    db_job = db.query(models.Job).filter(models.Job.id == job_id).first()
    if db_job:
        db_job.status = status
        db.commit()
        db.refresh(db_job)
    return db_job

# 4. Delete a job from the database
def delete_job(db: Session, job_id: int):
    db_job = db.query(models.Job).filter(models.Job.id == job_id).first()
    if db_job:
        db.delete(db_job)
        db.commit()
        return True
    return False
