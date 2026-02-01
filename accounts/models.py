from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    # created empty to extend in future it helps me to modify user model later if needed
    def __str__(self):
        return self.username
