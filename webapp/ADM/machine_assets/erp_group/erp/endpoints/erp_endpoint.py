# endpoints/erp_group_endpoint.py

from fastapi import APIRouter, Depends, HTTPException
from typing import List
from dependency_injector.wiring import inject, Provide
from webapp.ADM.machine_assets.erp_group.erp.schemas.erp_schema import ERPGroupCreate, ERPGroupUpdate, ERPGroupResponse
from webapp.ADM.machine_assets.erp_group.erp.services.erp_service import ERPGroupService
from webapp.containers import Container

router = APIRouter()

@router.get("/", response_model=List[ERPGroupResponse])
@inject
def get_erp_groups(
    erp_group_service: ERPGroupService = Depends(Provide[Container.erp_group_service])
):
    return erp_group_service.get_all_erp_groups()

@router.get("/{erp_group_id}", response_model=ERPGroupResponse)
@inject
def get_erp_group(
    erp_group_id: int,
    erp_group_service: ERPGroupService = Depends(Provide[Container.erp_group_service])
):
    erp_group = erp_group_service.get_erp_group_by_id(erp_group_id)
    if not erp_group:
        raise HTTPException(status_code=404, detail="ERP Group not found")
    return erp_group

@router.post("/", response_model=ERPGroupResponse)
@inject
def create_erp_group(
    erp_group_data: ERPGroupCreate,
    erp_group_service: ERPGroupService = Depends(Provide[Container.erp_group_service])
):
    return erp_group_service.add_erp_group(erp_group_data)

@router.put("/{erp_group_id}", response_model=ERPGroupResponse)
@inject
def update_erp_group(
    erp_group_id: int, erp_group_data: ERPGroupUpdate,
    erp_group_service: ERPGroupService = Depends(Provide[Container.erp_group_service])
):
    return erp_group_service.update_erp_group(erp_group_id, **erp_group_data.dict())

@router.delete("/{erp_group_id}")
@inject
def delete_erp_group(
    erp_group_id: int,
    erp_group_service: ERPGroupService = Depends(Provide[Container.erp_group_service])
):
    erp_group_service.delete_erp_group(erp_group_id)
    return {"message": "ERP Group deleted successfully"}
