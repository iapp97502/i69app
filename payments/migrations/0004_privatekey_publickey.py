# Generated by Django 3.1.5 on 2022-10-28 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payments", "0003_auto_20221028_1535"),
    ]

    operations = [
        migrations.CreateModel(
            name="PrivateKey",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "payment_gateway",
                    models.CharField(choices=[("boku", "Boku")], max_length=65),
                ),
                ("key_text", models.TextField()),
                ("modified_on", models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="PublicKey",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "payment_gateway",
                    models.CharField(choices=[("boku", "Boku")], max_length=65),
                ),
                ("key_text", models.TextField()),
                ("modified_on", models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
