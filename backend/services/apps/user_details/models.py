# Django
from django.db import models


class UserDetails(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    class Meta:
        db_table = "user_details"
