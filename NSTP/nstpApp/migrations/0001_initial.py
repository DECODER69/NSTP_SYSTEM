# Generated by Django 4.0.1 on 2022-02-06 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='alphamodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('pdf', models.FileField(upload_to='pdf/')),
            ],
        ),
        migrations.CreateModel(
            name='bravomodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('pdf', models.FileField(upload_to='pdf/')),
            ],
        ),
        migrations.CreateModel(
            name='certifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cert_email', models.EmailField(max_length=254, null=True)),
                ('cert_fullname', models.CharField(max_length=100)),
                ('cert_course', models.CharField(max_length=20)),
                ('cert_datereq', models.CharField(max_length=20)),
                ('cert_document', models.CharField(max_length=20)),
                ('cert_status', models.CharField(choices=[('PENDING', 'PENDING'), ('APPROVED', 'APPROVED')], default='PENDING', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='charliemodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('pdf', models.FileField(upload_to='pdf/')),
            ],
        ),
        migrations.CreateModel(
            name='deltamodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('pdf', models.FileField(upload_to='pdf/')),
            ],
        ),
        migrations.CreateModel(
            name='echomodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('pdf', models.FileField(upload_to='pdf/')),
            ],
        ),
        migrations.CreateModel(
            name='foxtrotmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('pdf', models.FileField(upload_to='pdf/')),
            ],
        ),
        migrations.CreateModel(
            name='golfmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('pdf', models.FileField(upload_to='pdf/')),
            ],
        ),
        migrations.CreateModel(
            name='hotelmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('pdf', models.FileField(upload_to='pdf/')),
            ],
        ),
        migrations.CreateModel(
            name='indiamodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('pdf', models.FileField(upload_to='pdf/')),
            ],
        ),
        migrations.CreateModel(
            name='julietmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('pdf', models.FileField(upload_to='pdf/')),
            ],
        ),
        migrations.CreateModel(
            name='kilomodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('pdf', models.FileField(upload_to='pdf/')),
            ],
        ),
        migrations.CreateModel(
            name='limamodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('pdf', models.FileField(upload_to='pdf/')),
            ],
        ),
        migrations.CreateModel(
            name='registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idnum', models.CharField(default='', max_length=12, null=True)),
                ('lname', models.CharField(default='', max_length=20)),
                ('fname', models.CharField(default='', max_length=30)),
                ('minitial', models.CharField(default='', max_length=1)),
                ('address', models.CharField(default='', max_length=100)),
                ('cpnumber', models.DecimalField(decimal_places=0, default='', max_digits=11)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('gender', models.CharField(default='', max_length=6)),
                ('age', models.DecimalField(decimal_places=0, max_digits=3)),
                ('bdate', models.CharField(default='', max_length=15)),
                ('password', models.CharField(default='', max_length=20)),
                ('section', models.CharField(default='', max_length=20)),
                ('field', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='yves',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('pdf', models.FileField(upload_to='pdf/')),
            ],
        ),
    ]
