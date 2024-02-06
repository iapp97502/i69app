# Generated by Django 3.1.5 on 2023-03-20 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0064_auto_20230308_1101'),
    ]

    operations = [
        migrations.CreateModel(
            name='SetInterestedInRegion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('countries', models.ManyToManyField(to='user.Country')),
            ],
        ),
        migrations.CreateModel(
            name='UserInterestForRegion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.setinterestedinregion')),
                ('user_interested_in', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.userinterestedin')),
            ],
            options={
                'unique_together': {('user_interested_in', 'region')},
            },
        ),
    ]
