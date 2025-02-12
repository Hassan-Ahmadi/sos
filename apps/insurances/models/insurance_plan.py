from django.db import models
from .base import BaseModel


class InsurancePlan(BaseModel):
    """
    Insurance Plans like: Gold, Silver, etc.
    """
    name = models.CharField(max_length=255)
    unique_plan_id = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.name} - {self.unique_plan_id}"
