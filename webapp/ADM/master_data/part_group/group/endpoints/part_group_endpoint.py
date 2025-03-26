from fastapi import APIRouter, Depends, HTTPException
from typing import List
from dependency_injector.wiring import inject, Provide
from webapp.ADM.master_data.part_group.group.schemas.part_group_schema import PartGroupCreate, PartGroupUpdate, PartGroupResponse
from webapp.ADM.master_data.part_group.group.services.part_group_service import PartGroupService
from webapp.containers import Container

router = APIRouter()

@router.get("/", response_model=List[PartGroupResponse])
@inject
def get_part_groups(
    part_group_service: PartGroupService = Depends(Provide[Container.part_group_service])
):
    return part_group_service.get_all_part_groups()

@router.get("/{part_group_id}", response_model=PartGroupResponse)
@inject
def get_part_group(
    part_group_id: int,
    part_group_service: PartGroupService = Depends(Provide[Container.part_group_service])
):
    part_group = part_group_service.get_part_group_by_id(part_group_id)
    if not part_group:
        raise HTTPException(status_code=404, detail="Part group not found")
    return part_group

@router.post("/", response_model=PartGroupResponse)
@inject
def create_part_group(
    part_group_data: PartGroupCreate,
    part_group_service: PartGroupService = Depends(Provide[Container.part_group_service])
):
    return part_group_service.add_part_group(**part_group_data.dict())

@router.put("/{part_group_id}", response_model=PartGroupResponse)
@inject
def update_part_group(
    part_group_id: int, part_group_data: PartGroupUpdate,
    part_group_service: PartGroupService = Depends(Provide[Container.part_group_service])
):
    return part_group_service.update_part_group(part_group_id, **part_group_data.dict())

@router.delete("/{part_group_id}")
@inject
def delete_part_group(
    part_group_id: int,
    part_group_service: PartGroupService = Depends(Provide[Container.part_group_service])
):
    part_group_service.delete_part_group(part_group_id)
    return {"message": "Part group deleted successfully"}
