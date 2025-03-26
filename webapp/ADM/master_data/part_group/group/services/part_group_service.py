from typing import List
from webapp.ADM.master_data.part_group.group.models.part_group_model import PartGroup
from webapp.ADM.master_data.part_group.group.repositories.part_group_repository import PartGroupRepository

class PartGroupService:
    def __init__(self, part_group_repository: PartGroupRepository) -> None:
        self.part_group_repository = part_group_repository

    def get_all_part_groups(self) -> List[PartGroup]:
        return self.part_group_repository.get_all()

    def get_part_group_by_id(self, part_group_id: int) -> PartGroup:
        return self.part_group_repository.get_by_id(part_group_id)

    def add_part_group(self, name: str, description: str, user_id: int, part_type: str, costs: int, is_active: bool,
                       circulating_lot: int, automatic_emptying: int, master_workplan: str, comment: str, state: int,
                       material_transfer: bool, created_on: str, edited_on: str, part_group_type_id: int) -> PartGroup:
        return self.part_group_repository.add(name, description, user_id, part_type, costs, is_active,
                                              circulating_lot, automatic_emptying, master_workplan, comment, state,
                                              material_transfer, created_on, edited_on, part_group_type_id)

    def delete_part_group(self, part_group_id: int) -> None:
        self.part_group_repository.delete_by_id(part_group_id)

    def update_part_group(self, part_group_id: int, **kwargs) -> PartGroup:
        return self.part_group_repository.update_part_group(part_group_id, **kwargs)
