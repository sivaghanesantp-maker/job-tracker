from pydantic import BaseModel, field_validator
from typing import Optional
from datetime import date
import re

# 1. Base schema containing shared fields & strict validation
class JobBase(BaseModel):
    company_name: str
    job_title: str
    status: Optional[str] = "Applied"
    application_date: Optional[date] = None
    job_url: Optional[str] = None
    notes: Optional[str] = None

    # Validator 1: Company Name rules
    @field_validator('company_name')
    @classmethod
    def validate_company_name(cls, value: str):
        cleaned = value.strip()
        if len(cleaned) < 2:
            raise ValueError("Company name must be at least 2 characters long.")
        if cleaned.isdigit():
            raise ValueError("Company name cannot consist only of numbers.")
        if not re.search(r'[a-zA-Z]', cleaned):
            raise ValueError("Company name must contain at least one letter.")
        return cleaned

    # Validator 2: Job Title rules (NO NUMBERS AT ALL)
    @field_validator('job_title')
    @classmethod
    def validate_job_title(cls, value: str):
        cleaned = value.strip()
        if len(cleaned) < 2:
            raise ValueError("Job title must be at least 2 characters long.")
        
        # Check if any digits (0-9) exist anywhere in the job title
        if re.search(r'\d', cleaned):
            raise ValueError("Job title cannot contain any numbers. Letters and punctuation only.")
            
        if not re.search(r'[a-zA-Z]', cleaned):
            raise ValueError("Job title must contain valid letters.")
            
        return cleaned


# 2. Schema used when CREATING a new job
class JobCreate(JobBase):
    pass


# 3. Schema used when RETURNING a job to the user/frontend
class JobResponse(JobBase):
    id: int

    class Config:
        from_attributes = True
