from typing import List

from webapp.ADM.master_data.workplan_data.workplan.models.workplan_model import WorkPlan
from webapp.ADM.master_data.workplan_data.workplan.repositories.workplan_repository import WorkPlanRepository


class WorkPlanService:
    def __init__(self, repository: WorkPlanRepository):
        self.repository = repository

    def get_all_work_plans(self) -> List[WorkPlan]:
        return self.repository.get_all()

    def get_work_plan_by_id(self, workplan_id: int) -> WorkPlan:
        return self.repository.get_by_id(workplan_id)

    def add_work_plan(self, **kwargs) -> WorkPlan:
        return self.repository.add(**kwargs)

    def delete_work_plan(self, workplan_id: int) -> None:
        self.repository.delete_by_id(workplan_id)

    def update_work_plan(self, workplan_id: int, **kwargs) -> WorkPlan:
        return self.repository.update(workplan_id, **kwargs)
