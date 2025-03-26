# repositories/station_repository.py

from contextlib import AbstractContextManager
from sqlalchemy.orm import Session
from typing import Callable, List
from webapp.ADM.machine_assets.machine_setup.station.models.station_model import Station

class StationRepository:
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    def get_all(self) -> List[Station]:
        with self.session_factory() as session:
            return session.query(Station).all()

    def get_by_id(self, station_id: int) -> Station:
        with self.session_factory() as session:
            return session.query(Station).filter(Station.id == station_id).first()

    def add(self, machine_group_id: int, name: str, description: str, is_active: bool, user_id: int, info: str) -> Station:
        with self.session_factory() as session:
            station = Station(
                machine_group_id=machine_group_id,
                name=name,
                description=description,
                is_active=is_active,
                user_id=user_id,
                info=info
            )
            session.add(station)
            session.commit()
            session.refresh(station)
            return station

    def delete_by_id(self, station_id: int) -> None:
        with self.session_factory() as session:
            station = session.query(Station).filter(Station.id == station_id).first()
            if station:
                session.delete(station)
                session.commit()

    def update_station(self, station_id: int, **kwargs) -> Station:
        with self.session_factory() as session:
            station = session.query(Station).filter(Station.id == station_id).first()
            if station:
                for key, value in kwargs.items():
                    setattr(station, key, value)
                session.commit()
                session.refresh(station)
            return station
