# Generated by Django 3.0.7 on 2021-03-15 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CenterAdmin',
            fields=[
                ('centerId', models.AutoField(primary_key=True, serialize=False)),
                ('userName', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='DistrictAdmin',
            fields=[
                ('districtId', models.AutoField(primary_key=True, serialize=False)),
                ('userName', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Receiver',
            fields=[
                ('aadharNumber', models.CharField(max_length=16, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('contactNumber', models.CharField(max_length=12)),
                ('address', models.CharField(max_length=1000, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='vaccine_app.CenterAdmin')),
            ],
        ),
        migrations.CreateModel(
            name='VaccineLot',
            fields=[
                ('lotId', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('produced', 'produced'), ('atDistrict', 'atDistrict'), ('atCenter', 'atCenter'), ('consumed', 'consumed')], default='produced', max_length=10)),
                ('productionTimestamp', models.DateTimeField(auto_now_add=True)),
                ('departureTimestamp', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ReceiverVaccination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointmentDate', models.DateField(auto_now_add=True)),
                ('vaccineDose', models.BooleanField(default=False)),
                ('lot', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='receiverVaccination', to='vaccine_app.VaccineLot')),
                ('receiver', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='receiverVaccination', to='vaccine_app.Receiver')),
            ],
        ),
        migrations.CreateModel(
            name='DistrictVaccineData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrivalTimestamp', models.DateTimeField(auto_now_add=True)),
                ('departureTimestamp', models.DateTimeField()),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='districtVaccine', to='vaccine_app.DistrictAdmin')),
                ('lot', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='districtVaccine', to='vaccine_app.VaccineLot')),
            ],
        ),
        migrations.CreateModel(
            name='CenterVaccineData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrivalTimestamp', models.DateTimeField(auto_now_add=True)),
                ('departureTimestamp', models.DateTimeField()),
                ('center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='centerVaccine', to='vaccine_app.CenterAdmin')),
                ('lot', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='centerVaccine', to='vaccine_app.VaccineLot')),
            ],
        ),
        migrations.CreateModel(
            name='CenterRegestration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('center', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='centerRegestrations', to='vaccine_app.CenterAdmin')),
            ],
        ),
        migrations.AddField(
            model_name='centeradmin',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='centerAdmin', to='vaccine_app.DistrictAdmin'),
        ),
    ]
