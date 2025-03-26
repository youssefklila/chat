from pydantic import BaseModel
from typing import Optional

class WorkPlanTypeBase(BaseModel):
    name: str
    description: Optional[str] = None

class WorkPlanTypeCreate(WorkPlanTypeBase):
    pass

class WorkPlanTypeUpdate(WorkPlanTypeBase):
    pass

class WorkPlanTypeResponse(WorkPlanTypeBase):
    id: int

    class Config:
        orm_mode = True
