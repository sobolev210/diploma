# Generated by Django 3.2.8 on 2022-04-03 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20220403_0808'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cluster',
            options={'verbose_name': 'Куст', 'verbose_name_plural': 'Кусты'},
        ),
        migrations.AlterModelOptions(
            name='fluidproperties',
            options={'verbose_name': 'Свойства флюидов', 'verbose_name_plural': 'Свойства флюидов'},
        ),
        migrations.AlterModelOptions(
            name='layer',
            options={'verbose_name': 'Пласт', 'verbose_name_plural': 'Пласты'},
        ),
        migrations.RemoveField(
            model_name='layer',
            name='porosity',
        ),
        migrations.AlterField(
            model_name='well',
            name='layer',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='wells', to='core.layer', verbose_name='Пласт'),
            preserve_default=False,
        ),
    ]