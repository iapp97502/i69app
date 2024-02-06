# Generated by Django 3.1.5 on 2022-10-31 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("defaultPicker", "0002_language"),
        ("user", "0028_auto_20221029_1627"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="user_language_code",
            field=models.CharField(
                blank=True, default="en", editable=False, max_length=5, null=True
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="language",
            field=models.ManyToManyField(blank=True, to="defaultPicker.language"),
        ),
    ]
