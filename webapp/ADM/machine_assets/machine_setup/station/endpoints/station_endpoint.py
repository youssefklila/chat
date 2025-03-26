# endpoints/station_endpoint.py

from fastapi import APIRouter, Depends, HTTPException
from typing import List
from dependency_injector.wiring import inject, Provide
from webapp.ADM.machine_assets.machine_setup.station.schemas.station_schema import StationCreate, StationUpdate, StationResponse
from webapp.ADM.machine_assets.machine_setup.station.services.station_service import StationService
from webapp.containers import Container

router = APIRouter()

@router.get("/", response_model=List[StationResponse])
@inject
def get_stations(
    station_service: StationService = Depends(Provide[Container.station_service])
):
    return station_service.get_all_stations()

@router.get("/{station_id}", response_model=StationResponse)
@inject
def get_station(
    station_id: int,
    station_service: StationService = Depends(Provide[Container.station_service])
):
    station = station_service.get_station_by_id(station_id)
    if not station:
        raise HTTPException(status_code=404, detail="Station not found")
    return station

@router.post("/", response_model=StationResponse)
@inject
def create_station(
    station_data: StationCreate,
    station_service: StationService = Depends(Provide[Container.station_service])
):
    return station_service.add_station(**station_data.dict())

@router.put("/{station_id}", response_model=StationResponse)
@inject
def update_station(
    station_id: int, station_data: StationUpdate,
    station_service: StationService = Depends(Provide[Container.station_service])
):
    return station_service.update_station(station_id, **station_data.dict())

@router.delete("/{station_id}")
@inject
def delete_station(
    station_id: int,
    station_service: StationService = Depends(Provide[Container.station_service])
):
    station_service.delete_station(station_id)
    return {"message": "Station deleted successfully"}
