# Generated by Django 4.0.3 on 2022-03-29 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('producer', models.CharField(max_length=255)),
                ('duration', models.FloatField()),
                ('image_url', models.CharField(max_length=2083)),
                ('rated', models.CharField(max_length=3)),
                ('info', models.CharField(max_length=100)),
            ],
        ),
    ]
