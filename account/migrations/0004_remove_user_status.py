# Generated by Django 3.2.7 on 2022-05-19 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_user_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='status',
        ),
    ]
