# Generated by Django 3.1.5 on 2023-03-20 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0025_auto_20230316_0612'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='paymentgatewayforregion',
            unique_together={('payment_gateway', 'region')},
        ),
    ]
