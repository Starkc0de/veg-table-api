# Generated by Django 3.2.7 on 2022-05-17 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('veg', '0003_auto_20220517_1711'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ChooseVeg',
            new_name='TypeVeg',
        ),
        migrations.RenameModel(
            old_name='Vegan_Veg',
            new_name='VeganVeg',
        ),
        migrations.AlterModelOptions(
            name='typeveg',
            options={'verbose_name_plural': 'TypeVeg'},
        ),
        migrations.AlterModelTable(
            name='typeveg',
            table='TypeVeg',
        ),
    ]