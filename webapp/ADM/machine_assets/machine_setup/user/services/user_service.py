"""User service implementation."""
from typing import Iterator, Optional
from uuid import uuid4
from webapp.auth.service import get_password_hash
from webapp.ADM.machine_assets.machine_setup.user.models.user_model import User
from webapp.ADM.machine_assets.machine_setup.user.repositories.user_repositorie import (
    UserRepository,
    NotFoundError,
)

class UserService:
    """Service for handling user operations."""

    def __init__(self, user_repository: UserRepository) -> None:
        """Initialize with user repository dependency."""
        self._repository: UserRepository = user_repository

    def get_users(self) -> Iterator[User]:
        """Get all users."""
        return self._repository.get_all()

    def get_user_by_id(self, user_id: int) -> User:
        """Get a user by ID."""
        return self._repository.get_by_id(user_id)

    def create_user(self, email: str, password: str, is_active: bool = True) -> User:
        """Create a new user with hashed password."""
        hashed_password = get_password_hash(password)
        return self._repository.add(email, hashed_password, is_active)

    def delete_user_by_id(self, user_id: int) -> None:
        """Delete a user by ID."""
        return self._repository.delete_by_id(user_id)

    def update_user(
        self,
        user_id: int,
        email: Optional[str] = None,
        password: Optional[str] = None,
        is_active: Optional[bool] = None,
    ) -> User:
        """Update user information."""
        hashed_password = get_password_hash(password) if password else None
        return self._repository.update_user(user_id, email, hashed_password, is_active)

    def get_user_by_email(self, email: str) -> User:
        """Get a user by email."""
        return self._repository.get_by_email(email)