# Generated by Django 4.0.4 on 2022-05-20 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0010_alter_duties_options_rename_order_duties_list_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='certificate',
            options={'ordering': ['-date']},
        ),
        migrations.AlterModelOptions(
            name='degree',
            options={'ordering': ['-year']},
        ),
    ]