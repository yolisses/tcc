# Generated by Django 4.1 on 2022-09-01 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advisor',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('given_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('lattes', models.URLField()),
            ],
        ),
    ]
