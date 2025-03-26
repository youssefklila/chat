# repositories/unit_repository.py

from contextlib import AbstractContextManager
from sqlalchemy.orm import Session
from typing import Callable, List
from webapp.ADM.master_data.unit.models.unit_model import Unit

class UnitRepository:
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    def get_all(self) -> List[Unit]:
        with self.session_factory() as session:
            return session.query(Unit).all()

    def get_by_id(self, unit_id: int) -> Unit:
        with self.session_factory() as session:
            return session.query(Unit).filter(Unit.id == unit_id).first()

    def add(self, unit_name: str, description: str) -> Unit:
        with self.session_factory() as session:
            unit = Unit(
                unit_name=unit_name,
                description=description
            )
            session.add(unit)
            session.commit()
            session.refresh(unit)
            return unit

    def delete_by_id(self, unit_id: int) -> None:
        with self.session_factory() as session:
            unit = session.query(Unit).filter(Unit.id == unit_id).first()
            if unit:
                session.delete(unit)
                session.commit()

    def update_unit(self, unit_id: int, **kwargs) -> Unit:
        with self.session_factory() as session:
            unit = session.query(Unit).filter(Unit.id == unit_id).first()
            if unit:
                for key, value in kwargs.items():
                    setattr(unit, key, value)
                session.commit()
                session.refresh(unit)
            return unit
