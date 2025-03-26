from typing import List
from webapp.ADM.master_data.workplan_data.workplan_type.models.workplan_type_model import WorkPlanType
from webapp.ADM.master_data.workplan_data.workplan_type.repositories.workplan_type_repository import WorkPlanTypeRepository

class WorkPlanTypeService:
    def __init__(self, workplan_type_repository: WorkPlanTypeRepository) -> None:
        self.workplan_type_repository = workplan_type_repository

    def get_all_workplan_types(self) -> List[WorkPlanType]:
        return self.workplan_type_repository.get_all()

    def get_workplan_type_by_id(self, workplan_type_id: int) -> WorkPlanType:
        return self.workplan_type_repository.get_by_id(workplan_type_id)

    def add_workplan_type(self, name: str, description: str) -> WorkPlanType:
        return self.workplan_type_repository.add(name, description)

    def delete_workplan_type(self, workplan_type_id: int) -> None:
        self.workplan_type_repository.delete_by_id(workplan_type_id)

    def update_workplan_type(self, workplan_type_id: int, **kwargs) -> WorkPlanType:
        return self.workplan_type_repository.update_workplan_type(workplan_type_id, **kwargs)
