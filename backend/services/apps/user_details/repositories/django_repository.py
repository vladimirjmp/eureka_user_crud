# Standard Library
from datetime import date
from typing import Optional

# Django
from django.contrib.auth.models import User
from django.db import transaction

# Libraries
from user_details.exceptions import UserNotFound
from user_details.models import UserDetails
from user_details.repositories.base import AbstractUserRepository


class DjangoUserRepository(AbstractUserRepository):
    def get(self, id: int) -> Optional[dict]:
        user_details = (
            UserDetails.objects.select_related("user").filter(pk=id).first()
        )
        if not user_details:
            raise UserNotFound("User not found")

        output = user_details.__dict__ | user_details.user.__dict__
        output.update(is_admin=user_details.user.is_staff)

        return output

    @transaction.atomic()
    def create(
        self,
        first_name: str,
        last_name: str,
        email: str,
        phone_number: str,
        dob: date,
        address: str,
        username: str,
        password: str,
        is_admin: bool,
    ) -> int:
        user = self.__create_django_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password,
            is_admin=is_admin,
        )
        user_detail = UserDetails.objects.create(
            phone_number=phone_number, dob=dob, address=address, user=user
        )

        return user_detail.id

    @staticmethod
    def __create_django_user(
        *,
        first_name: str,
        last_name: str,
        username: str,
        email: str,
        password: str,
        is_admin: bool,
    ) -> User:
        user = User(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            is_superuser=is_admin,
            is_staff=is_admin,
        )
        user.set_password(password)
        user.save()

        return user
