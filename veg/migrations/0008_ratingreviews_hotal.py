# Generated by Django 3.2.7 on 2022-05-18 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('veg', '0007_auto_20220518_1105'),
    ]

    operations = [
        migrations.AddField(
            model_name='ratingreviews',
            name='hotal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='veg.hotel'),
        ),
    ]
