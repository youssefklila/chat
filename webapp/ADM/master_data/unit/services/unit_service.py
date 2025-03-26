# services/unit_service.py

from typing import List
from webapp.ADM.master_data.unit.models.unit_model import Unit
from webapp.ADM.master_data.unit.repositories.unit_repository import UnitRepository

class UnitService:
    def __init__(self, unit_repository: UnitRepository) -> None:
        self.unit_repository = unit_repository

    def get_all_units(self) -> List[Unit]:
        return self.unit_repository.get_all()

    def get_unit_by_id(self, unit_id: int) -> Unit:
        return self.unit_repository.get_by_id(unit_id)

    def add_unit(self, unit_name: str, description: str) -> Unit:
        return self.unit_repository.add(unit_name, description)

    def delete_unit(self, unit_id: int) -> None:
        self.unit_repository.delete_by_id(unit_id)

    def update_unit(self, unit_id: int, **kwargs) -> Unit:
        return self.unit_repository.update_unit(unit_id, **kwargs)
