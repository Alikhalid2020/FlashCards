# Generated by Django 3.1.5 on 2021-01-29 01:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashapp', '0006_card_deck'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='date_created',
            field=models.DateField(default=datetime.date(1945, 8, 1)),
        ),
    ]
