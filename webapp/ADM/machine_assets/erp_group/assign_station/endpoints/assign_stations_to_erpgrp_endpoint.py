# endpoints/assign_stations_to_erpgrp_endpoint.py

from fastapi import APIRouter, Depends, HTTPException
from typing import List
from dependency_injector.wiring import inject, Provide
from webapp.ADM.machine_assets.erp_group.assign_station.schemas.assign_stations_to_erpgrp_schema import (
    AssignStationsToErpGrpCreate,
    AssignStationsToErpGrpResponse,
)
from webapp.ADM.machine_assets.erp_group.assign_station.services.assign_stations_to_erpgrp_service import AssignStationsToErpGrpService
from webapp.containers import Container

router = APIRouter()

@router.get("/", response_model=List[AssignStationsToErpGrpResponse])
@inject
def get_assignments(
    assign_stations_to_erpgrp_service: AssignStationsToErpGrpService = Depends(
        Provide[Container.assign_stations_to_erpgrp_service]
    )
):
    return assign_stations_to_erpgrp_service.get_all_assignments()

@router.get("/{assign_id}", response_model=AssignStationsToErpGrpResponse)
@inject
def get_assignment(
    assign_id: int,
    assign_stations_to_erpgrp_service: AssignStationsToErpGrpService = Depends(
        Provide[Container.assign_stations_to_erpgrp_service]
    )
):
    assignment = assign_stations_to_erpgrp_service.get_assignment_by_id(assign_id)
    if not assignment:
        raise HTTPException(status_code=404, detail="Assignment not found")
    return assignment

@router.get("/station/{station_id}", response_model=List[AssignStationsToErpGrpResponse])
@inject
def get_assignments_by_station(
    station_id: int,
    assign_stations_to_erpgrp_service: AssignStationsToErpGrpService = Depends(
        Provide[Container.assign_stations_to_erpgrp_service]
    )
):
    return assign_stations_to_erpgrp_service.get_assignments_by_station_id(station_id)

@router.post("/", response_model=AssignStationsToErpGrpResponse)
@inject
def create_assignment(
    assignment_data: AssignStationsToErpGrpCreate,
    assign_stations_to_erpgrp_service: AssignStationsToErpGrpService = Depends(
        Provide[Container.assign_stations_to_erpgrp_service]
    )
):
    return assign_stations_to_erpgrp_service.add_assignment(**assignment_data.dict())

@router.delete("/{assign_id}")
@inject
def delete_assignment(
    assign_id: int,
    assign_stations_to_erpgrp_service: AssignStationsToErpGrpService = Depends(
        Provide[Container.assign_stations_to_erpgrp_service]
    )
):
    assign_stations_to_erpgrp_service.delete_assignment(assign_id)
    return {"message": "Assignment deleted successfully"}
