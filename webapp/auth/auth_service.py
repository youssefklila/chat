"""Authentication service with dependencies."""
from datetime import timedelta
from typing import Optional
from webapp.auth.service import AuthCore
from webapp.ADM.machine_assets.machine_setup.user.models.user_model import User

class AuthService:
    def __init__(self, user_service):
        self.user_service = user_service
        self.core = AuthCore()

    async def authenticate_user(self, email: str, password: str) -> Optional[User]:
        """Authenticate a user with email/password."""
        try:
            user = self.user_service.get_user_by_email(email)
            if not self.core.verify_password(password, user.hashed_password):
                return None
            return user
        except Exception:
            return None

    def create_user_token(self, user: User) -> dict:
        """Generate JWT token for authenticated user."""
        access_token_expires = timedelta(minutes=30)  # Using direct value
        return {
            "access_token": self.core.create_access_token(
                data={"sub": user.email},
                expires_delta=access_token_expires
            ),
            "token_type": "bearer"
        }