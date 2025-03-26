# services/station_service.py

from typing import List
from webapp.ADM.machine_assets.machine_setup.station.models.station_model import Station
from webapp.ADM.machine_assets.machine_setup.station.repositories.station_repositorie import StationRepository

class StationService:
    def __init__(self, station_repository: StationRepository) -> None:
        self.station_repository = station_repository

    def get_all_stations(self) -> List[Station]:
        return self.station_repository.get_all()

    def get_station_by_id(self, station_id: int) -> Station:
        return self.station_repository.get_by_id(station_id)

    def add_station(self, machine_group_id: int, name: str, description: str, is_active: bool, user_id: int, info: str) -> Station:
        return self.station_repository.add(machine_group_id, name, description, is_active, user_id, info)

    def delete_station(self, station_id: int) -> None:
        self.station_repository.delete_by_id(station_id)

    def update_station(self, station_id: int, **kwargs) -> Station:
        return self.station_repository.update_station(station_id, **kwargs)
