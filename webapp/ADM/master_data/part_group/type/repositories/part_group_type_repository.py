from sqlalchemy.orm import Session
from typing import List, Callable
from contextlib import AbstractContextManager
from webapp.ADM.master_data.part_group.type.models.part_group_type_model import PartGroupType

class PartGroupTypeRepository:
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    def get_all(self) -> List[PartGroupType]:
        # Use the session factory to create a session context
        with self.session_factory() as session:
            return session.query(PartGroupType).all()

    def get_by_id(self, part_group_type_id: int) -> PartGroupType:
        with self.session_factory() as session:
            return session.query(PartGroupType).filter(PartGroupType.id == part_group_type_id).first()

    def add(self, name: str, description: str) -> PartGroupType:
        with self.session_factory() as session:
            part_group_type = PartGroupType(name=name, description=description)
            session.add(part_group_type)
            session.commit()
            session.refresh(part_group_type)
            return part_group_type

    def update(self, part_group_type_id: int, **kwargs) -> PartGroupType:
        with self.session_factory() as session:
            part_group_type = session.query(PartGroupType).filter(PartGroupType.id == part_group_type_id).first()
            if part_group_type:
                for key, value in kwargs.items():
                    setattr(part_group_type, key, value)
                session.commit()
                session.refresh(part_group_type)
            return part_group_type

    def delete(self, part_group_type_id: int) -> None:
        with self.session_factory() as session:
            part_group_type = session.query(PartGroupType).filter(PartGroupType.id == part_group_type_id).first()
            if part_group_type:
                session.delete(part_group_type)
                session.commit()
