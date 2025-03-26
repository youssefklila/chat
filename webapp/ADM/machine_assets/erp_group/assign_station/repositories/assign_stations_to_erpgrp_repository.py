# repositories/assign_stations_to_erpgrp_repository.py

from contextlib import AbstractContextManager
from sqlalchemy.orm import Session
from typing import Callable, List
from webapp.ADM.machine_assets.erp_group.assign_station.models.assign_stations_to_erpgrp_model import AssignStationsToErpGrp

class AssignStationsToErpGrpRepository:
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    def get_all(self) -> List[AssignStationsToErpGrp]:
        with self.session_factory() as session:
            return session.query(AssignStationsToErpGrp).all()

    def get_by_id(self, assign_id: int) -> AssignStationsToErpGrp:
        with self.session_factory() as session:
            return session.query(AssignStationsToErpGrp).filter(AssignStationsToErpGrp.id == assign_id).first()

    def get_by_station_id(self, station_id: int) -> List[AssignStationsToErpGrp]:
        with self.session_factory() as session:
            return session.query(AssignStationsToErpGrp).filter(AssignStationsToErpGrp.station_id == station_id).all()

    def add(self, station_id: int, erp_group_id: int, station_type: str, user_id: int) -> AssignStationsToErpGrp:
        with self.session_factory() as session:
            assign_st_erpgrp = AssignStationsToErpGrp(
                station_id=station_id,
                erp_group_id=erp_group_id,
                station_type=station_type,
                user_id=user_id
            )
            session.add(assign_st_erpgrp)
            session.commit()
            session.refresh(assign_st_erpgrp)
            return assign_st_erpgrp

    def delete_by_id(self, assign_id: int) -> None:
        with self.session_factory() as session:
            assign_st_erpgrp = session.query(AssignStationsToErpGrp).filter(AssignStationsToErpGrp.id == assign_id).first()
            if assign_st_erpgrp:
                session.delete(assign_st_erpgrp)
                session.commit()
