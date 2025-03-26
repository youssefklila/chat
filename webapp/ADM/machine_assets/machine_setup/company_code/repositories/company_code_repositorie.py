# repositories/company_code_repository.py

from contextlib import AbstractContextManager
from sqlalchemy.orm import Session
from typing import Callable, List

from webapp.ADM.machine_assets.machine_setup.company_code.models.company_code_model import CompanyCode


class CompanyCodeRepository:
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    def get_all(self) -> List[CompanyCode]:
        with self.session_factory() as session:
            return session.query(CompanyCode).all()

    def get_by_id(self, company_code_id: int) -> CompanyCode:
        with self.session_factory() as session:
            return session.query(CompanyCode).filter(CompanyCode.id == company_code_id).first()

    def add(self, user_id: int, client_id: int, name: str, description: str) -> CompanyCode:
        with self.session_factory() as session:
            company_code = CompanyCode(user_id=user_id, client_id=client_id, name=name, description=description)
            session.add(company_code)
            session.commit()
            session.refresh(company_code)
            return company_code

    def delete_by_id(self, company_code_id: int) -> None:
        with self.session_factory() as session:
            company_code = session.query(CompanyCode).filter(CompanyCode.id == company_code_id).first()
            if company_code:
                session.delete(company_code)
                session.commit()

    def update_company_code(self, company_code_id: int, **kwargs) -> CompanyCode:
        with self.session_factory() as session:
            company_code = session.query(CompanyCode).filter(CompanyCode.id == company_code_id).first()
            if company_code:
                for key, value in kwargs.items():
                    setattr(company_code, key, value)
                session.commit()
                session.refresh(company_code)
            return company_code
