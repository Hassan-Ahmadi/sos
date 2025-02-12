from django.contrib import admin
from .models import *
from .models.person import Person
from .models.insurance_plan import InsurancePlan
from .models.insurance_company import InsuranceCompany
from .models.insurance_policy import InsurancePolicy
from .models.policy_holder import Policyholder


class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'father_name', 'email', 'national_id_number', 'birth_date', 'phone_number')


class PolicyHolderAdmin(admin.ModelAdmin):
    list_display = ('name', 'unique_policy_holder_id')


class InsurancePlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'unique_plan_id')


class InsuranceCompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'unique_id')


class InsurancePolicyAdmin(admin.ModelAdmin):
    list_display = ('person', 'insurance_company', 'insurance_plan', 'policy_holder', 'unique_policy_number', 'start_date', 'end_date')


admin.site.register(Person, PersonAdmin)
admin.site.register(InsurancePlan, InsurancePlanAdmin)
admin.site.register(InsuranceCompany, InsuranceCompanyAdmin)
admin.site.register(Policyholder, PolicyHolderAdmin)
admin.site.register(InsurancePolicy, InsurancePolicyAdmin)
