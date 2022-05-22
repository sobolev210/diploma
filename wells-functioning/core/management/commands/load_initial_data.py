import random
from typing import Tuple, List
from datetime import date, timedelta, datetime

from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
from numpy.random import choice
from russian_names import RussianNames

from core.models import Well, WellState, WellExtraction, Field, Layer


class Command(BaseCommand):

    def __init__(self):
        super().__init__()
        self.purpose_values = {"добывающая": "Добыча",
                               "нагнетательная": "Нагнетание",
                               "специальная": ["Пьезометрическая", "Оценочная", "Разведочная", "Наблюдатетельная"],
                               "вспомогательная": ["Водозаборная", "Поглощающая"]}

    def create_field(self) -> Field:
        field = Field.objects.filter(name="Снежное").first()
        if field:
            return field
        return Field.objects.create(
            name="Снежное",
            field_type="нефтегазовое"
        )

    def create_layer(self) -> Layer:
        layer = Layer.objects.filter(name="Ю1").first()
        if layer:
            return layer
        return Layer.objects.create(
            name="Ю1",
            reservoir_type='поровый',
            layer_pressure=17.8,  # МПа
            bed_top_occurrence_depth=670,  # м
            bed_floor_occurrence_depth=1360,  # м
            net_oil_thickness=13.9,  # м
            full_porosity_ratio=0.18,
            penetrability=43.6,
            fluid_content="нефтенасыщенный",
            cluster_age=120000,
            cluster_toughness=1.6,
            oil_saturation_factor=0.35,
            gas_saturation_factor=0.24,
            water_saturation_factor=0.14,
            start_layer_pressure=20,
            residual_water_content=0.07,
            bubble_point_pressure=18.4,
        )

    def get_dates_of_drilling(self) -> Tuple[date, date, date]:
        start_date = date(2000, 1, 1)
        available_range = (date(datetime.now().year - 1, 12, 31) - start_date).days
        start_offset = random.randint(0, available_range - 1800)
        start_date_of_drilling = start_date + timedelta(days=start_offset)
        completion_offset = random.randint(90, 1700)
        completion_date_of_drilling = start_date_of_drilling + timedelta(days=completion_offset)
        service_offset = random.randint(0, 90)
        service_date = completion_date_of_drilling + timedelta(days=service_offset)
        return start_date_of_drilling, completion_date_of_drilling, service_date

    def get_purpose_and_nature_of_work(self) -> Tuple[str, str]:
        purpose = random.choice(list(self.purpose_values.keys()))
        nature_of_work_values = self.purpose_values[purpose]
        if type(nature_of_work_values) is list:
            nature_of_work = random.choice(nature_of_work_values)
        else:
            nature_of_work: str = nature_of_work_values
        return purpose, nature_of_work

    def create_wells(self, field: Field, layer: Layer, letter: str) -> List[Well]:
        wells = []
        for i in range(random.randint(10, 60)):
            params = dict(
                name=f"{random.randint(10, 2000)}{letter}",
                # todo пока вероятность не работает
                purpose=choice(["добывающая", "нагнетательная", "специальная", "вспомогательная"],
                               p=[0.7, 0.1, 0.1, 0.1]),
                well_type=choice(["многозабойная", "горизонтальная", "наклонно-направленная"], p=[0.25, 0.5, 0.25]),
                operator=RussianNames().get_person(),
                license_block="Снежный",
                mining_method=random.choice(["фонтанный", "компрессорный", "насосный"]),
                field=field,
                x_coordinate=field.x_coordinate + random.uniform(-0.07, 0.07),
                y_coordinate=field.y_coordinate + random.uniform(-0.07, 0.07)
            )
            params["profile"] = random.choice(["A", "Б", "В", "Г"]) if params["well_type"] == "наклонно-направленная" else "-"
            params["sank_amount"] = random.randint(1, 4) if params["well_type"] == "многозабойная" else 0
            params["start_date_of_drilling"], params["completion_date_of_drilling"], params[
                "service_date"] = self.get_dates_of_drilling()
            params["purpose"], params["nature_of_work"] = self.get_purpose_and_nature_of_work()
            well = Well(**params)
            try:
                well.save()
                well.layers.set([layer])
                well.save()
                wells.append(well)
            except IntegrityError:
                print(f"Скважина с именем {well.name} уже существует")
        return wells

    def create_well_state_data(self, well: Well) -> WellState:
        pass

    def create_well_extraction_data(self, well: Well) -> None:
        oil_output_t = 0
        gas_output_m3 = 0
        liquid_output_m3 = 0

        for year in range(well.service_date.year, datetime.now().year):
            oil_output_t_inc = random.uniform(0, 5000)
            liquid_output_m3_inc = random.uniform(0, 7000)
            gas_output_m3_inc = random.uniform(0, 600)
            oil_output_t += oil_output_t_inc
            liquid_output_m3 += liquid_output_m3_inc
            gas_output_m3 += gas_output_m3_inc

            WellExtraction.objects.create(
                year=year,
                oil_output_t=oil_output_t,
                oil_output_m3=oil_output_t / 865 * 1000,
                liquid_output_t=liquid_output_m3 / 1000 * 997,
                liquid_output_m3=liquid_output_m3,
                gas_output_m3=gas_output_m3,
                water_injection=random.uniform(0, 250),
                gas_injection=random.uniform(30000, 200000),
                well=well,
                oil_rate=oil_output_t_inc / 365,
                liquid_rate=liquid_output_m3_inc / 365,
                gas_rate=gas_output_m3_inc / 365,
                bottom_hole_pressure=well.layers.first().layer_pressure - random.uniform(1, 3.5)
            )

    def handle(self, *args, **options):
        fields = Field.objects.all()
        for field in fields:
            for layer in field.layers.all():
                letter = random.choice(["P", "I", "J", "N", "U"])
                wells = self.create_wells(field=field, layer=layer, letter=letter)
                for well in wells:
                    self.create_well_extraction_data(well)
