# Generated by Django 3.1.5 on 2021-03-28 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaccine_app', '0002_auto_20210328_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='districtvaccinedata',
            name='departureTimestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
