# Generated by Django 4.0.1 on 2022-01-28 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nstpApp', '0011_alter_certifications_cert_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='certifications',
            old_name='cert_email',
            new_name='idnumber',
        ),
    ]
