# Generated by Django 4.0.3 on 2022-03-28 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('instructor', models.CharField(max_length=255)),
                ('fees', models.FloatField(max_length=10)),
                ('mode', models.CharField(max_length=10)),
                ('duration', models.IntegerField(max_length=10)),
            ],
        ),
    ]
