# endpoints/site_endpoint.py

from fastapi import APIRouter, Depends, HTTPException
from typing import List
from dependency_injector.wiring import inject, Provide

from webapp.ADM.machine_assets.machine_setup.site.schemas.site_schema import SiteResponse, SiteCreate, SiteUpdate
from webapp.ADM.machine_assets.machine_setup.site.services.site_service import SiteService
from webapp.containers import Container

router = APIRouter()

@router.get("/", response_model=List[SiteResponse])
@inject
def get_sites(
    site_service: SiteService = Depends(Provide[Container.site_service])
):
    return site_service.get_all_sites()

@router.get("/{site_id}", response_model=SiteResponse)
@inject
def get_site(
    site_id: int,
    site_service: SiteService = Depends(Provide[Container.site_service])
):
    site = site_service.get_site_by_id(site_id)
    if not site:
        raise HTTPException(status_code=404, detail="Site not found")
    return site

@router.post("/", response_model=SiteResponse)
@inject
def create_site(
    site_data: SiteCreate,
    site_service: SiteService = Depends(Provide[Container.site_service])
):
    return site_service.add_site(**site_data.dict())

@router.delete("/{site_id}")
@inject
def delete_site(
    site_id: int,
    site_service: SiteService = Depends(Provide[Container.site_service])
):
    site_service.delete_site(site_id)
    return {"message": "Site deleted successfully"}

@router.put("/{site_id}", response_model=SiteResponse)
@inject
def update_site(
    site_id: int, site_data: SiteUpdate,
    site_service: SiteService = Depends(Provide[Container.site_service])
):
    return site_service.update_site(site_id, **site_data.dict(exclude_unset=True))
