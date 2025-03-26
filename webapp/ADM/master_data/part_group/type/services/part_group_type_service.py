# services/part_group_type_service.py

from typing import List

from webapp.ADM.master_data.part_group.type.models.part_group_type_model import PartGroupType
from webapp.ADM.master_data.part_group.type.repositories.part_group_type_repository import PartGroupTypeRepository


class PartGroupTypeService:
    def __init__(self, repository: PartGroupTypeRepository):
        self.repository = repository

    def get_all_part_group_types(self) -> List[PartGroupType]:
        return self.repository.get_all()

    def get_part_group_type_by_id(self, part_group_type_id: int) -> PartGroupType:
        return self.repository.get_by_id(part_group_type_id)

    def add_part_group_type(self, name: str, description: str) -> PartGroupType:
        return self.repository.add(name, description)

    def update_part_group_type(self, part_group_type_id: int, **kwargs) -> PartGroupType:
        return self.repository.update(part_group_type_id, **kwargs)

    def delete_part_group_type(self, part_group_type_id: int) -> None:
        self.repository.delete(part_group_type_id)
