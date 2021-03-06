# Generated by Django 4.0.4 on 2022-05-18 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('issuer', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
                ('industry', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProfessionalSummary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('elevator_pitch', models.CharField(blank=True, max_length=250, null=True)),
                ('tech_skills', models.CharField(blank=True, max_length=250, null=True)),
                ('soft_skills', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=40, null=True)),
                ('comments', models.CharField(blank=True, max_length=100, null=True)),
                ('level', models.CharField(choices=[('', 'Advanced'), ('', 'Intermediate'), ('', 'Novice')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
                ('start', models.CharField(max_length=35)),
                ('end', models.CharField(max_length=35)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.organization')),
            ],
        ),
        migrations.CreateModel(
            name='Duties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=250)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.experience')),
            ],
        ),
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('degree', models.CharField(max_length=50)),
                ('year', models.DateField()),
                ('distinctions', models.CharField(max_length=30)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume.organization')),
            ],
        ),
    ]
