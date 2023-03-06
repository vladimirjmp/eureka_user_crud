# Standard Library
from datetime import date
from typing import Optional

# Libraries
from user_details.repositories.base import AbstractUserRepository


class UserServices:
    def __init__(self, repository: AbstractUserRepository):
        self.repository = repository

    def get_user(self, *, id: int) -> Optional[dict]:
        return self.repository.get(id)

    def create_user(
        self,
        *,
        first_name: str,
        last_name: str,
        email: str,
        phone_number: str,
        dob: date,
        address: str,
        username: str,
        password: str,
        is_admin: bool,
    ) -> dict:
        user_id = self.repository.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            dob=dob,
            address=address,
            username=username,
            password=password,
            is_admin=is_admin,
        )

        return dict(user_id=user_id)
