from datetime import date, timedelta
import random
from typing import Tuple


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
        available_range = (date(2021, 12, 31) - start_date).days
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

    def create_wells(self, field: Field, layer: Layer) -> None:
        wells = []
        for i in range(50):
            params = dict(
                name=f"{random.randint(100, 1200)}P",
                #todo пока вероятность не работает
                purpose=choice(["добывающая", "нагнетательная", "специальная", "вспомогательная"],
                               p=[0.7, 0.1, 0.1, 0.1]),
                well_type=choice(["многозабойная", "горизонтальная", "наклонно-направленная"], p=[0.25, 0.5, 0.25]),
                operator=RussianNames().get_person(),
                license_block="Снежный",
                mining_method=random.choice(["фонтанный", "компрессорный", "насосный"]),
                field=field,
                layer=layer
            )
            params["profile"] = random.choice(["A", "Б", "В", "Г"]) if params["well_type"] == "наклонно-направленная" else "-"
            params["sank_amount"] = random.randint(1, 4) if params["well_type"] == "многозабойная" else 0
            params["start_date_of_drilling"], params["completion_date_of_drilling"], params[
                "service_date"] = self.get_dates_of_drilling()
            params["purpose"], params["nature_of_work"] = self.get_purpose_and_nature_of_work()
            wells.append(Well(**params))

        for well in wells:
            try:
                well.save()
            except IntegrityError:
                print(f"Скважина с именем {well.name} уже существует")

    def create_well_state(self, well: Well) -> WellState:
        pass

    def create_well_extraction(self, well: Well) -> WellExtraction:
        pass

    def handle(self, *args, **options):
        layer = self.create_layer()
        field = self.create_field()
        self.create_wells(field=field, layer=layer)
