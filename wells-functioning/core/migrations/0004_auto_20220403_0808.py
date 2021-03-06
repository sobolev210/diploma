# Generated by Django 3.2.8 on 2022-04-03 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20220221_1450'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cluster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название куста')),
                ('x_coordinate', models.FloatField(max_length=50, verbose_name='Координата Х')),
                ('y_coordinate', models.FloatField(max_length=50, verbose_name='Координата Y')),
            ],
        ),
        migrations.CreateModel(
            name='CoreSample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sample_number', models.PositiveIntegerField(unique=True, verbose_name='Номер образца')),
                ('sampling_date', models.DateField(verbose_name='Дата отбора керна')),
                ('sampling_method', models.CharField(max_length=255, verbose_name='Способ отбора керна')),
                ('gas_connected_porosity', models.FloatField(max_length=50, verbose_name='Открытая пористость по газу')),
                ('water_connected_porosity', models.FloatField(max_length=50, verbose_name='Открытая пористость по воде')),
                ('kerosene_connected_porosity', models.FloatField(max_length=50, verbose_name='Открытая пористость по керосину')),
                ('young_modulus', models.FloatField(max_length=50, verbose_name='Модуль Юнга')),
                ('poissons_ratio', models.FloatField(max_length=50, verbose_name='Коэффициент Пуассона')),
            ],
            options={
                'verbose_name': 'Керны',
                'verbose_name_plural': 'Керны',
            },
        ),
        migrations.CreateModel(
            name='FluidProperties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gas_factor', models.FloatField(max_length=50, verbose_name='Газовый фактор')),
                ('water_dynamic_viscosity', models.FloatField(max_length=50, verbose_name='Динамическая вязкость воды')),
                ('oil_dynamic_viscosity', models.FloatField(max_length=50, verbose_name='Динамическая вязкость нефти')),
                ('gas_dynamic_viscosity', models.FloatField(max_length=50, verbose_name='Динамическая вязкость газа')),
                ('water_density', models.FloatField(max_length=50, verbose_name='Плотность воды')),
                ('oil_density', models.FloatField(max_length=50, verbose_name='Плотность нефти')),
                ('gas_density', models.FloatField(max_length=50, verbose_name='Плотность газа')),
                ('formation_volume_factor_for_water', models.FloatField(max_length=50, verbose_name='Объемный коэффициент воды')),
                ('formation_volume_factor_for_oil', models.FloatField(max_length=50, verbose_name='Объемный коэффициент нефти')),
            ],
        ),
        migrations.CreateModel(
            name='Layer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название пласта')),
                ('reservoir_type', models.CharField(max_length=255, verbose_name='Тип коллектора')),
                ('layer_pressure', models.FloatField(max_length=50, verbose_name='Пластовое давление')),
                ('bed_top_occurrence_depth', models.FloatField(max_length=50, verbose_name='Глубина залегания кровли')),
                ('bed_floor_occurrence_depth', models.FloatField(max_length=50, verbose_name='Глубина залегания подошвы')),
                ('net_oil_thickness', models.FloatField(max_length=50, verbose_name='Эффективная нефтенасыщенная толщина')),
                ('porosity', models.FloatField(max_length=50, verbose_name='Пористость')),
                ('full_porosity_ratio', models.FloatField(max_length=50, verbose_name='Коэффициент полной пористости')),
                ('penetrability', models.FloatField(max_length=50, verbose_name='Проницаемость')),
                ('fluid_content', models.CharField(max_length=255, verbose_name='Характер насыщения пласта')),
                ('cluster_age', models.PositiveBigIntegerField(verbose_name='Возраст пласта')),
                ('cluster_toughness', models.FloatField(max_length=50, verbose_name='Упругость пласта')),
                ('oil_saturation_factor', models.FloatField(max_length=50, verbose_name='Коэффициент нефтенасыщенности')),
                ('gas_saturation_factor', models.FloatField(max_length=50, verbose_name='Коэффициент газонасыщенности')),
                ('water_saturation_factor', models.FloatField(max_length=50, verbose_name='Коэффициент водонасыщенности')),
                ('start_layer_pressure', models.FloatField(max_length=50, verbose_name='Начальное пластовое давление')),
                ('residual_water_content', models.FloatField(max_length=50, verbose_name='Содержание остаточной воды')),
                ('bubble_point_pressure', models.FloatField(max_length=50, verbose_name='Давление насыщения')),
            ],
        ),
        migrations.CreateModel(
            name='Smush',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smush_type', models.CharField(max_length=255, verbose_name='Вид бурового раствора')),
                ('density_of_drilling_liquid', models.FloatField(max_length=50, verbose_name='Плотность промывочных жидкостей')),
                ('viscosity', models.FloatField(max_length=50, verbose_name='Вязкость')),
                ('filtration_factor', models.FloatField(max_length=50, verbose_name='Показатель фильтрации')),
                ('gel_strength', models.FloatField(max_length=50, verbose_name='Статическое напряжение сдвига')),
                ('stability', models.FloatField(max_length=50, verbose_name='Стабильность')),
                ('daily_feculence', models.FloatField(max_length=50, verbose_name='Суточный отстой')),
                ('sand_concentration', models.FloatField(max_length=50, verbose_name='Содержание песка')),
                ('hydrogen_index', models.FloatField(max_length=50, verbose_name='Водородный показатель')),
            ],
            options={
                'verbose_name': 'Буровой раствор',
                'verbose_name_plural': 'Буровые растворы',
            },
        ),
        migrations.CreateModel(
            name='WellExtraction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_date', models.DateField(auto_now_add=True, verbose_name='Дата создания записи')),
                ('oil_output_t', models.FloatField(max_length=50, verbose_name='Добыча нефти, т')),
                ('oil_output_m3', models.FloatField(max_length=50, verbose_name='Добыча нефти, м3')),
                ('liquid_output_t', models.FloatField(max_length=50, verbose_name='Добыча жидкости, т')),
                ('liquid_output_m3', models.FloatField(max_length=50, verbose_name='Добыча жидкости, м3')),
                ('gas_output_m3', models.FloatField(max_length=50, verbose_name='Добыча газа, м3')),
                ('injection', models.FloatField(max_length=50, verbose_name='Закачка')),
            ],
            options={
                'verbose_name': 'Добыча скважины',
                'verbose_name_plural': 'Добычи скважин',
            },
        ),
        migrations.CreateModel(
            name='WellState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_date', models.DateField(auto_now_add=True, verbose_name='Дата создания записи')),
                ('status', models.CharField(max_length=255, verbose_name='Текущий статус')),
                ('uptime', models.FloatField(max_length=10, verbose_name='Время работы')),
                ('accumulation_time', models.FloatField(max_length=10, verbose_name='Время накопления')),
                ('downtime', models.FloatField(max_length=10, verbose_name='Время простоя')),
                ('reason', models.CharField(max_length=255, verbose_name='Причина простоя')),
                ('oil_rate', models.FloatField(max_length=50, verbose_name='Дебит нефти')),
                ('liquid_rate', models.FloatField(max_length=50, verbose_name='Дебит жидкости')),
                ('gas_rate', models.FloatField(max_length=50, verbose_name='Дебит газа')),
                ('bottom_hole_pressure', models.FloatField(max_length=50, verbose_name='Забойное давление')),
                ('formational_pressure', models.FloatField(max_length=50, verbose_name='Пластовое давление')),
                ('pump_parameters_measurement_date', models.DateField(verbose_name='Дата измерения параметров насоса')),
                ('esp_frequency', models.FloatField(max_length=50, verbose_name='Частота ЭЦН')),
                ('esp_pressure', models.FloatField(max_length=50, verbose_name='Напор ЭЦН')),
                ('esp_current', models.FloatField(max_length=50, verbose_name='Ток ЭЦН')),
            ],
            options={
                'verbose_name': 'Состояние скважины',
                'verbose_name_plural': 'Состояния скважин',
            },
        ),
        migrations.RemoveField(
            model_name='state',
            name='well',
        ),
        migrations.RemoveField(
            model_name='field',
            name='formation_saturation',
        ),
        migrations.RemoveField(
            model_name='field',
            name='organisation',
        ),
        migrations.RemoveField(
            model_name='field',
            name='reservoir_age',
        ),
        migrations.RemoveField(
            model_name='field',
            name='x_coordinate',
        ),
        migrations.RemoveField(
            model_name='field',
            name='y_coordinate',
        ),
        migrations.RemoveField(
            model_name='organisation',
            name='amount_of_workers',
        ),
        migrations.RemoveField(
            model_name='well',
            name='developing_cost',
        ),
        migrations.RemoveField(
            model_name='well',
            name='drilling_cost',
        ),
        migrations.RemoveField(
            model_name='well',
            name='drilling_mud',
        ),
        migrations.AddField(
            model_name='field',
            name='field_type',
            field=models.CharField(default='-', max_length=255, verbose_name='Тип месторождения'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='well',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='Примечание'),
        ),
        migrations.AddField(
            model_name='well',
            name='completion_date_of_drilling',
            field=models.DateField(default='2022-01-01', verbose_name='Дата окончания бурения'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='well',
            name='license_block',
            field=models.CharField(default='-', max_length=255, verbose_name='Лицензионный участок'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='well',
            name='mining_method',
            field=models.CharField(default='-', max_length=255, verbose_name='Метод добычи'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='well',
            name='nature_of_work',
            field=models.CharField(default='-', max_length=255, verbose_name='Характер работы'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='well',
            name='operator',
            field=models.CharField(default='-', max_length=255, verbose_name='Оператор'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='well',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='wells', to='core.organisation', verbose_name='Владелец'),
        ),
        migrations.AddField(
            model_name='well',
            name='service_date',
            field=models.DateField(default='2022-01-01', verbose_name='Дата ввода скважины'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='well',
            name='start_date_of_drilling',
            field=models.DateField(default='2022-01-01', verbose_name='Дата начала бурения'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='well',
            name='well_type',
            field=models.CharField(default='-', max_length=255, verbose_name='Тип скважины'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='organisation',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.DeleteModel(
            name='Extraction',
        ),
        migrations.DeleteModel(
            name='State',
        ),
        migrations.AddField(
            model_name='wellstate',
            name='well',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='state_notes', to='core.well', verbose_name='Скважина'),
        ),
        migrations.AddField(
            model_name='wellextraction',
            name='well',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='extraction_notes', to='core.well', verbose_name='Скважина'),
        ),
        migrations.AddField(
            model_name='fluidproperties',
            name='layer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='fluid_properties', to='core.layer', verbose_name='Пласт'),
        ),
        migrations.AddField(
            model_name='coresample',
            name='well',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='core_samples', to='core.well', verbose_name='Скважина'),
        ),
        migrations.AddField(
            model_name='cluster',
            name='field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clusters', to='core.field', verbose_name='Месторождение'),
        ),
        migrations.AddField(
            model_name='field',
            name='layers',
            field=models.ManyToManyField(blank=True, related_name='fields', to='core.Layer', verbose_name='Пласты'),
        ),
        migrations.AddField(
            model_name='well',
            name='cluster',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='wells', to='core.cluster', verbose_name='Куст'),
        ),
        migrations.AddField(
            model_name='well',
            name='layer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wells', to='core.layer', verbose_name='Пласт'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='well',
            name='smush',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='wells', to='core.smush', verbose_name='Буровой раствор'),
        ),
    ]
