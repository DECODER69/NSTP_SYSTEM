# Generated by Django 4.0.1 on 2022-02-21 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nstpApp', '0003_extenduser_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extenduser',
            name='status',
            field=models.CharField(choices=[('PENDING', 'PENDING'), ('ENROLLED', 'ENROLLED')], default='PENDING', max_length=10),
        ),
    ]
