"""Endpoints module."""

from fastapi import APIRouter, Depends, Response, status, HTTPException
from dependency_injector.wiring import inject, Provide

from webapp.ADM.machine_assets.machine_setup.client.schemas.client_schema import ClientUpdate
from webapp.ADM.machine_assets.machine_setup.client.services.client_service import ClientService
from webapp.ADM.machine_assets.machine_setup.user.repositories.user_repositorie import NotFoundError
from webapp.containers import Container


router = APIRouter()

@router.get("/clients",tags=["Clients"])
@inject
def get_clients(
        client_service: ClientService = Depends(Provide[Container.client_service]),
):
    return client_service.get_clients()


@router.get("/clients/{client_id}",tags=["Clients"])
@inject
def get_client_by_id(
        client_id: int,
        client_service: ClientService = Depends(Provide[Container.client_service]),
):
    try:
        return client_service.get_client_by_id(client_id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)


@router.post("/clients", status_code=status.HTTP_201_CREATED,tags=["Clients"])
@inject
def add_client(
        client_data: ClientUpdate,
        client_service: ClientService = Depends(Provide[Container.client_service]),
):
    return client_service.create_client(
        user_id=client_data.user_id,
        company_code=client_data.company_code,
        name = client_data.name,
        description = client_data.description)



@router.delete("/clients/{client_id}", status_code=status.HTTP_204_NO_CONTENT,tags=["Clients"])
@inject
def remove_client(
        client_id: int,
        client_service: ClientService = Depends(Provide[Container.client_service]),
):
    try:
        client_service.delete_client_by_id(client_id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/clients/{client_id}",tags=["Clients"])
@inject
def update_client(
        client_id: int,
        client_data: ClientUpdate,
        client_service: ClientService = Depends(Provide[Container.client_service]),
):
    try:
        client = client_service.update_client(client_id,
            user_id=client_data.user_id,
            company_code=client_data.company_code,
            name = client_data.name,
            description = client_data.description)
        return client
    except NotFoundError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
