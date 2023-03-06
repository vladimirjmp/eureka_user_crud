# Standard Library
import abc
from datetime import date
from typing import Optional


class AbstractUserRepository(abc.ABC):
    @abc.abstractmethod
    def get(self, id: int) -> Optional[dict]:
        raise NotImplementedError

    @abc.abstractmethod
    def create(
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
    ) -> int:
        raise NotImplementedError
