import os

import pandas as pd
from django.conf import settings
from django.db.models import Count, Sum, Avg

from core.models import WellExtraction, Layer, Field, Organization
from core.utils import get_field_names


class WellExtractionChart:

    def __init__(self, chart_type: str, well_name: str, layer_id: int, x_axis: str = None, y_axis: list = None):
        self.chart_type = chart_type
        self.well_name = well_name
        self.layer_id = layer_id
        self.x_axis = x_axis
        self.y_axis = y_axis

    def plot_figure(self, x_field, y_fields, objects):
        df = pd.DataFrame(objects.values(*[x_field, *y_fields]))
        figure = df.plot(
            kind="bar",
            x=x_field,
            y=y_fields
        ).legend(self.y_axis).get_figure()
        figure.set_figwidth(8)
        path = os.path.join(settings.MEDIA_ROOT, "chart.png")
        figure.savefig(path)

    def build_chart(self) -> str:
        well_extractions = WellExtraction.objects.filter(
            well__name=self.well_name, #well__layer_id=self.layer_id
        ).order_by("year")
        if not well_extractions:
            return "Скважины с заданными параметрами не найдены"
        field_names = get_field_names(WellExtraction)
        x_field = field_names.get(self.x_axis)
        y_fields = [field_names.get(attr_name) for attr_name in self.y_axis]
        self.plot_figure(x_field=x_field, y_fields=y_fields, objects=well_extractions)
        return "chart.png"


class GroupedWellChart:
    aggregation_methods = {"Суммировать": Sum, "Среднее арифметическое": Avg}
    _expressions = {
        **{model._meta.verbose_name: "wells" for model in [Layer, Field]},
        Organization._meta.verbose_name: "fields__wells"
    }
    _extractions_expression = "extraction_notes"
    _group_by_models = {model._meta.verbose_name: model for model in [Layer, Field, Organization]}

    def __init__(self, field: str, group_by: str, representation: str, aggregation_type: str = None):
        # layer_id: int,
        #self.layer_id = layer_id
        self.field = field
        self.aggregation_type = aggregation_type
        self.group_by = group_by
        self.representation = representation
        self.symbol = "%" if self.representation == "Проценты" else ""

    def round_value(self, value):
        value = round(value, 2)
        if value.is_integer():
            value = int(value)
        return value

    def get_title(self):
        if self.field == "Количество_скважин":
            return "Количество скважин"
        return get_field_names(WellExtraction, invert=True).get(self.field)

    def plot_figure(self, data):
        df = pd.DataFrame({self.field: [item[0] for item in data]}, index=[item[1] for item in data])
        figure = df.plot(
            kind='pie', y=self.field,
            autopct=lambda x:
            f'{round(x, 2) if self.representation == "Проценты" else self.round_value(x / 100 * float(df.sum()))}{self.symbol}',
            ylabel='', title=self.get_title()).legend(
            loc='center left', bbox_to_anchor=(-0.5, 0.8)
        ).get_figure()
        figure.set_figwidth(8.5)
        path = os.path.join(settings.MEDIA_ROOT, "chart.png")
        figure.savefig(path)

    def get_aggregation_condition(self, attr_expression: str):
        aggregation_class = self.aggregation_methods.get(self.aggregation_type, Sum)
        return aggregation_class(attr_expression)

    def build_chart(self) -> str:
        model = self._group_by_models.get(self.group_by)
        # Выражение для получения скважин
        well_expression = self._expressions.get(self.group_by)
        if self.field == "Количество_скважин":
            data = model.objects.annotate(amount_of_wells=Count(well_expression)).values_list("amount_of_wells", "name")
        else:
            new_field_name = f"aggregated_{self.field}"
            data = model.objects.annotate(
                **{new_field_name: self.get_aggregation_condition(
                    f"{well_expression}__{self._extractions_expression}__{self.field}"
                )}
            ).values_list(new_field_name, "name")
        self.plot_figure(data=data)
        return "chart.png"
