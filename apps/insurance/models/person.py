from django.db import models
from django.core.validators import validate_email
from phonenumber_field.modelfields import PhoneNumberField
from apps.insurance.models.base import BaseModel


class Person(BaseModel):
    """
    The Person model represents a person for whom an insurance policy is created.
    """
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, null=True, blank=True, validators=[validate_email])
    phone_number = PhoneNumberField()
    national_id_number = models.CharField(max_length=10, unique=True)
    birth_date = models.DateField()
    father_name = models.CharField(max_length=255, null=True, blank=True)
    issue_place = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
