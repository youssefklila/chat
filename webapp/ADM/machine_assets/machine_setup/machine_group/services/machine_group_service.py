# services/machine_group_service.py
from webapp.ADM.machine_assets.machine_setup.machine_group.models.machine_group_model import MachineGroup
from webapp.ADM.machine_assets.machine_setup.machine_group.repositories.machine_group_repositorie import MachineGroupRepository


class MachineGroupService:
    def __init__(self, machine_group_repository: MachineGroupRepository):
        self.machine_group_repository = machine_group_repository

    def create_machine_group(self, name: str, description: str, user_id: int, cell_id: int, is_active: bool, failure: bool) -> MachineGroup:
        return self.machine_group_repository.add(name, description, user_id, cell_id, is_active, failure)

    def get_machine_group_by_id(self, machine_group_id: int) -> MachineGroup:
        return self.machine_group_repository.get_by_id(machine_group_id)

    def get_all_machine_groups(self) -> list[MachineGroup]:
        return self.machine_group_repository.get_all()

    def update_machine_group(self, machine_group_id: int, name: str, description: str, is_active: bool, failure: bool) -> MachineGroup:
        return self.machine_group_repository.update(machine_group_id, name, description, is_active, failure)

    def delete_machine_group(self, machine_group_id: int) -> bool:
        return self.machine_group_repository.delete(machine_group_id)
