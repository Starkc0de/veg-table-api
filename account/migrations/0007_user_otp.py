# Generated by Django 3.2.7 on 2022-05-24 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_remove_user_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='otp',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
