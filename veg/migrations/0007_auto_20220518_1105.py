# Generated by Django 3.2.7 on 2022-05-18 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('veg', '0006_auto_20220518_1037'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodOnlineOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('discriptiion', models.TextField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='veg.hotel')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.user')),
            ],
            options={
                'verbose_name_plural': 'FoodOnlineOrder',
                'db_table': 'FoodOnlineOrder',
            },
        ),
        migrations.RenameField(
            model_name='gallery',
            old_name='vagan',
            new_name='hotal',
        ),
        migrations.DeleteModel(
            name='OrderOnline',
        ),
    ]