from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.http import urlencode
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.db.models import F

from .models import Well, Field
from core.utils import get_field_names
from core.services.chart_service import WellExtractionChart


# user and request are passed automatically to the template
# reverse('login') - login page
# reverse('logout') - logout page

class WellListView(ListView):
    model = Well
    template_name = "core/wells.html"


class WellDetailView(DetailView):
    model = Well
    template_name = "core/wells_detail.html"


class WellTableView(View):
    def get(self, request):
        print(request)
        columns = get_field_names(model=Well, exclude_foreign_keys=False, exclude_ids=False)
        well_data = Well.objects.values().annotate(field_name=F('field__name'))
        for obj in well_data:
            obj.pop("field_id")

        return render(request, "core/wells_table.html", {"columns": columns.keys(), "well_data": well_data})

    def post(self, request):
        print(request["data"])
        well_columns = get_field_names(model=Well, exclude_foreign_keys=False, exclude_ids=False)
        list_of_chosen_models = [Field]
        table_columns = list(well_columns.keys())
        required_fields = list(well_columns.values())
        # нужно добавить field__name, а не просто name
        # for model in list_of_chosen_models:
        #     fields = get_field_names(model=model, exclude_foreign_keys=False, exclude_ids=True)
        #     required_fields += list(fields.values())
        #     table_columns += list(fields.keys())
        data = Well.objects.values(*required_fields)
        return render(request, "core/wells_table.html", {"columns": table_columns, "well_data": data})


# Для теста, перенесу в WellTableView с другой логикой
class ExtendedWellTableView(View):
    def get(self, request):
        print(request)
        well_columns = get_field_names(model=Well, exclude_foreign_keys=False, exclude_ids=False)
        field_columns = get_field_names(model=Field, exclude_foreign_keys=False, exclude_ids=True)
        needed_columns = [f"field__{name}" for name in field_columns.values()]
        # print(well_columns)
        # print(field_columns)
        data = Well.objects.values(*well_columns.values(), *needed_columns)  # .annotate(field_name=F('field__name'))
        # print(data)
        return render(request, "core/wells_table.html",
                      {"columns": list(well_columns.keys()) + list(field_columns.keys()), "well_data": data})


class WellExtractionChartView(View):
    def get(self, request):
        return render(request, "core/wells_chart.html")

    def post(self, request):
        well_name = request.POST.get("well_name")
        image_name = WellExtractionChart(well_name=well_name, chart_type="123").build_chart()
        return render(request, "core/wells_chart.html", {"image_name": image_name})


class FieldDetailView(DetailView):
    model = Field
    template_name = "core/fields_detail.html"


class WellCreateView(CreateView):
    model = Well
    fields = '__all__'
    template_name = "core/well_form.html"
    # куда редиректить после создания
    # success_url = "wells/success-url"


class FieldCreateView(CreateView):
    model = Field
    fields = '__all__'
    template_name = "core/field_form.html"


class ImportView(View):
    def post(self, request):
        pass


class OpenView(View):
    def get(self, request):
        return render(request, 'core/main.html')


class ApereoView(View):
    def get(self, request):
        return render(request, 'core/main.html')


class ManualProtect(View):
    def get(self, request):
        if not request.user.is_authenticated:
            loginurl = reverse('login') + '?' + urlencode({'next': request.path})
            return redirect(loginurl)
        return render(request, 'core/main.html')


class ProtectView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'core/main.html')


class DumpPython(View):
    def get(self, req):
        resp = "<pre>\nUser Data in Python:\n\n"
        resp += "Login url: " + reverse('login') + "\n"
        resp += "Logout url: " + reverse('logout') + "\n\n"
        if req.user.is_authenticated:
            resp += "User: " + req.user.username + "\n"
            resp += "Email: " + req.user.email + "\n"
        else:
            resp += "User is not logged in\n"

        resp += "\n"
        resp += "</pre>\n"
        resp += """<a href="/core">Go back</a>"""
        return HttpResponse(resp)
