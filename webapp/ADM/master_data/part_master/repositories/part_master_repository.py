from typing import Callable
from sqlalchemy.orm import Session
from contextlib import AbstractContextManager
from webapp.ADM.master_data.part_master.models.part_master_model import PartMaster


class PartMasterRepository:
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    def get_all(self):
        with self.session_factory() as session:
            return session.query(PartMaster).all()

    def get_by_id(self, part_master_id: int):
        with self.session_factory() as session:
            return session.query(PartMaster).filter(PartMaster.id == part_master_id).first()

    def create(self, **kwargs):
        with self.session_factory() as session:
            new_part_master = PartMaster(**kwargs)
            session.add(new_part_master)
            session.flush()  # Ensures IDs are assigned before commit
            session.commit()  # Commit the transaction to save to the database
            session.refresh(new_part_master)
            return new_part_master

    def update(self, part_master_id: int, **kwargs):
        with self.session_factory() as session:
            part_master = session.query(PartMaster).filter(PartMaster.id == part_master_id).first()
            if part_master:
                for key, value in kwargs.items():
                    setattr(part_master, key, value)
                session.flush()  # Sync changes with the database immediately
            return part_master

    def delete(self, part_master_id: int):
        with self.session_factory() as session:
            part_master = session.query(PartMaster).filter(PartMaster.id == part_master_id).first()
            if part_master:
                session.delete(part_master)
