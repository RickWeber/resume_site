# Generated by Django 4.0.4 on 2022-05-19 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0005_remove_experience_location_remove_duties_job_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blurb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blurb', models.TextField()),
            ],
        ),
    ]