# Generated by Django 3.2.8 on 2022-04-03 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20220403_1733'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wellextraction',
            old_name='injection',
            new_name='gas_injection',
        ),
        migrations.AddField(
            model_name='wellextraction',
            name='water_injection',
            field=models.FloatField(default=1, max_length=50, verbose_name='Закачка'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wellextraction',
            name='year',
            field=models.IntegerField(default=2020, verbose_name='Год'),
            preserve_default=False,
        ),
    ]
