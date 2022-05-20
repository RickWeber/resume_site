# Generated by Django 4.0.4 on 2022-05-20 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0008_alter_certificate_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='degree',
            options={'ordering': ['year']},
        ),
        migrations.AlterModelOptions(
            name='duties',
            options={'ordering': ['order'], 'verbose_name': 'Duty', 'verbose_name_plural': 'Duties'},
        ),
        migrations.AddField(
            model_name='duties',
            name='order',
            field=models.IntegerField(default=1),
        ),
    ]