"""Services module."""

from typing import Iterator

from webapp.ADM.machine_assets.machine_setup.client.models.client_model import Client
from webapp.ADM.machine_assets.machine_setup.client.repositories.client_repositorie import ClientRepository


class ClientService:

    def __init__(self, client_repository: ClientRepository) -> None:
        self._repository = client_repository

    def get_clients(self) -> Iterator[Client]:
        return self._repository.get_all()

    def get_client_by_id(self, client_id: int) -> Client:
        return self._repository.get_by_id(client_id)

    def create_client(self, user_id: int, company_code: str, name: str, description: str) -> Client:
        return self._repository.add(user_id, company_code,name, description)

    def delete_client_by_id(self, client_id: int) -> None:
        return self._repository.delete_by_id(client_id)

    def update_client(self, client_id: int, user_id: int, company_code: str, name: str, description: str) -> Client:
        return self._repository.update_client(client_id, user_id, company_code, name, description)