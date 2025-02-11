from django.db import models
from apps.insurances.models.base import BaseModel


class Policyholder(BaseModel):
    """
    The Company that is requesting the insurance policy for a person. like: Fanap, etc.
    """
    name = models.CharField(max_length=255)
    unique_policy_holder_id = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.name}"
