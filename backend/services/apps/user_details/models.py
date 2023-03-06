# Django
from django.contrib.auth.models import User
from django.db import models


class UserDetails(models.Model):
    phone_number = models.CharField(max_length=9)
    dob = models.DateField()
    address = models.CharField(max_length=300)
    user = models.OneToOneField(
        User, on_delete=models.PROTECT, related_name="user_detail"
    )

    class Meta:
        db_table = "user_details"
