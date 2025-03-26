"""Containers module."""

from dependency_injector import containers, providers
from fastapi.security import OAuth2PasswordBearer

from webapp.ADM.machine_assets.erp_group.erp.repositories.erp_repositorie import ERPGroupRepository
from webapp.ADM.machine_assets.erp_group.erp.services.erp_service import ERPGroupService
from webapp.ADM.machine_assets.machine_setup.cell.repositories.cell_repositorie import CellRepository
from webapp.ADM.machine_assets.machine_setup.cell.services.cell_service import CellService
from webapp.ADM.machine_assets.machine_setup.client.repositories.client_repositorie import ClientRepository
from webapp.ADM.machine_assets.machine_setup.company_code.repositories.company_code_repositorie import CompanyCodeRepository
from webapp.ADM.machine_assets.machine_setup.company_code.services.company_code_service import CompanyCodeService
from webapp.ADM.machine_assets.machine_setup.machine_group.repositories.machine_group_repositorie import MachineGroupRepository
from webapp.ADM.machine_assets.machine_setup.machine_group.services.machine_group_service import MachineGroupService
from webapp.ADM.machine_assets.machine_setup.site.repositories.site_repositorie import SiteRepository
from webapp.ADM.machine_assets.machine_setup.site.services.site_service import SiteService
from webapp.ADM.machine_assets.machine_setup.station.repositories.station_repositorie import StationRepository
from webapp.ADM.machine_assets.machine_setup.station.services.station_service import StationService
from webapp.ADM.machine_assets.machine_setup.user.repositories.user_repositorie import UserRepository
from webapp.ADM.machine_assets.machine_setup.user.services.user_service import UserService
from webapp.ADM.machine_assets.erp_group.assign_station.repositories.assign_stations_to_erpgrp_repository import AssignStationsToErpGrpRepository
from webapp.ADM.machine_assets.erp_group.assign_station.services.assign_stations_to_erpgrp_service import AssignStationsToErpGrpService
from webapp.ADM.machine_assets.machine_setup.client.services.client_service import ClientService
from webapp.ADM.master_data.part_group.group.repositories.part_group_repository import PartGroupRepository
from webapp.ADM.master_data.part_group.group.services.part_group_service import PartGroupService
from webapp.ADM.master_data.part_group.type.repositories.part_group_type_repository import PartGroupTypeRepository
from webapp.ADM.master_data.part_group.type.services.part_group_type_service import PartGroupTypeService
from webapp.ADM.master_data.part_master.repositories.part_master_repository import PartMasterRepository
from webapp.ADM.master_data.part_master.services.part_master_service import PartMasterService
from webapp.ADM.master_data.part_type.repositories.part_type_repository import PartTypeRepository
from webapp.ADM.master_data.part_type.services.part_type_service import PartTypeService
from webapp.ADM.master_data.unit.repositories.unit_repository import UnitRepository
from webapp.ADM.master_data.unit.services.unit_service import UnitService
from webapp.ADM.master_data.workplan_data.workplan.repositories.workplan_repository import WorkPlanRepository
from webapp.ADM.master_data.workplan_data.workplan.services.workplan_service import WorkPlanService
from webapp.ADM.master_data.workplan_data.workplan_type.repositories.workplan_type_repository import WorkPlanTypeRepository
from webapp.ADM.master_data.workplan_data.workplan_type.services.workplan_type_service import WorkPlanTypeService
from webapp.database import Database # New import for auth service
from webapp.ADM.machine_assets.machine_setup.client.repositories.client_repositorie import ClientRepository
from webapp.ADM.machine_assets.machine_setup.client.services.client_service import ClientService
from dependency_injector import containers, providers
from webapp.auth.auth_service import AuthService
class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(
        modules=[
            "webapp.ADM.machine_assets.machine_setup.user.endpoints.user_endpoint",
            "webapp.ADM.machine_assets.machine_setup.client.endpoints.client_endpoint",
            "webapp.ADM.machine_assets.machine_setup.company_code.endpoints.company_code_endpoint",
            "webapp.ADM.machine_assets.machine_setup.cell.endpoints.cell_endpoint",
            "webapp.ADM.machine_assets.machine_setup.machine_group.endpoints.machine_group_endpoint",
            "webapp.ADM.machine_assets.machine_setup.site.endpoints.site_endpoint",
            "webapp.ADM.machine_assets.machine_setup.station.endpoints.station_endpoint",
            "webapp.ADM.machine_assets.erp_group.erp.endpoints.erp_endpoint",
            "webapp.ADM.machine_assets.erp_group.assign_station.endpoints.assign_stations_to_erpgrp_endpoint",
            "webapp.ADM.master_data.part_type.endpoints.part_type_endpoint",
            "webapp.ADM.master_data.part_group.type.endpoints.part_group_type_endpoint",
            "webapp.ADM.master_data.part_group.group.endpoints.part_group_endpoint",
            "webapp.ADM.master_data.unit.endpoints.unit_endpoint",
            "webapp.ADM.master_data.part_master.endpoints.part_master_endpoint",
            "webapp.ADM.master_data.workplan_data.workplan_type.endpoints.workplan_type_endpoint",
            "webapp.ADM.master_data.workplan_data.workplan.endpoints.workplan_endpoint",
            "webapp.auth.endpoints",  # Added auth endpoints to wiring config
            "webapp.ADM.machine_assets.machine_setup.client.endpoints.client_endpoint",
            "webapp.ADM.machine_assets.machine_setup.user.endpoints.user_endpoint",
        ]
    )

    # Authentication providers
    oauth2_scheme = providers.Object(OAuth2PasswordBearer(tokenUrl="auth/token"))

    config = providers.Configuration(yaml_files=["config.yml"])

    # Database
    db = providers.Singleton(Database, db_url=config.db.url)

    # Client Service
    client_repository = providers.Factory(
        ClientRepository,
        session_factory=db.provided.session,
    )

    client_service = providers.Factory(
        ClientService,
        client_repository=client_repository,
    )

    # User Service
    user_repository = providers.Factory(
        UserRepository,
        session_factory=db.provided.session,
    )

    user_service = providers.Factory(
        UserService,
        user_repository=user_repository,
    )

    # Auth Service
    auth_service = providers.Factory(
        AuthService,
        user_service=user_service,
    )

    # Company Code management
    company_code_repository = providers.Factory(
        CompanyCodeRepository,
        session_factory=db.provided.session,
    )

    company_code_service = providers.Factory(
        CompanyCodeService,
        company_code_repository=company_code_repository,
    )

    # Cell management
    cell_repository = providers.Factory(
        CellRepository,
        session_factory=db.provided.session,
    )

    cell_service = providers.Factory(
        CellService,
        cell_repository=cell_repository,
    )

    # Site management
    site_repository = providers.Factory(
        SiteRepository,
        session_factory=db.provided.session,
    )

    site_service = providers.Factory(
        SiteService,
        site_repository=site_repository,
    )

    # Machine Group management
    machine_group_repository = providers.Factory(
        MachineGroupRepository,
        session_factory=db.provided.session,
    )

    machine_group_service = providers.Factory(
        MachineGroupService,
        machine_group_repository=machine_group_repository,
    )

    # Station management
    station_repository = providers.Factory(
        StationRepository,
        session_factory=db.provided.session,
    )

    station_service = providers.Factory(
        StationService,
        station_repository=station_repository,
    )

    # ERP Group management
    erp_group_repository = providers.Factory(
        ERPGroupRepository,
        session_factory=db.provided.session,
    )

    erp_group_service = providers.Factory(
        ERPGroupService,
        erp_group_repository=erp_group_repository,
    )

    # Assign Stations to ERP Group
    assign_stations_to_erpgrp_repository = providers.Factory(
        AssignStationsToErpGrpRepository,
        session_factory=db.provided.session,
    )

    assign_stations_to_erpgrp_service = providers.Factory(
        AssignStationsToErpGrpService,
        assign_stations_to_erpgrp_repository=assign_stations_to_erpgrp_repository,
    )

    # Part Type management
    part_type_repository = providers.Factory(
        PartTypeRepository,
        session_factory=db.provided.session,
    )

    part_type_service = providers.Factory(
        PartTypeService,
        repository=part_type_repository,
    )

    # Part Group Type management
    part_group_type_repository = providers.Factory(
        PartGroupTypeRepository,
        session_factory=db.provided.session,
    )

    part_group_type_service = providers.Factory(
        PartGroupTypeService,
        repository=part_group_type_repository,
    )

    # Part Group management
    part_group_repository = providers.Factory(
        PartGroupRepository,
        session_factory=db.provided.session)

    part_group_service = providers.Factory(
        PartGroupService,
        part_group_repository=part_group_repository)

    # Unit management
    unit_repository = providers.Factory(
        UnitRepository,
        session_factory=db.provided.session,
    )

    unit_service = providers.Factory(
        UnitService,
        unit_repository=unit_repository,
    )

    # Part Master management
    part_master_repository = providers.Factory(
        PartMasterRepository,
        session_factory=db.provided.session,
    )

    part_master_service = providers.Factory(
        PartMasterService,
        part_master_repository=part_master_repository,
    )

    # Workplan Type management
    workplan_type_repository = providers.Factory(
        WorkPlanTypeRepository,
        session_factory=db.provided.session,
    )

    workplan_type_service = providers.Factory(
        WorkPlanTypeService,
        workplan_type_repository=workplan_type_repository,
    )

    # Workplan management
    work_plan_repository = providers.Factory(
        WorkPlanRepository,
        session_factory=db.provided.session,
    )

    work_plan_service = providers.Factory(
        WorkPlanService,
        repository=work_plan_repository,
    )