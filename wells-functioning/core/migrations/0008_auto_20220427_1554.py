# Generated by Django 3.2.8 on 2022-04-27 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20220408_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='well',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Имя скважины'),
        ),
        migrations.AlterField(
            model_name='wellextraction',
            name='gas_rate',
            field=models.FloatField(max_length=50, verbose_name='Дебит газа, тыс м3/сут'),
        ),
        migrations.AlterField(
            model_name='wellextraction',
            name='liquid_rate',
            field=models.FloatField(max_length=50, verbose_name='Дебит жидкости, м3/сут'),
        ),
        migrations.AlterField(
            model_name='wellextraction',
            name='oil_rate',
            field=models.FloatField(max_length=50, verbose_name='Дебит нефти, т/cут'),
        ),
        migrations.AlterUniqueTogether(
            name='well',
            unique_together={('name', 'layer')},
        ),
    ]
