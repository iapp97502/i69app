# Generated by Django 3.1.5 on 2023-04-29 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0072_auto_20230413_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Male'), (1, 'Female'), (2, 'Prefer not to say')], null=True),
        ),
    ]