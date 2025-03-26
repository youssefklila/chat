# services/erp_group_service.py

from typing import List
from webapp.ADM.machine_assets.erp_group.erp.models.erp_model import ERPGroup
from webapp.ADM.machine_assets.erp_group.erp.repositories.erp_repositorie import ERPGroupRepository
from webapp.ADM.machine_assets.erp_group.erp.schemas.erp_schema import ERPGroupCreate

class ERPGroupService:
    def __init__(self, erp_group_repository: ERPGroupRepository) -> None:
        self.erp_group_repository = erp_group_repository

    def get_all_erp_groups(self) -> List[ERPGroup]:
        return self.erp_group_repository.get_all()

    def get_erp_group_by_id(self, erp_group_id: int) -> ERPGroup:
        return self.erp_group_repository.get_by_id(erp_group_id)

    def add_erp_group(self, erp_group_data: ERPGroupCreate) -> ERPGroup:
        erp_group = ERPGroup(**erp_group_data.dict())
        return self.erp_group_repository.add(erp_group)

    def delete_erp_group(self, erp_group_id: int) -> None:
        self.erp_group_repository.delete_by_id(erp_group_id)

    def update_erp_group(self, erp_group_id: int, **kwargs) -> ERPGroup:
        return self.erp_group_repository.update(erp_group_id, **kwargs)
