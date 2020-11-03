# Generated by Django 3.1.1 on 2020-11-02 21:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_task_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='amount',
            field=models.PositiveBigIntegerField(validators=[django.core.validators.MaxValueValidator(281474976710656), django.core.validators.MinValueValidator(1)]),
        ),
    ]
