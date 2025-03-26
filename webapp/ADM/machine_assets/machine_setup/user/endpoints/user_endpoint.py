"""Endpoints module."""

from fastapi import APIRouter, Depends, Response, status, HTTPException
from dependency_injector.wiring import inject, Provide
from webapp.auth.dependencies import get_current_user  # Updated import path
from webapp.auth.schemas import UserCreate, UserUpdate, UserInDB  # Updated import path
from webapp.containers import Container
from webapp.ADM.machine_assets.machine_setup.user.services.user_service import UserService
from webapp.ADM.machine_assets.machine_setup.user.repositories.user_repositorie import NotFoundError
from webapp.ADM.machine_assets.machine_setup.user.models.user_model import User  # Added import

router = APIRouter()

@router.get("/users", response_model=list[UserInDB], tags=["Users"])
@inject
def get_list(
    user_service: UserService = Depends(Provide[Container.user_service]),
    current_user: User = Depends(get_current_user),
):
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return user_service.get_users()

@router.get("/users/{user_id}", response_model=UserInDB, tags=["Users"])
@inject
def get_by_id(
    user_id: int,
    user_service: UserService = Depends(Provide[Container.user_service]),
    current_user: User = Depends(get_current_user),
):
    try:
        user = user_service.get_user_by_id(user_id)
        if not current_user.is_active:
            raise HTTPException(status_code=400, detail="Inactive user")
        return user
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)

@router.post("/users", status_code=status.HTTP_201_CREATED, response_model=UserInDB, tags=["Users"])
@inject
def add(
    user_data: UserCreate,
    user_service: UserService = Depends(Provide[Container.user_service]),
):
    try:
        existing_user = user_service.get_user_by_email(user_data.email)
        raise HTTPException(status_code=400, detail="Email already registered")
    except NotFoundError:
        pass

    return user_service.create_user(
        email=user_data.email,
        password=user_data.password,
        is_active=user_data.is_active
    )

@router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Users"])
@inject
def remove(
    user_id: int,
    user_service: UserService = Depends(Provide[Container.user_service]),
    current_user: User = Depends(get_current_user),
):
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    try:
        user_service.delete_user_by_id(user_id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/users/{user_id}", response_model=UserInDB, tags=["Users"])
@inject
def update(
    user_id: int,
    user_data: UserUpdate,
    user_service: UserService = Depends(Provide[Container.user_service]),
    current_user: User = Depends(get_current_user),
):
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    try:
        user = user_service.update_user(
            user_id,
            email=user_data.email,
            password=user_data.password,
            is_active=user_data.is_active
        )
        return user
    except NotFoundError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@router.get("/users/email/{email}", response_model=UserInDB, tags=["Users"])
@inject
def get_by_email(
    email: str,
    user_service: UserService = Depends(Provide[Container.user_service]),
    current_user: User = Depends(get_current_user),
):
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    try:
        return user_service.get_user_by_email(email)
    except NotFoundError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@router.get("/users/me/", response_model=UserInDB)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user