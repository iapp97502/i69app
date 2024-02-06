# Generated by Django 3.1.5 on 2022-04-14 13:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("chat", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="NotificationSettings",
            fields=[
                (
                    "id",
                    models.CharField(max_length=5, primary_key=True, serialize=False),
                ),
                ("title", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Notification",
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
                ("priority", models.IntegerField(null=True)),
                ("created_date", models.DateTimeField(auto_now_add=True, null=True)),
                ("app_url", models.CharField(blank=True, max_length=100, null=True)),
                ("seen", models.BooleanField(default=False)),
                ("notification_body", models.CharField(max_length=1000, null=True)),
                ("data", models.CharField(max_length=500, null=True)),
                (
                    "notification_setting",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="chat.notificationsettings",
                    ),
                ),
                (
                    "sender",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="notification_sender",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
