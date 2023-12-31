# Generated by Django 4.1.3 on 2023-07-20 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('idPerson', models.BigAutoField(primary_key=True, serialize=False, unique=True)),
                ('login', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=20)),
                ('secondName', models.CharField(max_length=20)),
                ('thirdName', models.CharField(max_length=20)),
                ('contrie', models.CharField(max_length=30)),
                ('region', models.CharField(max_length=40)),
                ('photo', models.ImageField(upload_to='')),
                ('role', models.IntegerField()),
                ('RegistrationDate', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'Users',
            },
        ),
    ]
