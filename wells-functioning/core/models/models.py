from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# добавить owner
from django.urls import reverse


class Well(models.Model):
    name = models.CharField("Имя скважины", max_length=255, unique=True)
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
    field = models.ForeignKey('Field', on_delete=models.CASCADE, related_name='wells', verbose_name='Месторождение')
    owner = models.ForeignKey('Organisation', on_delete=models.SET_NULL, related_name='wells', null=True,
                              blank=True, verbose_name='Владелец')
    smush = models.ForeignKey('Smush', on_delete=models.SET_NULL, related_name='wells', null=True,
                              blank=True, verbose_name='Буровой раствор')
    cluster = models.ForeignKey('Cluster', on_delete=models.SET_NULL, related_name='wells', null=True,
                                blank=True, verbose_name='Куст')
    layer = models.ForeignKey('Layer', on_delete=models.CASCADE, related_name='wells', verbose_name='Пласт')

    class Meta:
        verbose_name = 'Скважина'
        verbose_name_plural = 'Скважины'

    def __str__(self):
        return self.name

    # for generic create view
    def get_absolute_url(self):
        return reverse('core:wells-detail', kwargs={"pk": self.pk})

    # @classmethod
    # def get_field_names(cls, exclude_ids=True, exclude_foreign_keys=True):
    #     if not exclude_ids and not exclude_foreign_keys:
    #         fields = tuple(cls._meta.fields)
    #     else:
    #         fields = tuple(
    #             filter(lambda field:
    #                    (exclude_foreign_keys is False or field.get_internal_type() != "ForeignKey") and
    #                    (exclude_ids is False or field.verbose_name != "ID"),
    #                    cls._meta.fields))
    #     result = [field.verbose_name for field in fields]
    #     return result

    # https://stackoverflow.com/questions/10027298/django-detailview-template-show-display-values-of-all-fields
    def get_fields(self):
        for field in self._meta.fields:
            print(field.get_internal_type())
        fields = tuple(
            filter(lambda field: field.get_internal_type() != "ForeignKey" and field.verbose_name != "ID",
                   self._meta.fields))
        result = [(field.verbose_name, field.value_from_object(self)) for field in fields]
        return result


class Field(models.Model):
    name = models.CharField("Название месторождения", max_length=255, unique=True)
    field_type = models.CharField("Тип месторождения", max_length=255)
    layers = models.ManyToManyField('Layer', related_name='fields', blank=True, verbose_name="Пласты")

    class Meta:
        verbose_name = 'Месторождение'
        verbose_name_plural = 'Месторождения'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('core:field-detail', kwargs={"pk": self.pk})

    def get_fields(self):
        fields = tuple(
            filter(lambda field: field.get_internal_type() != models.ForeignKey and field.verbose_name != "ID",
                   self._meta.fields))
        result = [(field.verbose_name, field.value_from_object(self)) for field in fields]
        return result


