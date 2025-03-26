from fastapi import APIRouter, Depends, HTTPException
from typing import List
from dependency_injector.wiring import inject, Provide

from webapp.ADM.master_data.workplan_data.workplan.schemas.workplan_schema import WorkPlanResponse, WorkPlanCreate, \
    WorkPlanUpdate
from webapp.ADM.master_data.workplan_data.workplan.services.workplan_service import WorkPlanService
from webapp.containers import Container

router = APIRouter()

@router.get("/", response_model=List[WorkPlanResponse])
@inject
def get_work_plans(
    work_plan_service: WorkPlanService = Depends(Provide[Container.work_plan_service])
):
    return work_plan_service.get_all_work_plans()

@router.get("/{work_plan_id}", response_model=WorkPlanResponse)
@inject
def get_work_plan(
    work_plan_id: int,
    work_plan_service: WorkPlanService = Depends(Provide[Container.work_plan_service])
):
    work_plan = work_plan_service.get_work_plan_by_id(work_plan_id)
    if not work_plan:
        raise HTTPException(status_code=404, detail="Work Plan not found")
    return work_plan

@router.post("/", response_model=WorkPlanResponse)
@inject
def create_work_plan(
    work_plan_data: WorkPlanCreate,
    work_plan_service: WorkPlanService = Depends(Provide[Container.work_plan_service])
):
    return work_plan_service.add_work_plan(**work_plan_data.dict())

@router.put("/{work_plan_id}", response_model=WorkPlanResponse)
@inject
def update_work_plan(
    work_plan_id: int, work_plan_data: WorkPlanUpdate,
    work_plan_service: WorkPlanService = Depends(Provide[Container.work_plan_service])
):
    return work_plan_service.update_work_plan(work_plan_id, **work_plan_data.dict())

@router.delete("/{work_plan_id}")
@inject
def delete_work_plan(
    work_plan_id: int,
    work_plan_service: WorkPlanService = Depends(Provide[Container.work_plan_service])
):
    work_plan_service.delete_work_plan(work_plan_id)
    return {"message": "Work Plan deleted successfully"}
