# Generated by Django 4.0.1 on 2022-02-06 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nstpApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='yves',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
