# Generated by Django 4.2.7 on 2023-12-17 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_project_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='github',
            field=models.CharField(blank=True, max_length=400),
        ),
    ]
