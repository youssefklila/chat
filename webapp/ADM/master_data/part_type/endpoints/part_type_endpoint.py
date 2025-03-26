# endpoints/part_type_endpoint.py

from fastapi import APIRouter, Depends, HTTPException
from dependency_injector.wiring import inject, Provide
from typing import List

from webapp.ADM.master_data.part_type.schemas.part_type_schema import PartTypeResponse, PartTypeCreate, PartTypeUpdate
from webapp.ADM.master_data.part_type.services.part_type_service import PartTypeService
from webapp.containers import Container

router = APIRouter()

@router.get("/", response_model=List[PartTypeResponse])
@inject
def get_part_types(
    service: PartTypeService = Depends(Provide[Container.part_type_service])
):
    return service.get_all_part_types()

@router.get("/{part_type_id}", response_model=PartTypeResponse)
@inject
def get_part_type(
    part_type_id: int,
    service: PartTypeService = Depends(Provide[Container.part_type_service])
):
    part_type = service.get_part_type_by_id(part_type_id)
    if not part_type:
        raise HTTPException(status_code=404, detail="PartType not found")
    return part_type

@router.post("/", response_model=PartTypeResponse)
@inject
def create_part_type(
    data: PartTypeCreate,
    service: PartTypeService = Depends(Provide[Container.part_type_service])
):
    return service.add_part_type(**data.dict())

@router.put("/{part_type_id}", response_model=PartTypeResponse)
@inject
def update_part_type(
    part_type_id: int,
    data: PartTypeUpdate,
    service: PartTypeService = Depends(Provide[Container.part_type_service])
):
    return service.update_part_type(part_type_id, **data.dict())

@router.delete("/{part_type_id}")
@inject
def delete_part_type(
    part_type_id: int,
    service: PartTypeService = Depends(Provide[Container.part_type_service])
):
    service.delete_part_type(part_type_id)
    return {"message": "PartType deleted successfully"}
