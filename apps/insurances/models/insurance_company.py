from django.db import models
from .base import BaseModel


class InsuranceCompany(BaseModel):
    """
    Insurance Companies like: Pasargad, Hekmat, etc.
    """
    name = models.CharField(max_length=255)
    unique_id = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.name}"
