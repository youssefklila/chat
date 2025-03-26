# services/company_code_service.py

from typing import List

from webapp.ADM.machine_assets.machine_setup.company_code.models.company_code_model import CompanyCode
from webapp.ADM.machine_assets.machine_setup.company_code.repositories.company_code_repositorie import CompanyCodeRepository


class CompanyCodeService:
    def __init__(self, company_code_repository: CompanyCodeRepository) -> None:
        self.company_code_repository = company_code_repository

    def get_all_company_codes(self) -> List[CompanyCode]:
        return self.company_code_repository.get_all()

    def get_company_code_by_id(self, company_code_id: int) -> CompanyCode:
        return self.company_code_repository.get_by_id(company_code_id)

    def add_company_code(self, user_id: int, client_id: int, name: str, description: str) -> CompanyCode:
        return self.company_code_repository.add(user_id, client_id, name, description)

    def delete_company_code(self, company_code_id: int) -> None:
        self.company_code_repository.delete_by_id(company_code_id)

    def update_company_code(self, company_code_id: int, **kwargs) -> CompanyCode:
        return self.company_code_repository.update_company_code(company_code_id, **kwargs)
