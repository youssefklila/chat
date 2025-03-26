from contextlib import AbstractContextManager
from sqlalchemy.orm import Session
from typing import Callable, List
from webapp.ADM.machine_assets.erp_group.erp.models.erp_model import ERPGroup

class ERPGroupRepository:
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    def get_all(self) -> List[ERPGroup]:
        with self.session_factory() as session:
            return session.query(ERPGroup).all()

    def get_by_id(self, erp_group_id: int) -> ERPGroup:
        with self.session_factory() as session:
            return session.query(ERPGroup).filter(ERPGroup.id == erp_group_id).first()

    def add(self, erp_group_data: ERPGroup) -> ERPGroup:
        with self.session_factory() as session:
            session.add(erp_group_data)
            session.commit()
            session.refresh(erp_group_data)
            return erp_group_data

    def delete_by_id(self, erp_group_id: int) -> None:
        with self.session_factory() as session:
            erp_group = session.query(ERPGroup).filter(ERPGroup.id == erp_group_id).first()
            if erp_group:
                session.delete(erp_group)
                session.commit()

    def update(self, erp_group_id: int, **kwargs) -> ERPGroup:
        with self.session_factory() as session:
            erp_group = session.query(ERPGroup).filter(ERPGroup.id == erp_group_id).first()
            if erp_group:
                for key, value in kwargs.items():
                    setattr(erp_group, key, value)
                session.commit()
                session.refresh(erp_group)
            return erp_group
