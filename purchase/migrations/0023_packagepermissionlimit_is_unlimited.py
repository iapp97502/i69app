# Generated by Django 3.1.5 on 2022-12-26 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("purchase", "0022_auto_20221226_1101"),
    ]

    operations = [
        migrations.AddField(
            model_name="packagepermissionlimit",
            name="is_unlimited",
            field=models.BooleanField(default=False),
        ),
    ]