class Organisation(models.Model):
    name = models.CharField("Название организации", max_length=255, unique=True)
    description = models.TextField('Описание', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'


class WellState(models.Model):
    record_date = models.DateField("Дата создания записи", auto_now_add=True)
    status = models.CharField("Текущий статус", max_length=255)
    uptime = models.FloatField("Время работы", max_length=10)
    accumulation_time = models.FloatField("Время накопления", max_length=10)
    downtime = models.FloatField("Время простоя", max_length=10)
    reason = models.CharField("Причина простоя", max_length=255)
    oil_rate = models.FloatField("Дебит нефти", max_length=50)
    liquid_rate = models.FloatField("Дебит жидкости", max_length=50)
    gas_rate = models.FloatField("Дебит газа", max_length=50)
    bottom_hole_pressure = models.FloatField("Забойное давление", max_length=50)
    formational_pressure = models.FloatField("Пластовое давление", max_length=50)
    pump_parameters_measurement_date = models.DateField("Дата измерения параметров насоса")
    esp_frequency = models.FloatField("Частота ЭЦН", max_length=50)
    esp_pressure = models.FloatField("Напор ЭЦН", max_length=50)
    esp_current = models.FloatField("Ток ЭЦН", max_length=50)
    well = models.ForeignKey('Well', on_delete=models.CASCADE, related_name='state_notes', verbose_name='Скважина')

    def __str__(self):
        return f"Состояние скважины {self.well.name} на момент {self.record_date}"

    class Meta:
        verbose_name = 'Состояние скважины'
        verbose_name_plural = 'Состояния скважин'


class WellExtraction(models.Model):
    year = models.IntegerField("Год")
    record_date = models.DateField("Дата создания записи", auto_now_add=True)
    oil_output_t = models.FloatField("Добыча нефти, т", max_length=50)
    oil_output_m3 = models.FloatField("Добыча нефти, м3", max_length=50)
    liquid_output_t = models.FloatField("Добыча жидкости, т", max_length=50)
    liquid_output_m3 = models.FloatField("Добыча жидкости, м3", max_length=50)
    gas_output_m3 = models.FloatField("Добыча газа, м3", max_length=50)
    water_injection = models.FloatField("Закачка воды", max_length=50)
    gas_injection = models.FloatField("Закачка газа", max_length=50)
    well = models.ForeignKey('Well', on_delete=models.CASCADE, related_name='extraction_notes', verbose_name='Скважина')

    def __str__(self):
        return f"Добыча cкважины {self.well.name} за {self.year} год "

    class Meta:
        verbose_name = 'Добыча скважины'
        verbose_name_plural = 'Добычи скважин'


class CoreSample(models.Model):
    sample_number = models.PositiveIntegerField("Номер образца", unique=True)
    sampling_date = models.DateField("Дата отбора керна")
    sampling_method = models.CharField("Способ отбора керна", max_length=255)
    gas_connected_porosity = models.FloatField("Открытая пористость по газу", max_length=50)
    water_connected_porosity = models.FloatField("Открытая пористость по воде", max_length=50)
    kerosene_connected_porosity = models.FloatField("Открытая пористость по керосину", max_length=50)
    young_modulus = models.FloatField("Модуль Юнга", max_length=50)
    poissons_ratio = models.FloatField("Коэффициент Пуассона", max_length=50)
    well = models.ForeignKey('Well', on_delete=models.CASCADE, related_name='core_samples', verbose_name='Скважина')

    def __str__(self):
        return f"Керн № {self.sample_number}"

    class Meta:
        verbose_name = 'Керны'
        verbose_name_plural = 'Керны'


class Smush(models.Model):
    smush_type = models.CharField("Вид бурового раствора", max_length=255)
    density_of_drilling_liquid = models.FloatField("Плотность промывочных жидкостей", max_length=50)
    viscosity = models.FloatField("Вязкость", max_length=50)
    filtration_factor = models.FloatField("Показатель фильтрации", max_length=50)
    gel_strength = models.FloatField("Статическое напряжение сдвига", max_length=50)
    stability = models.FloatField("Стабильность", max_length=50)
    daily_feculence = models.FloatField("Суточный отстой", max_length=50)
    sand_concentration = models.FloatField("Содержание песка", max_length=50)
    hydrogen_index = models.FloatField("Водородный показатель", max_length=50)

    def __str__(self):
        return f"Буровой раствор {self.pk}"

    class Meta:
        verbose_name = 'Буровой раствор'
        verbose_name_plural = 'Буровые растворы'


class Cluster(models.Model):
    name = models.CharField('Название куста', max_length=255)
    x_coordinate = models.FloatField("Координата Х", max_length=50)
    y_coordinate = models.FloatField("Координата Y", max_length=50)
    field = models.ForeignKey("Field", on_delete=models.CASCADE, related_name='clusters', verbose_name='Месторождение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Куст'
        verbose_name_plural = 'Кусты'


class Layer(models.Model):
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

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пласт'
        verbose_name_plural = 'Пласты'


class FluidProperties(models.Model):
    gas_factor = models.FloatField("Газовый фактор", max_length=50)
    water_dynamic_viscosity = models.FloatField("Динамическая вязкость воды", max_length=50)
    oil_dynamic_viscosity = models.FloatField("Динамическая вязкость нефти", max_length=50)
    gas_dynamic_viscosity = models.FloatField("Динамическая вязкость газа", max_length=50)
    water_density = models.FloatField("Плотность воды", max_length=50)
    oil_density = models.FloatField("Плотность нефти", max_length=50)
    gas_density = models.FloatField("Плотность газа", max_length=50)
    formation_volume_factor_for_water = models.FloatField("Объемный коэффициент воды", max_length=50)
    formation_volume_factor_for_oil = models.FloatField("Объемный коэффициент нефти", max_length=50)
    layer = models.OneToOneField('Layer', on_delete=models.CASCADE, related_name="fluid_properties",
                                 verbose_name='Пласт')

    def __str__(self):
        return f"Свойства флюидов пласта {self.layer.name}"

    class Meta:
        verbose_name = 'Свойства флюидов'
        verbose_name_plural = 'Свойства флюидов'


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
