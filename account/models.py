from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    CUSTOMER='C'
    RESTAURANT_OWNER='R'
    USER_TYPE_CHOICES=[
        (CUSTOMER,'Customer'),
         (RESTAURANT_OWNER,'Restaurant Owner'),
    ]
    user_type=models.Charfield(
        max_length=1,
        choices=USER_TYPE_CHOICES,
        default=CUSTOMER,
    )

