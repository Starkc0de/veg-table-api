# Generated by Django 3.2.7 on 2022-05-17 11:22

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('veg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChooseVeg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choose_veg', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name_plural': 'ChooseVeg',
                'db_table': 'ChooseVeg',
            },
        ),
        migrations.AlterField(
            model_name='choosecountry',
            name='country',
            field=django_countries.fields.CountryField(default='AF', max_length=2),
        ),
    ]