# Generated by Django 3.2.8 on 2022-05-15 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20220514_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='field',
            name='x_coordinate',
            field=models.FloatField(default=0, max_length=50, verbose_name='Координата Х'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='field',
            name='y_coordinate',
            field=models.FloatField(default=0, max_length=50, verbose_name='Координата Y'),
            preserve_default=False,
        ),
    ]
