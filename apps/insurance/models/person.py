from django.db import models
from django.core.validators import validate_email
from phonenumber_field.modelfields import PhoneNumberField
from .base import BaseModel


class Person(BaseModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, null=True, blank=True, validators=[validate_email])
    phone_number = PhoneNumberField()
    national_id_number = models.CharField(max_length=10, unique=True)
    birth_date = models.DateField()
    father_name = models.CharField(max_length=255, null=True, blank=True)
    issue_place = models.CharField(max_length=255, null=True, blank=True)
