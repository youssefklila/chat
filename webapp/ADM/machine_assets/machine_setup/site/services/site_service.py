# services/site_service.py

from typing import List

from webapp.ADM.machine_assets.machine_setup.site.models.site_model import Site
from webapp.ADM.machine_assets.machine_setup.site.repositories.site_repositorie import SiteRepository


class SiteService:
    def __init__(self, site_repository: SiteRepository) -> None:
        self.site_repository = site_repository

    def get_all_sites(self) -> List[Site]:
        return self.site_repository.get_all()

    def get_site_by_id(self, site_id: int) -> Site:
        return self.site_repository.get_by_id(site_id)

    def add_site(self, user_id: int, company_code_id: int, site_number: str, site_external_number: str, deletion_priority: int, geo_coordinates: str, description: str) -> Site:
        return self.site_repository.add(user_id, company_code_id, site_number, site_external_number, deletion_priority, geo_coordinates, description)

    def delete_site(self, site_id: int) -> None:
        self.site_repository.delete_by_id(site_id)

    def update_site(self, site_id: int, **kwargs) -> Site:
        return self.site_repository.update_site(site_id, **kwargs)
