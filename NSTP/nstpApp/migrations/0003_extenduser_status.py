# Generated by Django 4.0.1 on 2022-02-20 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nstpApp', '0002_certifications_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='extenduser',
            name='status',
            field=models.CharField(choices=[('PENDING', 'PENDING'), ('APPROVED', 'APPROVED')], default='PENDING', max_length=10),
        ),
    ]
