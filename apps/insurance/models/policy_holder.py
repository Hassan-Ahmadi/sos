from django.db import models
from .base import BaseModel


class Policyholder(BaseModel):
    name = models.CharField(max_length=255)
    unique_policy_holder_id = models.CharField(max_length=255, unique=True)

