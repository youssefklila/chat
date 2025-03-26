from contextlib import AbstractContextManager
from sqlalchemy.orm import Session
from typing import Callable, List
from webapp.ADM.master_data.workplan_data.workplan_type.models.workplan_type_model import WorkPlanType

class WorkPlanTypeRepository:
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    def get_all(self) -> List[WorkPlanType]:
        with self.session_factory() as session:
            return session.query(WorkPlanType).all()

    def get_by_id(self, workplan_type_id: int) -> WorkPlanType:
        with self.session_factory() as session:
            return session.query(WorkPlanType).filter(WorkPlanType.id == workplan_type_id).first()

    def add(self, name: str, description: str) -> WorkPlanType:
        with self.session_factory() as session:
            workplan_type = WorkPlanType(name=name, description=description)
            session.add(workplan_type)
            session.commit()
            session.refresh(workplan_type)
            return workplan_type

    def delete_by_id(self, workplan_type_id: int) -> None:
        with self.session_factory() as session:
            workplan_type = session.query(WorkPlanType).filter(WorkPlanType.id == workplan_type_id).first()
            if workplan_type:
                session.delete(workplan_type)
                session.commit()

    def update_workplan_type(self, workplan_type_id: int, **kwargs) -> WorkPlanType:
        with self.session_factory() as session:
            workplan_type = session.query(WorkPlanType).filter(WorkPlanType.id == workplan_type_id).first()
            if workplan_type:
                for key, value in kwargs.items():
                    setattr(workplan_type, key, value)
                session.commit()
                session.refresh(workplan_type)
            return workplan_type
