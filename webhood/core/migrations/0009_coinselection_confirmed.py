# Generated by Django 4.2.5 on 2023-09-20 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_coinselection_transaction_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='coinselection',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
