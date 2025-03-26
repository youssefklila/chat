# endpoints/company_code_endpoint.py

from fastapi import APIRouter, Depends, HTTPException
from typing import List
from dependency_injector.wiring import inject, Provide

from webapp.ADM.machine_assets.machine_setup.company_code.schemas.company_code_schema import CompanyCodeOut, CompanyCodeCreate, \
    CompanyCodeUpdate
from webapp.ADM.machine_assets.machine_setup.company_code.services.company_code_service import CompanyCodeService
from webapp.containers import Container

router = APIRouter()

@router.get("/", response_model=List[CompanyCodeOut])
@inject
def get_company_codes(
    company_code_service: CompanyCodeService = Depends(Provide[Container.company_code_service])
):
    return company_code_service.get_all_company_codes()

@router.get("/{company_code_id}", response_model=CompanyCodeOut)
@inject
def get_company_code(
    company_code_id: int,
    company_code_service: CompanyCodeService = Depends(Provide[Container.company_code_service])
):
    company_code = company_code_service.get_company_code_by_id(company_code_id)
    if not company_code:
        raise HTTPException(status_code=404, detail="CompanyCode not found")
    return company_code

@router.post("/", response_model=CompanyCodeOut)
@inject
def create_company_code(
    company_code_create: CompanyCodeCreate,  # Using Pydantic schema for validation
    company_code_service: CompanyCodeService = Depends(Provide[Container.company_code_service])
):
    return company_code_service.add_company_code(
        user_id=company_code_create.user_id,
        client_id=company_code_create.client_id,
        name=company_code_create.name,
        description=company_code_create.description
    )

@router.delete("/{company_code_id}")
@inject
def delete_company_code(
    company_code_id: int,
    company_code_service: CompanyCodeService = Depends(Provide[Container.company_code_service])
):
    company_code_service.delete_company_code(company_code_id)
    return {"message": "CompanyCode deleted successfully"}

@router.put("/{company_code_id}", response_model=CompanyCodeOut)
@inject
def update_company_code(
    company_code_id: int, company_code_update: CompanyCodeUpdate,  # Using Pydantic schema for updates
    company_code_service: CompanyCodeService = Depends(Provide[Container.company_code_service])
):
    return company_code_service.update_company_code(
        company_code_id,
        user_id=company_code_update.user_id,
        client_id=company_code_update.client_id,
        name=company_code_update.name,
        description=company_code_update.description
    )
