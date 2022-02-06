# Generated by Django 4.0.1 on 2022-02-05 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nstpApp', '0023_alter_certifications_cert_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='alpha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('pdf', models.FileField(upload_to='pdf/')),
            ],
        ),
        migrations.DeleteModel(
            name='platoons',
        ),
    ]
