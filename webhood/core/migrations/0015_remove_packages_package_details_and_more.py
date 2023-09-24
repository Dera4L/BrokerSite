# Generated by Django 4.2.5 on 2023-09-24 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_alter_packages_package_range2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='packages',
            name='package_details',
        ),
        migrations.AddField(
            model_name='packages',
            name='package_details1',
            field=models.CharField(default='features', max_length=400),
        ),
        migrations.AddField(
            model_name='packages',
            name='package_details2',
            field=models.CharField(default='features', max_length=400),
        ),
        migrations.AddField(
            model_name='packages',
            name='package_details3',
            field=models.CharField(default='features', max_length=400),
        ),
        migrations.AddField(
            model_name='packages',
            name='package_details4',
            field=models.CharField(default='features', max_length=400),
        ),
    ]
