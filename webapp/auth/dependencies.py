from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from dependency_injector.wiring import inject, Provide
from webapp.containers import Container
from webapp.auth.schemas import TokenData
from webapp.ADM.machine_assets.machine_setup.user.services.user_service import UserService
from webapp.ADM.machine_assets.machine_setup.user.repositories.user_repositorie import UserNotFoundError
from webapp.ADM.machine_assets.machine_setup.user.models.user_model import User

# Configuration
SECRET_KEY = "your-secret-key-here"  # Make sure this matches your token service
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")


@inject
async def get_current_user(
        token: str = Depends(oauth2_scheme),  # Use the scheme directly, not through container
        user_service: UserService = Depends(Provide[Container.user_service]),
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except JWTError as e:
        print(f"JWT Error: {str(e)}")  # Helpful for debugging
        raise credentials_exception

    try:
        return user_service.get_user_by_email(email=token_data.email)
    except UserNotFoundError:
        raise credentials_exception