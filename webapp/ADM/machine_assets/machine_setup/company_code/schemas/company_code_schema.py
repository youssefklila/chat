# schemas/company_code_schema.py

from pydantic import BaseModel
from typing import Optional

class CompanyCodeCreate(BaseModel):
    user_id: int
    client_id: Optional[int] = None
    name: str
    description: Optional[str] = None

class CompanyCodeUpdate(BaseModel):
    user_id: Optional[int] = None
    client_id: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None

class CompanyCodeOut(BaseModel):
    id: int
    user_id: int
    client_id: Optional[int] = None
    name: str
    description: Optional[str] = None

    class Config:
        orm_mode = True
