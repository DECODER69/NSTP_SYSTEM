# Generated by Django 4.0.1 on 2022-01-27 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nstpApp', '0008_registration_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certifications',
            name='cert_email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
