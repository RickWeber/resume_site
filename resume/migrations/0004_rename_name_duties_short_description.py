# Generated by Django 4.0.4 on 2022-05-19 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_alter_duties_options_alter_skill_options_duties_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='duties',
            old_name='name',
            new_name='short_description',
        ),
    ]
