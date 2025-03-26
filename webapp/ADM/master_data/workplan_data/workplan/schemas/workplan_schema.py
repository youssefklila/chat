from pydantic import BaseModel
from typing import Optional
from datetime import date

class WorkPlanBase(BaseModel):
    state: str
    part_master_id: int
    workplan_description: Optional[str] = None
    valid_from: date
    valid_to: Optional[date] = None
    alternative_work_plan: Optional[str] = None
    infotext: Optional[str] = None
    locked_by: Optional[int] = None
    process_type: Optional[str] = None
    items: Optional[str] = None
    source_system: Optional[str] = None
    user_id: int
    edited_on: Optional[date] = None
    created_on: date
    erp_change_number: Optional[str] = None
    workplan_type_id: int

class WorkPlanCreate(WorkPlanBase):
    pass

class WorkPlanUpdate(WorkPlanBase):
    pass

class WorkPlanResponse(WorkPlanBase):
    id: int

    class Config:
        orm_mode = True
