from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
import models, schemas, crud
from database import engine, get_db

# Create the database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Allow our frontend webpage to talk to our backend server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 1. Get all jobs
@app.get("/jobs", response_model=List[schemas.JobResponse])
def read_jobs(db: Session = Depends(get_db)):
    return crud.get_jobs(db)

# 2. Create a new job
@app.post("/jobs", response_model=schemas.JobResponse)
def create_job(job: schemas.JobCreate, db: Session = Depends(get_db)):
    return crud.create_job(db=db, job=job)

# 3. Update job status
@app.put("/jobs/{job_id}", response_model=schemas.JobResponse)
def update_job(job_id: int, status_update: schemas.JobBase, db: Session = Depends(get_db)):
    db_job = crud.update_job_status(db, job_id=job_id, status=status_update.status)
    if not db_job:
        raise HTTPException(status_code=404, detail="Job not found")
    return db_job

# 4. Delete a job
@app.delete("/jobs/{job_id}")
def delete_job(job_id: int, db: Session = Depends(get_db)):
    success = crud.delete_job(db, job_id=job_id)
    if not success:
        raise HTTPException(status_code=404, detail="Job not found")
    return {"message": "Job deleted successfully"}
