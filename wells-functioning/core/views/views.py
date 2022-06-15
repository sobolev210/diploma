import pandas as pd
from django.core.paginator import Paginator
from django.db.models import F
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django_admin_geomap import geomap_context

from core.models import Well, Field, Layer, WellExtraction
from core.services.chart_service import WellExtractionChart, GroupedWellChart
from core.utils import get_field_names


# user and request are passed automatically to the template
# reverse('login') - login page
# reverse('logout') - logout page

class WellTableView(View):
    def get(self, request):
        columns = get_field_names(model=Well, exclude_foreign_keys=False, exclude_ids=False)
        well_data = Well.objects.order_by("-id").values().annotate(field_name=F('field__name'))
        for obj in well_data:
            obj.pop("field_id")
        paginator = Paginator(well_data, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        for obj in page_obj.object_list:
            for key, value in obj.items():
                if isinstance(value, float):
                    obj[key] = round(value, 2)
                elif value is None:
                    obj[key] = "-"
        return render(
            request, "core/tables.html", {"columns": columns.keys(), "well_data": well_data, 'page_obj': page_obj}
        )

    def post(self, request):
        columns = get_field_names(model=Well, exclude_foreign_keys=False, exclude_ids=False, invert=True)
        well_data = Well.objects.order_by("-id").values().annotate(field_name=F('field__name'))
        for obj in well_data:
            obj.pop("field_id")
        df = pd.DataFrame(list(well_data), )
        df.rename(columns=columns, inplace=True)
        response = HttpResponse(headers={
            'Content-Type': 'application/vnd.ms-excel',
            'Content-Disposition': 'attachment; filename="result.xlsx"',
        })
        df.to_excel(response, index=False, sheet_name="Данные по скважинам")
        return response

    # def post(self, request):
    #     print(request["data"])
    #     well_columns = get_field_names(model=Well, exclude_foreign_keys=False, exclude_ids=False)
    #     list_of_chosen_models = [Field]
    #     table_columns = list(well_columns.keys())
    #     required_fields = list(well_columns.values())
    #     for model in list_of_chosen_models:
    #         fields = get_field_names(model=model, exclude_foreign_keys=False, exclude_ids=True)
    #         required_fields += list(fields.values())
    #         table_columns += list(fields.keys())
    #     data = Well.objects.values(*required_fields)
    #     #return render(request, "core/Главная.html")
    #     return render(request, "core/wells_table.html", {"columns": table_columns, "well_data": data})


class ExtendedWellTableView(View):
    def get(self, request):
        well_columns = get_field_names(model=Well, exclude_foreign_keys=False, exclude_ids=False)
        field_columns = get_field_names(model=Field, exclude_foreign_keys=False, exclude_ids=True)
        needed_columns = [f"field__{name}" for name in field_columns.values()]
        data = Well.objects.values(*well_columns.values(), *needed_columns)  # .annotate(field_name=F('field__name'))
        return render(request, "core/wells_table.html",
                      {"columns": list(well_columns.keys()) + list(field_columns.keys()), "well_data": data})


class WellExtractionChartView(View):
    _layers = Layer.objects.all()

    params = {
        "По дебитам": {
            "газ": "Дебит газа, тыс м3/сут", "жидкость": "Дебит жидкости, м3/сут", "нефть": "Дебит нефти, т/cут"
        },
        "По накопленной добыче": {
            "газ": "Добыча газа, тыс м3", "жидкость": "Добыча жидкости, м3", "нефть": "Добыча нефти, м3"
        }
    }
    options = ["нефть", "жидкость", "газ"]

    def get(self, request):
        return render(request, "core/single_object_chart.html", {"layers": self._layers})

    def post(self, request):
        well_name = request.POST.get("well_name")
        if not well_name:
            return render(request, "core/single_object_chart.html", {
                "message": "Ошибка: не указано имя скважины.",
                "layers": self._layers,
            })
        layer_id = request.POST.get("layers")
        chart_data = request.POST.get("parameters")
        x_axis = "Год"
        y_axis = []
        for option, attr_name in self.params[chart_data].items():
            if request.POST.get(option):
                y_axis.append(attr_name)
        if not y_axis:
            return render(request, "core/single_object_chart.html", {
                "message": "Ошибка: для построения графика должен быть выбран хотя бы один вид показателя.", "layers": self._layers,
            })
            # exception - для построения графика должен быть выбран хотя бы один параметр
        message = WellExtractionChart(
            well_name=well_name,
            chart_type="bar",
            x_axis=x_axis,
            y_axis=y_axis,
            layer_id=layer_id
        ).build_chart()
        if message:
            return render(request, "core/single_object_chart.html", {
                "message": message,
                "layers": self._layers,
            })
        return render(request, "core/single_object_chart.html", {
            "image_name": "chart.png", "layers": self._layers, "well_name": well_name, "chart_data": chart_data
        })


class GroupedWellExtractionChartView(View):
    _fields = {**{"Количество скважин": "Количество_скважин"},
               **get_field_names(WellExtraction, exclude_fields=["year", "record_date", ])}

    def get(self, request):
        return render(request, "core/Графики-по-всей-компании.html", {"fields": self._fields})

    def post(self, request):
        field = request.POST.get("fields")
        group_by = request.POST.get("group_by")
        aggregation_type = request.POST.get("aggregation_type")
        representation = request.POST.get("representation", "Проценты")
        GroupedWellChart(
            field=field,
            aggregation_type=aggregation_type,
            group_by=group_by,
            representation=representation
        ).build_chart()

        return render(request, "core/Графики-по-всей-компании.html", {
            "image_name": "chart.png", "fields": self._fields, "group_by": group_by, "aggregation_type": aggregation_type,
            "field": field, "representation": representation
        })


#https://github.com/vb64/django.admin.geomap
def map_view(request):
    return render(request, 'core/map.html', geomap_context(Well.objects.all(), map_height="1300px"))
