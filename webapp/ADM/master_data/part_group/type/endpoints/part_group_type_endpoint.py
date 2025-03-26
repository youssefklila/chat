# endpoints/part_group_type_endpoint.py

from fastapi import APIRouter, Depends, HTTPException
from dependency_injector.wiring import inject, Provide
from typing import List

from webapp.ADM.master_data.part_group.type.schemas.part_group_type_schema import PartGroupTypeResponse, \
    PartGroupTypeCreate, PartGroupTypeUpdate
from webapp.ADM.master_data.part_group.type.services.part_group_type_service import PartGroupTypeService
from webapp.containers import Container

router = APIRouter()

@router.get("/", response_model=List[PartGroupTypeResponse])
@inject
def get_part_group_types(
    service: PartGroupTypeService = Depends(Provide[Container.part_group_type_service])
):
    return service.get_all_part_group_types()

@router.get("/{part_group_type_id}", response_model=PartGroupTypeResponse)
@inject
def get_part_group_type(
    part_group_type_id: int,
    service: PartGroupTypeService = Depends(Provide[Container.part_group_type_service])
):
    part_group_type = service.get_part_group_type_by_id(part_group_type_id)
    if not part_group_type:
        raise HTTPException(status_code=404, detail="PartGroupType not found")
    return part_group_type

@router.post("/", response_model=PartGroupTypeResponse)
@inject
def create_part_group_type(
    data: PartGroupTypeCreate,
    service: PartGroupTypeService = Depends(Provide[Container.part_group_type_service])
):
    return service.add_part_group_type(**data.dict())

@router.put("/{part_group_type_id}", response_model=PartGroupTypeResponse)
@inject
def update_part_group_type(
    part_group_type_id: int,
    data: PartGroupTypeUpdate,
    service: PartGroupTypeService = Depends(Provide[Container.part_group_type_service])
):
    return service.update_part_group_type(part_group_type_id, **data.dict())

@router.delete("/{part_group_type_id}")
@inject
def delete_part_group_type(
    part_group_type_id: int,
    service: PartGroupTypeService = Depends(Provide[Container.part_group_type_service])
):
    service.delete_part_group_type(part_group_type_id)
    return {"message": "PartGroupType deleted successfully"}
