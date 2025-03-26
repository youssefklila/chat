# repositories/cell_repository.py

from contextlib import AbstractContextManager
from sqlalchemy.orm import Session
from typing import Callable, List

from webapp.ADM.machine_assets.machine_setup.cell.models.cell_model import Cell


class CellRepository:
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    def get_all(self) -> List[Cell]:
        with self.session_factory() as session:
            return session.query(Cell).all()

    def get_by_id(self, cell_id: int) -> Cell:
        with self.session_factory() as session:
            return session.query(Cell).filter(Cell.id == cell_id).first()

    def add(self, name: str, description: str, site_id: int, user_id: int, info: str, is_active: bool) -> Cell:
        with self.session_factory() as session:
            cell = Cell(name=name, description=description, site_id=site_id, user_id=user_id, info=info, is_active=is_active)
            session.add(cell)
            session.commit()
            session.refresh(cell)
            return cell

    def delete_by_id(self, cell_id: int) -> None:
        with self.session_factory() as session:
            cell = session.query(Cell).filter(Cell.id == cell_id).first()
            if cell:
                session.delete(cell)
                session.commit()

    def update_cell(self, cell_id: int, **kwargs) -> Cell:
        with self.session_factory() as session:
            cell = session.query(Cell).filter(Cell.id == cell_id).first()
            if cell:
                for key, value in kwargs.items():
                    setattr(cell, key, value)
                session.commit()
                session.refresh(cell)
            return cell
