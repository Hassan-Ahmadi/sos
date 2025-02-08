from django.db import models
from .base import BaseModel


class InsurancePlan(BaseModel):
    name = models.CharField(max_length=255)
    unique_plan_id = models.CharField(max_length=255, unique=True)

