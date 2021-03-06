from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django_admin_geomap import GeoItem
# добавить owner
from django.urls import reverse


from core.models.utils import GetFieldsMixin, GetVerboseNameMixin


class Well(models.Model, GeoItem, GetFieldsMixin, GetVerboseNameMixin):

    @property
    def geomap_latitude(self):
        return '' if self.x_coordinate is None else str(self.x_coordinate)

    @property
    def geomap_longitude(self):
        return '' if self.y_coordinate is None else str(self.y_coordinate)

    name = models.CharField("Имя скважины", max_length=255)
    purpose = models.CharField("Назначение скважины", max_length=255)
    well_type = models.CharField("Тип скважины", max_length=255)
    profile = models.CharField("Профиль", max_length=255)
    sank_amount = models.IntegerField("Количество стволов")
    start_date_of_drilling = models.DateField("Дата начала бурения")
    completion_date_of_drilling = models.DateField("Дата окончания бурения")
    nature_of_work = models.CharField("Характер работы", max_length=255)
    operator = models.CharField("Оператор", max_length=255)
    license_block = models.CharField("Лицензионный участок", max_length=255)
    service_date = models.DateField("Дата ввода скважины")
    mining_method = models.CharField("Метод добычи", max_length=255)
    comment = models.TextField("Примечание", blank=True, null=True)
    x_coordinate = models.FloatField("Координата Х", max_length=50)
    y_coordinate = models.FloatField("Координата Y", max_length=50)
    smush = models.ForeignKey('Smush', on_delete=models.SET_NULL, related_name='wells', null=True,
                              blank=True, verbose_name='Буровой раствор')
    cluster = models.ForeignKey('Cluster', on_delete=models.SET_NULL, related_name='wells', null=True,
                                blank=True, verbose_name='Куст')
    layers = models.ManyToManyField('Layer', related_name='wells', blank=True, verbose_name="Пласты")
    field = models.ForeignKey('Field', on_delete=models.CASCADE, related_name='wells', verbose_name='Месторождение')

    # https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/#model-style
    class Meta:
        verbose_name = 'Скважина'
        verbose_name_plural = 'Скважины'
        #unique_together = ('name', 'layers',)

    def __str__(self):
        return self.name

    # used by generic create view
    def get_absolute_url(self):
        return reverse('core:wells-detail', kwargs={"pk": self.pk})

    @classmethod
    def genitive_case(cls):
        return "скважины"

    def get_update_url(self):
        return reverse('core:well-update', kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse('core:well-delete', kwargs={"pk": self.pk})


class Field(models.Model, GetFieldsMixin, GetVerboseNameMixin):
    name = models.CharField("Название месторождения", max_length=255, unique=True)
    field_type = models.CharField("Тип месторождения", max_length=255)
    x_coordinate = models.FloatField("Координата Х", max_length=50)
    y_coordinate = models.FloatField("Координата Y", max_length=50)
    layers = models.ManyToManyField('Layer', related_name='fields', blank=True, verbose_name="Пласты")
    owner = models.ForeignKey('Organization', on_delete=models.SET_NULL, related_name='fields', null=True,
                              blank=True, verbose_name='Владелец')

    class Meta:
        verbose_name = 'Месторождение'
        verbose_name_plural = 'Месторождения'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('core:fields-detail', kwargs={"pk": self.pk})

    @classmethod
    def genitive_case(cls):
        return "месторождения"

    def get_update_url(self):
        return reverse('core:field-update', kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse('core:field-delete', kwargs={"pk": self.pk})


class Organization(models.Model, GetFieldsMixin, GetVerboseNameMixin):
    name = models.CharField("Название организации", max_length=255, unique=True)
    description = models.TextField('Описание', null=True, blank=True)
    abbreviation = models.CharField("Аббревиатура", max_length=20, null=True, blank=True)

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('core:organizations-detail', kwargs={"pk": self.pk})

    @classmethod
    def genitive_case(cls):
        return "организации"

    def get_update_url(self):
        return reverse('core:organization-update', kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse('core:organization-delete', kwargs={"pk": self.pk})


class WellState(models.Model, GetFieldsMixin, GetVerboseNameMixin):
    record_date = models.DateField("Дата создания записи", auto_now_add=True)
    status = models.CharField("Текущий статус", max_length=255)
    uptime = models.FloatField("Время работы", max_length=10)
    accumulation_time = models.FloatField("Время накопления", max_length=10)
    downtime = models.FloatField("Время простоя", max_length=10)
    reason = models.CharField("Причина простоя", max_length=255)
    well = models.ForeignKey('Well', on_delete=models.CASCADE,
                             related_name='state_notes', verbose_name='Скважина')

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Состояния скважин'

    def __str__(self):
        return f"Состояние скважины {self.well.name} на момент {self.record_date}"

    def get_absolute_url(self):
        return reverse('core:well-states-detail', kwargs={"pk": self.pk})

    @classmethod
    def genitive_case(cls):
        return "записи о состоянии скважины"

    def get_update_url(self):
        return reverse('core:well-state-update', kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse('core:well-state-delete', kwargs={"pk": self.pk})


class PumpParameters(models.Model, GetFieldsMixin, GetVerboseNameMixin):
    pump_parameters_measurement_date = models.DateField("Дата измерения параметров насоса")
    pump_type = models.CharField("Вид насоса", max_length=255)
    pump_state = models.CharField("Состояние насоса", max_length=255)
    esp_frequency = models.FloatField("Частота ЭЦН", max_length=50)
    esp_pressure = models.FloatField("Напор ЭЦН", max_length=50)
    esp_current = models.FloatField("Ток ЭЦН", max_length=50)
    well = models.OneToOneField('Well', on_delete=models.CASCADE, related_name='pump_parameters', verbose_name='Скважина')

    class Meta:
        verbose_name = 'Насос'
        verbose_name_plural = 'Насосы'

    def __str__(self):
        return f"Насос скважины {self.well.name}"

    def get_absolute_url(self):
        return reverse('core:pump-parameters-detail', kwargs={"pk": self.pk})

    @classmethod
    def genitive_case(cls):
        return "насоса"

    def get_update_url(self):
        return reverse('core:pump-parameters-update', kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse('core:pump-parameters-delete', kwargs={"pk": self.pk})


class WellExtraction(models.Model, GetFieldsMixin, GetVerboseNameMixin):
    year = models.IntegerField("Год")
    record_date = models.DateField("Дата создания записи", auto_now_add=True)
    oil_output_t = models.FloatField("Добыча нефти, т", max_length=50)
    oil_output_m3 = models.FloatField("Добыча нефти, м3", max_length=50)
    liquid_output_t = models.FloatField("Добыча жидкости, т", max_length=50)
    liquid_output_m3 = models.FloatField("Добыча жидкости, м3", max_length=50)
    gas_output_m3 = models.FloatField("Добыча газа, тыс м3", max_length=50)
    water_injection = models.FloatField("Закачка воды", max_length=50)
    gas_injection = models.FloatField("Закачка газа", max_length=50)
    oil_rate = models.FloatField("Дебит нефти, т/cут", max_length=50)
    liquid_rate = models.FloatField("Дебит жидкости, м3/сут", max_length=50)
    gas_rate = models.FloatField("Дебит газа, тыс м3/сут", max_length=50)
    bottom_hole_pressure = models.FloatField("Забойное давление", max_length=50)
    well = models.ForeignKey('Well', on_delete=models.CASCADE, related_name='extraction_notes', verbose_name='Скважина')

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Добычи скважин'

    def __str__(self):
        return f"Добыча cкважины {self.well.name} за {self.year} год "

    def get_absolute_url(self):
        return reverse('core:well-extractions-detail', kwargs={"pk": self.pk})

    @classmethod
    def genitive_case(cls):
        return "записи о добыче скважины"

    def get_update_url(self):
        return reverse('core:well-extractions-update', kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse('core:well-extractions-delete', kwargs={"pk": self.pk})


class CoreSample(models.Model, GetFieldsMixin, GetVerboseNameMixin):
    sample_number = models.PositiveIntegerField("Номер образца", unique=True)
    sampling_date = models.DateField("Дата отбора керна")
    sampling_method = models.CharField("Способ отбора керна", max_length=255)
    gas_connected_porosity = models.FloatField("Открытая пористость по газу", max_length=50)
    water_connected_porosity = models.FloatField("Открытая пористость по воде", max_length=50)
    kerosene_connected_porosity = models.FloatField("Открытая пористость по керосину", max_length=50)
    young_modulus = models.FloatField("Модуль Юнга", max_length=50)
    poissons_ratio = models.FloatField("Коэффициент Пуассона", max_length=50)
    # Скважина выводится из эксплуатации, а образцы пород остаются
    well = models.ForeignKey('Well', on_delete=models.SET_NULL, null=True, related_name='core_samples',
                             verbose_name='Скважина')

    class Meta:
        verbose_name = 'Керны'
        verbose_name_plural = 'Керны'

    def __str__(self):
        return f"Керн № {self.sample_number}"

    def get_absolute_url(self):
        return reverse('core:core-samples-detail', kwargs={"pk": self.pk})

    @classmethod
    def genitive_case(cls):
        return "керна"

    def get_update_url(self):
        return reverse('core:core-sample-update', kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse('core:core-sample-delete', kwargs={"pk": self.pk})


class Smush(models.Model, GetFieldsMixin, GetVerboseNameMixin):
    smush_type = models.CharField("Вид бурового раствора", max_length=255)
    density_of_drilling_liquid = models.FloatField("Плотность промывочных жидкостей", max_length=50)
    viscosity = models.FloatField("Вязкость", max_length=50)
    filtration_factor = models.FloatField("Показатель фильтрации", max_length=50)
    gel_strength = models.FloatField("Статическое напряжение сдвига", max_length=50)
    stability = models.FloatField("Стабильность", max_length=50)
    daily_feculence = models.FloatField("Суточный отстой", max_length=50)
    sand_concentration = models.FloatField("Содержание песка", max_length=50)
    hydrogen_index = models.FloatField("Водородный показатель", max_length=50)

    class Meta:
        verbose_name = 'Буровой раствор'
        verbose_name_plural = 'Буровые растворы'

    def __str__(self):
        return f"Буровой раствор {self.pk}"

    def get_absolute_url(self):
        return reverse('core:smushes-detail', kwargs={"pk": self.pk})

    @classmethod
    def genitive_case(cls):
        return "бурового раствора"

    def get_update_url(self):
        return reverse('core:smush-update', kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse('core:smush-delete', kwargs={"pk": self.pk})


class Cluster(models.Model, GetFieldsMixin, GetVerboseNameMixin):
    name = models.CharField('Название куста', max_length=255)
    field = models.ForeignKey("Field", on_delete=models.CASCADE, related_name='clusters', verbose_name='Месторождение')
    max_deflection_of_borehole = models.FloatField("Максимальное отклонение забоя", max_length=50)

    class Meta:
        verbose_name = 'Куст'
        verbose_name_plural = 'Кусты'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('core:clusters-detail', kwargs={"pk": self.pk})

    @classmethod
    def genitive_case(cls):
        return "куста скважин"

    def get_update_url(self):
        return reverse('core:cluster-update', kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse('core:cluster-delete', kwargs={"pk": self.pk})


class Layer(models.Model, GetFieldsMixin, GetVerboseNameMixin):
    name = models.CharField('Название пласта', max_length=255)
    reservoir_type = models.CharField('Тип коллектора', max_length=255)
    layer_pressure = models.FloatField("Пластовое давление", max_length=50)
    bed_top_occurrence_depth = models.FloatField("Глубина залегания кровли", max_length=50)
    bed_floor_occurrence_depth = models.FloatField("Глубина залегания подошвы", max_length=50)
    net_oil_thickness = models.FloatField("Эффективная нефтенасыщенная толщина", max_length=50)
    full_porosity_ratio = models.FloatField("Коэффициент полной пористости", max_length=50)
    penetrability = models.FloatField("Проницаемость", max_length=50)
    fluid_content = models.CharField('Характер насыщения пласта', max_length=255)
    cluster_age = models.PositiveBigIntegerField('Возраст пласта')
    cluster_toughness = models.FloatField("Упругость пласта", max_length=50)
    oil_saturation_factor = models.FloatField("Коэффициент нефтенасыщенности", max_length=50)
    gas_saturation_factor = models.FloatField("Коэффициент газонасыщенности", max_length=50)
    water_saturation_factor = models.FloatField("Коэффициент водонасыщенности", max_length=50)
    start_layer_pressure = models.FloatField("Начальное пластовое давление", max_length=50)
    residual_water_content = models.FloatField("Содержание остаточной воды", max_length=50)
    bubble_point_pressure = models.FloatField("Давление насыщения", max_length=50)
    gas_factor = models.FloatField("Газовый фактор", max_length=50, null=True)
    water_dynamic_viscosity = models.FloatField("Динамическая вязкость воды", max_length=50, null=True)
    oil_dynamic_viscosity = models.FloatField("Динамическая вязкость нефти", max_length=50, null=True)
    gas_dynamic_viscosity = models.FloatField("Динамическая вязкость газа", max_length=50, null=True)
    water_density = models.FloatField("Плотность воды", max_length=50, null=True)
    oil_density = models.FloatField("Плотность нефти", max_length=50, null=True)
    gas_density = models.FloatField("Плотность газа", max_length=50, null=True)
    formation_volume_factor_for_water = models.FloatField("Объемный коэффициент воды", max_length=50, null=True)
    formation_volume_factor_for_oil = models.FloatField("Объемный коэффициент нефти", max_length=50, null=True)

    class Meta:
        verbose_name = 'Пласт'
        verbose_name_plural = 'Пласты'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('core:layers-detail', kwargs={"pk": self.pk})

    @classmethod
    def genitive_case(cls):
        return "пласта"

    def get_update_url(self):
        return reverse('core:layer-update', kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse('core:layer-delete', kwargs={"pk": self.pk})


class ImportSchema(models.Model):
    name = models.CharField("Название схемы", max_length=255)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = 'Схема импорта'
        verbose_name_plural = 'Схемы импорта'


class ImportSchemaAttribute(models.Model):
    column_position = models.PositiveIntegerField("Номер столбца")
    type_name = models.CharField("Название cвязываемой модели", max_length=255)
    attr_name = models.CharField("Атрибут", max_length=255)
    import_schema = models.ForeignKey('ImportSchema', on_delete=models.CASCADE, related_name='attributes',
                                      verbose_name='Схема импорта')

    class Meta:
        verbose_name = 'Атрибут схемы импорта'
        verbose_name_plural = 'Атрибуты схемы импорта'
