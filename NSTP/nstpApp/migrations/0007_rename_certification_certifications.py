# Generated by Django 4.0.1 on 2022-01-27 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nstpApp', '0006_alter_certification_cert_course_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='certification',
            new_name='certifications',
        ),
    ]