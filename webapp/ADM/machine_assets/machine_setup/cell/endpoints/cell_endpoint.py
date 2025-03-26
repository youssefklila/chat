# endpoints/cell_endpoint.py

from fastapi import APIRouter, Depends, HTTPException
from typing import List
from dependency_injector.wiring import inject, Provide

from webapp.ADM.machine_assets.machine_setup.cell.schemas.cell_schema import CellOut, CellCreate, CellUpdate
from webapp.ADM.machine_assets.machine_setup.cell.services.cell_service import CellService
from webapp.containers import Container

router = APIRouter()

@router.get("/", response_model=List[CellOut])
@inject
def get_cells(
    cell_service: CellService = Depends(Provide[Container.cell_service])
):
    return cell_service.get_all_cells()

@router.get("/{cell_id}", response_model=CellOut)
@inject
def get_cell(
    cell_id: int,
    cell_service: CellService = Depends(Provide[Container.cell_service])
):
    cell = cell_service.get_cell_by_id(cell_id)
    if not cell:
        raise HTTPException(status_code=404, detail="Cell not found")
    return cell

@router.post("/", response_model=CellOut)
@inject
def create_cell(
    cell_create: CellCreate,
    cell_service: CellService = Depends(Provide[Container.cell_service])
):
    return cell_service.add_cell(
        name=cell_create.name,
        description=cell_create.description,
        site_id=cell_create.site_id,
        user_id=cell_create.user_id,
        info=cell_create.info,
        is_active=cell_create.is_active
    )

@router.delete("/{cell_id}")
@inject
def delete_cell(
    cell_id: int,
    cell_service: CellService = Depends(Provide[Container.cell_service])
):
    cell_service.delete_cell(cell_id)
    return {"message": "Cell deleted successfully"}

@router.put("/{cell_id}", response_model=CellOut)
@inject
def update_cell(
    cell_id: int, cell_update: CellUpdate,
    cell_service: CellService = Depends(Provide[Container.cell_service])
):
    return cell_service.update_cell(
        cell_id,
        name=cell_update.name,
        description=cell_update.description,
        site_id=cell_update.site_id,
        user_id=cell_update.user_id,
        info=cell_update.info,
        is_active=cell_update.is_active
    )
