# Generated by Django 4.0.4 on 2022-05-19 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_alter_skill_level'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='duties',
            options={'verbose_name': 'Duty', 'verbose_name_plural': 'Duties'},
        ),
        migrations.AlterModelOptions(
            name='skill',
            options={'verbose_name': 'Skill', 'verbose_name_plural': 'Skills'},
        ),
        migrations.AddField(
            model_name='duties',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='degree',
            name='distinctions',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
