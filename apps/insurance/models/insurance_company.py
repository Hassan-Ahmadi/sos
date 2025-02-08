from django.db import models
from .base import BaseModel


class InsuranceCompany(BaseModel):
    name = models.CharField(max_length=255)
    unique_id = models.CharField(max_length=255, unique=True)
