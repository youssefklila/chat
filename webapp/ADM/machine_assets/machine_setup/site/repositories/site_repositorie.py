# repositories/site_repository.py

from contextlib import AbstractContextManager


from sqlalchemy.orm import Session
from typing import Callable, List

from webapp.ADM.machine_assets.machine_setup.site.models.site_model import Site


class SiteRepository:
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    def get_all(self) -> List[Site]:
        with self.session_factory() as session:
            return session.query(Site).all()

    def get_by_id(self, site_id: int) -> Site:
        with self.session_factory() as session:
            return session.query(Site).filter(Site.id == site_id).first()

    def add(self, user_id: int, company_code_id: int, site_number: str, site_external_number: str, deletion_priority: int, geo_coordinates: str, description: str) -> Site:
        with self.session_factory() as session:
            site = Site(
                user_id=user_id,
                company_code_id=company_code_id,
                site_number=site_number,
                site_external_number=site_external_number,
                deletion_priority=deletion_priority,
                geo_coordinates=geo_coordinates,
                description=description,
            )
            session.add(site)
            session.commit()
            session.refresh(site)
            return site

    def delete_by_id(self, site_id: int) -> None:
        with self.session_factory() as session:
            site = session.query(Site).filter(Site.id == site_id).first()
            if site:
                session.delete(site)
                session.commit()

    def update_site(self, site_id: int, **kwargs) -> Site:
        with self.session_factory() as session:
            site = session.query(Site).filter(Site.id == site_id).first()
            if site:
                for key, value in kwargs.items():
                    setattr(site, key, value)
                session.commit()
                session.refresh(site)
            return site
