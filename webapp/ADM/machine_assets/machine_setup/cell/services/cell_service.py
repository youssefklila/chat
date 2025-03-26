# services/cell_service.py

from typing import List

from webapp.ADM.machine_assets.machine_setup.cell.models.cell_model import Cell
from webapp.ADM.machine_assets.machine_setup.cell.repositories.cell_repositorie import CellRepository


class CellService:
    def __init__(self, cell_repository: CellRepository) -> None:
        self.cell_repository = cell_repository

    def get_all_cells(self) -> List[Cell]:
        return self.cell_repository.get_all()

    def get_cell_by_id(self, cell_id: int) -> Cell:
        return self.cell_repository.get_by_id(cell_id)

    def add_cell(self, name: str, description: str, site_id: int, user_id: int, info: str, is_active: bool) -> Cell:
        return self.cell_repository.add(name, description, site_id, user_id, info, is_active)

    def delete_cell(self, cell_id: int) -> None:
        self.cell_repository.delete_by_id(cell_id)

    def update_cell(self, cell_id: int, **kwargs) -> Cell:
        return self.cell_repository.update_cell(cell_id, **kwargs)
