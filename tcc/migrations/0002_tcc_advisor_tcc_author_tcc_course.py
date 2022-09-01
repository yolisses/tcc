# Generated by Django 4.1 on 2022-09-01 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
        ('advisor', '0001_initial'),
        ('course', '0001_initial'),
        ('tcc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tcc',
            name='advisor',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='advisor.advisor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tcc',
            name='author',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='author.author'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tcc',
            name='course',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='course.course'),
            preserve_default=False,
        ),
    ]