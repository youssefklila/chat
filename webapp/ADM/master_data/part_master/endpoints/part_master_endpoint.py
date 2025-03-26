from fastapi import APIRouter, Depends, HTTPException
from typing import List
from dependency_injector.wiring import inject, Provide

from webapp.ADM.master_data.part_master.schemas.part_master_schema import PartMasterResponse, PartMasterCreate, \
    PartMasterUpdate
from webapp.ADM.master_data.part_master.services.part_master_service import PartMasterService
from webapp.containers import Container

router = APIRouter()

@router.get("/", response_model=List[PartMasterResponse])
@inject
def get_part_masters(
    part_master_service: PartMasterService = Depends(Provide[Container.part_master_service])
):
    return part_master_service.get_all_part_masters()

@router.get("/{part_master_id}", response_model=PartMasterResponse)
@inject
def get_part_master(
    part_master_id: int,
    part_master_service: PartMasterService = Depends(Provide[Container.part_master_service])
):
    part_master = part_master_service.get_part_master_by_id(part_master_id)
    if not part_master:
        raise HTTPException(status_code=404, detail="PartMaster not found")
    return part_master

@router.post("/", response_model=PartMasterResponse)
@inject
def create_part_master(
    part_master_data: PartMasterCreate,
    part_master_service: PartMasterService = Depends(Provide[Container.part_master_service])
):
    return part_master_service.create_part_master(**part_master_data.dict())

@router.put("/{part_master_id}", response_model=PartMasterResponse)
@inject
def update_part_master(
    part_master_id: int,
    part_master_data: PartMasterUpdate,
    part_master_service: PartMasterService = Depends(Provide[Container.part_master_service])
):
    return part_master_service.update_part_master(part_master_id, **part_master_data.dict())

@router.delete("/{part_master_id}")
@inject
def delete_part_master(
    part_master_id: int,
    part_master_service: PartMasterService = Depends(Provide[Container.part_master_service])
):
    part_master_service.delete_part_master(part_master_id)
    return {"message": "PartMaster deleted successfully"}
