# Generated by Django 3.2 on 2023-09-08 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20230908_1304'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='status_code',
            field=models.IntegerField(null=True),
        ),
    ]
