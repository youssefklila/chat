# repositories/machine_group_repository.py

from webapp.ADM.machine_assets.machine_setup.machine_group.models.machine_group_model import MachineGroup


class MachineGroupRepository:
    def __init__(self, session_factory):
        self.session_factory = session_factory

    def add(self, name: str, description: str, user_id: int, cell_id: int, is_active: bool, failure: bool) -> MachineGroup:
        with self.session_factory() as session:
            machine_group = MachineGroup(
                name=name,
                description=description,
                user_id=user_id,
                cell_id=cell_id,
                is_active=is_active,
                failure=failure
            )
            session.add(machine_group)
            session.commit()
            session.refresh(machine_group)
            return machine_group

    def get_by_id(self, machine_group_id: int) -> MachineGroup:
        with self.session_factory() as session:
            return session.query(MachineGroup).filter(MachineGroup.id == machine_group_id).first()

    def get_all(self) -> list[MachineGroup]:
        with self.session_factory() as session:
            return session.query(MachineGroup).all()

    def update(self, machine_group_id: int, name: str, description: str, is_active: bool, failure: bool) -> MachineGroup:
        with self.session_factory() as session:
            machine_group = session.query(MachineGroup).filter(MachineGroup.id == machine_group_id).first()
            if machine_group:
                machine_group.name = name
                machine_group.description = description
                machine_group.is_active = is_active
                machine_group.failure = failure
                session.commit()
                session.refresh(machine_group)
                return machine_group
            return None

    def delete(self, machine_group_id: int) -> bool:
        with self.session_factory() as session:
            machine_group = session.query(MachineGroup).filter(MachineGroup.id == machine_group_id).first()
            if machine_group:
                session.delete(machine_group)
                session.commit()
                return True
            return False
