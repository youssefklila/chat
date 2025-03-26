from fastapi import APIRouter, Depends, HTTPException
from typing import List
from dependency_injector.wiring import inject, Provide
from webapp.ADM.master_data.workplan_data.workplan_type.schemas.workplan_type_schema import (
    WorkPlanTypeCreate,
    WorkPlanTypeUpdate,
    WorkPlanTypeResponse,
)
from webapp.ADM.master_data.workplan_data.workplan_type.services.workplan_type_service import WorkPlanTypeService
from webapp.containers import Container

router = APIRouter()

@router.get("/", response_model=List[WorkPlanTypeResponse])
@inject
def get_workplan_types(
    workplan_type_service: WorkPlanTypeService = Depends(Provide[Container.workplan_type_service])
):
    return workplan_type_service.get_all_workplan_types()

@router.get("/{workplan_type_id}", response_model=WorkPlanTypeResponse)
@inject
def get_workplan_type(
    workplan_type_id: int,
    workplan_type_service: WorkPlanTypeService = Depends(Provide[Container.workplan_type_service])
):
    workplan_type = workplan_type_service.get_workplan_type_by_id(workplan_type_id)
    if not workplan_type:
        raise HTTPException(status_code=404, detail="WorkPlanType not found")
    return workplan_type

@router.post("/", response_model=WorkPlanTypeResponse)
@inject
def create_workplan_type(
    workplan_type_data: WorkPlanTypeCreate,
    workplan_type_service: WorkPlanTypeService = Depends(Provide[Container.workplan_type_service])
):
    return workplan_type_service.add_workplan_type(**workplan_type_data.dict())

@router.put("/{workplan_type_id}", response_model=WorkPlanTypeResponse)
@inject
def update_workplan_type(
    workplan_type_id: int,
    workplan_type_data: WorkPlanTypeUpdate,
    workplan_type_service: WorkPlanTypeService = Depends(Provide[Container.workplan_type_service])
):
    return workplan_type_service.update_workplan_type(workplan_type_id, **workplan_type_data.dict())

@router.delete("/{workplan_type_id}")
@inject
def delete_workplan_type(
    workplan_type_id: int,
    workplan_type_service: WorkPlanTypeService = Depends(Provide[Container.workplan_type_service])
):
    workplan_type_service.delete_workplan_type(workplan_type_id)
    return {"message": "WorkPlanType deleted successfully"}
