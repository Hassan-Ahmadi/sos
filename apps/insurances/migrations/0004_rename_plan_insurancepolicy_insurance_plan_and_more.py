# Generated by Django 5.1.6 on 2025-02-12 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insurances', '0003_insurancepolicy_plan'),
    ]

    operations = [
        migrations.RenameField(
            model_name='insurancepolicy',
            old_name='plan',
            new_name='insurance_plan',
        ),
        migrations.RenameField(
            model_name='insurancepolicy',
            old_name='policyholder',
            new_name='policy_holder',
        ),
    ]
