from django.db import models
from .base import BaseModel
from .person import Person
from .insurance_company import InsuranceCompany
from .policy_holder import Policyholder
from .insurance_plan import InsurancePlan


class InsurancePolicy(BaseModel):
    """
    Insurance plan for a person from an insurance company.
    """
    person = models.ForeignKey(Person, on_delete=models.PROTECT)
    insurance_company = models.ForeignKey(InsuranceCompany, on_delete=models.PROTECT)
    policy_holder = models.ForeignKey(Policyholder, on_delete=models.PROTECT)
    insurance_plan = models.ForeignKey(InsurancePlan, on_delete=models.PROTECT, null=True, blank=True)
    unique_policy_number = models.CharField(max_length=255, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    confirmation_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.person} - {self.insurance_company} Insurance - {self.policy_holder} Company"
