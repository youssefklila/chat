# schemas/cell_schema.py

from pydantic import BaseModel
from typing import Optional

class CellBase(BaseModel):
    name: str
    description: Optional[str] = None
    info: Optional[str] = None
    is_active: bool

    class Config:
        orm_mode = True  # This allows Pydantic models to work with ORM models like SQLAlchemy.

class CellCreate(CellBase):
    site_id: int
    user_id: int

class CellUpdate(CellBase):
    site_id: Optional[int] = None
    user_id: Optional[int] = None

class CellOut(CellBase):
    id: int
    site_id: int
    user_id: int

    class Config:
        orm_mode = True
