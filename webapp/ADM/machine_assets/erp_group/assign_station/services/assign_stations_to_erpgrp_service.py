# services/assign_stations_to_erpgrp_service.py

from typing import List
from webapp.ADM.machine_assets.erp_group.assign_station.models.assign_stations_to_erpgrp_model import AssignStationsToErpGrp
from webapp.ADM.machine_assets.erp_group.assign_station.repositories.assign_stations_to_erpgrp_repository import AssignStationsToErpGrpRepository

class AssignStationsToErpGrpService:
    def __init__(self, assign_stations_to_erpgrp_repository: AssignStationsToErpGrpRepository) -> None:
        self.assign_stations_to_erpgrp_repository = assign_stations_to_erpgrp_repository

    def get_all_assignments(self) -> List[AssignStationsToErpGrp]:
        return self.assign_stations_to_erpgrp_repository.get_all()

    def get_assignment_by_id(self, assign_id: int) -> AssignStationsToErpGrp:
        return self.assign_stations_to_erpgrp_repository.get_by_id(assign_id)

    def get_assignments_by_station_id(self, station_id: int) -> List[AssignStationsToErpGrp]:
        return self.assign_stations_to_erpgrp_repository.get_by_station_id(station_id)

    def add_assignment(self, station_id: int, erp_group_id: int, station_type: str, user_id: int) -> AssignStationsToErpGrp:
        return self.assign_stations_to_erpgrp_repository.add(station_id, erp_group_id, station_type, user_id)

    def delete_assignment(self, assign_id: int) -> None:
        self.assign_stations_to_erpgrp_repository.delete_by_id(assign_id)
