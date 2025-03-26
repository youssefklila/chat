# services/part_type_service.py

from typing import List

from webapp.ADM.master_data.part_type.models.part_type_model import PartType
from webapp.ADM.master_data.part_type.repositories.part_type_repository import PartTypeRepository


class PartTypeService:
    def __init__(self, repository: PartTypeRepository):
        self.repository = repository

    def get_all_part_types(self) -> List[PartType]:
        return self.repository.get_all()

    def get_part_type_by_id(self, part_type_id: int) -> PartType:
        return self.repository.get_by_id(part_type_id)

    def add_part_type(self, name: str, description: str, user_id: int, is_active: bool) -> PartType:
        return self.repository.add(name, description, user_id, is_active)

    def update_part_type(self, part_type_id: int, **kwargs) -> PartType:
        return self.repository.update(part_type_id, **kwargs)

    def delete_part_type(self, part_type_id: int) -> None:
        self.repository.delete(part_type_id)
