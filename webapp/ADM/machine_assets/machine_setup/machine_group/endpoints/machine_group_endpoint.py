# endpoints/machine_group_endpoint.py

from fastapi import APIRouter, Depends, HTTPException

from webapp.ADM.machine_assets.machine_setup.machine_group.schemas.machine_group_schema import MachineGroup, MachineGroupCreate, \
    MachineGroupUpdate
from webapp.ADM.machine_assets.machine_setup.machine_group.services.machine_group_service import MachineGroupService
from webapp.containers import Container
from dependency_injector.wiring import inject, Provide

router = APIRouter()

@router.post("/", response_model=MachineGroup)
@inject
def create_machine_group(
    machine_group: MachineGroupCreate,
    machine_group_service: MachineGroupService = Depends(Provide[Container.machine_group_service])
):
    return machine_group_service.create_machine_group(
        name=machine_group.name,
        description=machine_group.description,
        user_id=machine_group.user_id,
        cell_id=machine_group.cell_id,
        is_active=machine_group.is_active,
        failure=machine_group.failure
    )

@router.get("/{machine_group_id}", response_model=MachineGroup)
@inject
def get_machine_group(
    machine_group_id: int,
    machine_group_service: MachineGroupService = Depends(Provide[Container.machine_group_service])
):
    machine_group = machine_group_service.get_machine_group_by_id(machine_group_id)
    if machine_group is None:
        raise HTTPException(status_code=404, detail="Machine group not found")
    return machine_group

@router.get("/", response_model=list[MachineGroup])
@inject
def get_all_machine_groups(
    machine_group_service: MachineGroupService = Depends(Provide[Container.machine_group_service])
):
    return machine_group_service.get_all_machine_groups()

@router.put("/{machine_group_id}", response_model=MachineGroup)
@inject
def update_machine_group(
    machine_group_id: int,
    machine_group: MachineGroupUpdate,
    machine_group_service: MachineGroupService = Depends(Provide[Container.machine_group_service])
):
    updated_machine_group = machine_group_service.update_machine_group(
        machine_group_id,
        machine_group.name,
        machine_group.description,
        machine_group.is_active,
        machine_group.failure
    )
    if updated_machine_group is None:
        raise HTTPException(status_code=404, detail="Machine group not found")
    return updated_machine_group

@router.delete("/{machine_group_id}", status_code=204)
@inject
def delete_machine_group(
    machine_group_id: int,
    machine_group_service: MachineGroupService = Depends(Provide[Container.machine_group_service])
):
    success = machine_group_service.delete_machine_group(machine_group_id)
    if not success:
        raise HTTPException(status_code=404, detail="Machine group not found")
