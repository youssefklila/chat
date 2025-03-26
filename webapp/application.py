"""Application module."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .ADM.machine_assets.erp_group.assign_station.endpoints import assign_stations_to_erpgrp_endpoint
from .ADM.machine_assets.erp_group.erp.endpoints import erp_endpoint
from .ADM.machine_assets.machine_setup.cell.endpoints import cell_endpoint
from .ADM.machine_assets.machine_setup.client.endpoints import client_endpoint
from .ADM.machine_assets.machine_setup.company_code.endpoints import company_code_endpoint
from .ADM.machine_assets.machine_setup.machine_group.endpoints import machine_group_endpoint
from .ADM.machine_assets.machine_setup.site.endpoints import site_endpoint
from webapp.ADM.machine_assets.machine_setup.station.endpoints import station_endpoint
from webapp.ADM.machine_assets.machine_setup.user.endpoints import user_endpoint
from .ADM.master_data.part_group.group.endpoints import part_group_endpoint
from .ADM.master_data.part_group.type.endpoints import part_group_type_endpoint
from .ADM.master_data.part_master.endpoints import part_master_endpoint
from .ADM.master_data.part_type.endpoints import part_type_endpoint
from .ADM.master_data.unit.endpoints import unit_endpoint
from .ADM.master_data.workplan_data.workplan.endpoints import workplan_endpoint
from .ADM.master_data.workplan_data.workplan_type.endpoints import workplan_type_endpoint
from .containers import Container
from webapp.auth.endpoints import router as auth_router
def create_app() -> FastAPI:
    container = Container()

    db = container.db()
    db.create_database()

    app = FastAPI()
    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.container = container
    # Include auth router
    app.include_router(auth_router, prefix="/auth", tags=["auth"])
    app.include_router(user_endpoint.router)
    app.include_router(client_endpoint.router)
    app.include_router(company_code_endpoint.router, prefix="/company_codes", tags=["Company Codes"])
    app.include_router(cell_endpoint.router, prefix="/cells", tags=["Cells"])
    app.include_router(site_endpoint.router, prefix="/sites", tags=["Sites"])
    app.include_router(machine_group_endpoint.router, prefix="/machine_groups", tags=["Machine Groups"])
    app.include_router(station_endpoint.router, prefix="/stations", tags=["Stations"])
    app.include_router(erp_endpoint.router, prefix="/erp_groups", tags=["ERP Groups"])
    app.include_router(assign_stations_to_erpgrp_endpoint.router, prefix="/assign_stations_to_erpgrp", tags=["ERP Groups"])
    app.include_router(part_type_endpoint.router, prefix="/part_types", tags=["Parts"])

    app.include_router(part_group_type_endpoint.router, prefix="/part_group_types", tags=["Parts"])

    app.include_router(part_group_endpoint.router, prefix="/part_group", tags=["Parts"])
    app.include_router(unit_endpoint.router, prefix="/units", tags=["Units"])
    app.include_router(part_master_endpoint.router, prefix="/part-master", tags=["Parts"])
    app.include_router(workplan_type_endpoint.router, prefix="/workplan-types", tags=["Work Plan"])
    app.include_router(workplan_endpoint.router, prefix="/workplan", tags=["Work Plan"])

    return app


app = create_app()
