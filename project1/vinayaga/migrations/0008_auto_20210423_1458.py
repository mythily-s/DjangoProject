# Generated by Django 3.1.6 on 2021-04-23 09:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vinayaga', '0007_buyer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='Company_address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='detail',
            name='Company_name',
            field=models.CharField(blank=True, max_length=40, null=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only  characters are allowed.')]),
        ),
        migrations.AlterField(
            model_name='detail',
            name='Email',
            field=models.CharField(max_length=20, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')]),
        ),
        migrations.AlterField(
            model_name='detail',
            name='Landmark',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
