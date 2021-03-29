# Generated by Django 3.1.5 on 2021-03-28 07:23

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('vaccine_app', '0004_auto_20210328_1215'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accesscontrollistdistrict',
            old_name='districtID',
            new_name='district',
        ),
        migrations.AlterUniqueTogether(
            name='accesscontrollistdistrict',
            unique_together={('person', 'district')},
        ),
        migrations.RenameModel(
            old_name='DistrictAdmin',
            new_name='District',
        ),
        migrations.CreateModel(
            name='Center',
            fields=[
                ('centerPrimaryKey', models.AutoField(primary_key=True, serialize=False)),
                ('centerId', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Center', to='vaccine_app.district')),
            ],
        ),
        migrations.AddField(
            model_name='accesscontrollistcenter',
            name='center',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='access_control_list_center', to='vaccine_app.center'),
        ),
        migrations.AlterField(
            model_name='centerregestration',
            name='center',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='centerRegestrations', to='vaccine_app.center'),
        ),
        migrations.AlterField(
            model_name='centervaccinedata',
            name='center',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='centerVaccine', to='vaccine_app.center'),
        ),
        migrations.AlterField(
            model_name='receiver',
            name='center',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='vaccine_app.center'),
        ),
        migrations.AlterUniqueTogether(
            name='accesscontrollistcenter',
            unique_together={('person', 'center')},
        ),
        migrations.RemoveField(
            model_name='accesscontrollistcenter',
            name='centerID',
        ),
        migrations.DeleteModel(
            name='CenterAdmin',
        ),
    ]