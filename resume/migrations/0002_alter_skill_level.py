# Generated by Django 4.0.4 on 2022-05-18 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='level',
            field=models.CharField(choices=[('a', 'Advanced'), ('b', 'Intermediate'), ('c', 'Novice')], max_length=20),
        ),
    ]
