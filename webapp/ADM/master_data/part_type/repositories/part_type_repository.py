from sqlalchemy.orm import Session
from typing import List
from webapp.ADM.master_data.part_type.models.part_type_model import PartType
from typing import Callable, Iterator
from contextlib import AbstractContextManager

class PartTypeRepository:
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    def get_all(self) -> List[PartType]:
        with self.session_factory() as session:
            return session.query(PartType).all()

    def get_by_id(self, part_type_id: int) -> PartType:
        with self.session_factory() as session:
            return session.query(PartType).filter(PartType.id == part_type_id).first()

    def add(self, name: str, description: str, user_id: int, is_active: bool) -> PartType:
        with self.session_factory() as session:
            part_type = PartType(
                name=name,
                description=description,
                user_id=user_id,
                is_active=is_active,
            )
            session.add(part_type)
            session.commit()
            session.refresh(part_type)
            return part_type

    def update(self, part_type_id: int, **kwargs) -> PartType:
        with self.session_factory() as session:
            part_type = session.query(PartType).filter(PartType.id == part_type_id).first()
            if part_type:
                for key, value in kwargs.items():
                    setattr(part_type, key, value)
                session.commit()
                session.refresh(part_type)
            return part_type

    def delete(self, part_type_id: int) -> None:
        with self.session_factory() as session:
            part_type = session.query(PartType).filter(PartType.id == part_type_id).first()
            if part_type:
                session.delete(part_type)
                session.commit()
