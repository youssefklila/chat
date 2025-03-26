from contextlib import AbstractContextManager
from sqlalchemy.orm import Session
from typing import Callable, List
from webapp.ADM.master_data.part_group.group.models.part_group_model import PartGroup

class PartGroupRepository:
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    def get_all(self) -> List[PartGroup]:
        with self.session_factory() as session:
            return session.query(PartGroup).all()

    def get_by_id(self, part_group_id: int) -> PartGroup:
        with self.session_factory() as session:
            return session.query(PartGroup).filter(PartGroup.id == part_group_id).first()

    def add(self, name: str, description: str, user_id: int, part_type: str, costs: int, is_active: bool,
            circulating_lot: int, automatic_emptying: int, master_workplan: str, comment: str, state: int,
            material_transfer: bool, created_on: str, edited_on: str, part_group_type_id: int) -> PartGroup:
        with self.session_factory() as session:
            part_group = PartGroup(
                name=name,
                description=description,
                user_id=user_id,
                part_type=part_type,
                costs=costs,
                is_active=is_active,
                circulating_lot=circulating_lot,
                automatic_emptying=automatic_emptying,
                master_workplan=master_workplan,
                comment=comment,
                state=state,
                material_transfer=material_transfer,
                created_on=created_on,
                edited_on=edited_on,
                part_group_type_id=part_group_type_id
            )
            session.add(part_group)
            session.commit()
            session.refresh(part_group)
            return part_group

    def delete_by_id(self, part_group_id: int) -> None:
        with self.session_factory() as session:
            part_group = session.query(PartGroup).filter(PartGroup.id == part_group_id).first()
            if part_group:
                session.delete(part_group)
                session.commit()

    def update_part_group(self, part_group_id: int, **kwargs) -> PartGroup:
        with self.session_factory() as session:
            part_group = session.query(PartGroup).filter(PartGroup.id == part_group_id).first()
            if part_group:
                for key, value in kwargs.items():
                    setattr(part_group, key, value)
                session.commit()
                session.refresh(part_group)
            return part_group
