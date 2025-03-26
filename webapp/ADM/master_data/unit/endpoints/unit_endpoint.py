# endpoints/unit_endpoint.py

from fastapi import APIRouter, Depends, HTTPException
from typing import List
from dependency_injector.wiring import inject, Provide
from webapp.ADM.master_data.unit.schemas.unit_schema import UnitCreate, UnitUpdate, UnitResponse
from webapp.ADM.master_data.unit.services.unit_service import UnitService
from webapp.containers import Container

router = APIRouter()

@router.get("/", response_model=List[UnitResponse])
@inject
def get_units(
    unit_service: UnitService = Depends(Provide[Container.unit_service])
):
    return unit_service.get_all_units()

@router.get("/{unit_id}", response_model=UnitResponse)
@inject
def get_unit(
    unit_id: int,
    unit_service: UnitService = Depends(Provide[Container.unit_service])
):
    unit = unit_service.get_unit_by_id(unit_id)
    if not unit:
        raise HTTPException(status_code=404, detail="Unit not found")
    return unit

@router.post("/", response_model=UnitResponse)
@inject
def create_unit(
    unit_data: UnitCreate,
    unit_service: UnitService = Depends(Provide[Container.unit_service])
):
    return unit_service.add_unit(**unit_data.dict())

@router.put("/{unit_id}", response_model=UnitResponse)
@inject
def update_unit(
    unit_id: int, unit_data: UnitUpdate,
    unit_service: UnitService = Depends(Provide[Container.unit_service])
):
    return unit_service.update_unit(unit_id, **unit_data.dict())

@router.delete("/{unit_id}")
@inject
def delete_unit(
    unit_id: int,
    unit_service: UnitService = Depends(Provide[Container.unit_service])
):
    unit_service.delete_unit(unit_id)
    return {"message": "Unit deleted successfully"}
