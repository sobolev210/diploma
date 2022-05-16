# Generated by Django 3.2.8 on 2022-05-14 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20220514_1133'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название организации')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('abbreviation', models.CharField(blank=True, max_length=20, null=True, verbose_name='Аббревиатура')),
            ],
            options={
                'verbose_name': 'Организация',
                'verbose_name_plural': 'Организации',
            },
        ),
        migrations.RemoveField(
            model_name='field',
            name='abbreviation',
        ),
        migrations.AlterField(
            model_name='field',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fields', to='core.organization', verbose_name='Владелец'),
        ),
        migrations.DeleteModel(
            name='Organisation',
        ),
    ]