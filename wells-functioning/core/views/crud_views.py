from django import forms
from django.conf import settings
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from core.models import *
from core.forms import WellForm, WellExtractionForm, WellStateForm, PumpParametersForm, CoreSampleForm


class WellListView(ListView):
    model = Well
    template_name = "core/wells/wells.html"
    paginate_by = settings.DEFAULT_PAGE_SIZE


class WellDetailView(DetailView):
    model = Well
    template_name = "core/wells/wells_detail.html"

#todo вместо object_create.html и object_update.html использовать object_form.html, добавить fields в UpdateView и DeleteView
#todo для удаления добавить template object_delete.html
#todo поменять UpdateView на DeleteView для эндпоинтов с удалением
class WellCreateView(CreateView):
    model = Well
    form_class = WellForm
    #template_name = "core/wells/Создание-объекта.html"
    template_name = "core/wells/well_form.html"
    #fields = '__all__'

    # куда редиректить после создания
    # success_url = "wells/success-url"


class WellUpdateView(UpdateView):
    model = Well
    form_class = WellForm
    template_name = "core/wells/well_form.html"


class WellDeleteView(DeleteView):
    model = Well
    fields = '__all__'
    template_name = "core/wells/well_delete.html"
    success_url = reverse_lazy('core:wells')


class FieldListView(ListView):
    model = Field
    template_name = "core/fields/fields.html"
    paginate_by = settings.DEFAULT_PAGE_SIZE


class FieldDetailView(DetailView):
    model = Field
    template_name = "core/fields/fields_detail.html"


class FieldCreateView(CreateView):
    model = Field
    fields = '__all__'
    template_name = "core/fields/field_form.html"


class FieldUpdateView(UpdateView):
    model = Field
    fields = '__all__'
    template_name = "core/fields/field_form.html"


class FieldDeleteView(DeleteView):
    model = Field
    fields = '__all__'
    template_name = "core/fields/field_delete.html"


# добавить шаблон
class OrganizationListView(ListView):
    model = Organization
    template_name = "core/organizations/organizations.html"
    paginate_by = settings.DEFAULT_PAGE_SIZE


class OrganizationDetailView(DetailView):
    model = Organization
    template_name = "core/organizations/organizations_detail.html"


class OrganizationCreateView(CreateView):
    model = Organization
    fields = '__all__'
    template_name = "core/organizations/organization_create.html"


class OrganizationUpdateView(UpdateView):
    model = Organization
    template_name = "core/organizations/organization_update.html"


class OrganizationDeleteView(UpdateView):
    model = Organization
    template_name = "core/organizations/organization_delete.html"


class WellStateListView(ListView):
    model = WellState
    template_name = "core/well_state/well_states.html"
    paginate_by = settings.DEFAULT_PAGE_SIZE


class WellStateDetailView(DetailView):
    model = WellState
    template_name = "core/well_state/well_states_detail.html"


class WellStateCreateView(CreateView):
    model = WellState
    form_class = WellStateForm
    template_name = "core/well_state/well_state_create.html"


class WellStateUpdateView(UpdateView):
    model = WellState
    form_class = WellStateForm
    template_name = "core/well_state/well_state_update.html"


class WellStateDeleteView(UpdateView):
    model = WellState
    template_name = "core/well_state/well_state_delete.html"


class PumpParametersListView(ListView):
    model = PumpParameters
    template_name = "core/pump_parameters/pump_parameters.html"
    paginate_by = settings.DEFAULT_PAGE_SIZE


class PumpParametersDetailView(DetailView):
    model = PumpParameters
    template_name = "core/pump_parameters/pump_parameters_detail.html"


class PumpParametersCreateView(CreateView):
    model = PumpParameters
    form_class = PumpParametersForm
    template_name = "core/pump_parameters/pump_parameters_create.html"


class PumpParametersUpdateView(UpdateView):
    model = PumpParameters
    form_class = PumpParametersForm
    template_name = "core/pump_parameters/pump_parameters_update.html"


class PumpParametersDeleteView(UpdateView):
    model = PumpParameters
    template_name = "core/pump_parameters/pump_parameters_delete.html"


class WellExtractionListView(ListView):
    model = WellExtraction
    template_name = "core/well_extraction/well_extractions.html"
    paginate_by = settings.DEFAULT_PAGE_SIZE


class WellExtractionDetailView(DetailView):
    model = WellExtraction
    template_name = "core/well_extraction/well_extractions_detail.html"


class WellExtractionCreateView(CreateView):
    model = WellExtraction
    form_class = WellExtractionForm
    template_name = "core/well_extraction/well_extraction_create.html"


class WellExtractionUpdateView(UpdateView):
    model = WellExtraction
    form_class = WellExtractionForm
    template_name = "core/well_extraction/well_extraction_update.html"


class WellExtractionDeleteView(UpdateView):
    model = WellExtraction
    template_name = "core/well_extraction/well_extraction_delete.html"


class CoreSampleListView(ListView):
    model = CoreSample
    template_name = "core/core_samples/core_samples.html"
    paginate_by = settings.DEFAULT_PAGE_SIZE


class CoreSampleDetailView(DetailView):
    model = CoreSample
    template_name = "core/core_samples/core_samples_detail.html"


class CoreSampleCreateView(CreateView):
    model = CoreSample
    form_class = CoreSampleForm
    template_name = "core/core_samples/core_sample_create.html"


class CoreSampleUpdateView(UpdateView):
    model = CoreSample
    form_class = CoreSampleForm
    template_name = "core/core_samples/core_sample_update.html"


class CoreSampleDeleteView(UpdateView):
    model = CoreSample
    template_name = "core/core_samples/core_sample_delete.html"


class SmushListView(ListView):
    model = Smush
    template_name = "core/smushes/smushes.html"
    paginate_by = settings.DEFAULT_PAGE_SIZE


class SmushDetailView(DetailView):
    model = Smush
    template_name = "core/smushes/smushes_detail.html"


class SmushCreateView(CreateView):
    model = Smush
    fields = '__all__'
    template_name = "core/smushes/smush_create.html"


class SmushUpdateView(UpdateView):
    model = Smush
    template_name = "core/smushes/smush_update.html"


class SmushDeleteView(UpdateView):
    model = Smush
    template_name = "core/smushes/smush_delete.html"


class ClusterListView(ListView):
    model = Cluster
    template_name = "core/clusters/clusters.html"
    paginate_by = settings.DEFAULT_PAGE_SIZE


class ClusterDetailView(DetailView):
    model = Cluster
    template_name = "core/clusters/clusters_detail.html"


class ClusterCreateView(CreateView):
    model = Cluster
    fields = '__all__'
    template_name = "core/clusters/cluster_create.html"


class ClusterUpdateView(UpdateView):
    model = Cluster
    template_name = "core/clusters/cluster_update.html"


class ClusterDeleteView(UpdateView):
    model = Cluster
    template_name = "core/clusters/cluster_delete.html"


class LayerListView(ListView):
    model = Layer
    template_name = "core/layers/layers.html"
    paginate_by = settings.DEFAULT_PAGE_SIZE


class LayerDetailView(DetailView):
    model = Layer
    template_name = "core/layers/layers_detail.html"


class LayerCreateView(CreateView):
    model = Layer
    fields = '__all__'
    template_name = "core/layers/layer_create.html"


class LayerUpdateView(UpdateView):
    model = Layer
    template_name = "core/layers/layer_update.html"


class LayerDeleteView(UpdateView):
    model = Layer
    template_name = "core/layers/layer_delete.html"


class FluidPropertiesListView(ListView):
    model = FluidProperties
    template_name = "core/fluid_properties/fluid_properties.html"
    paginate_by = settings.DEFAULT_PAGE_SIZE


class FluidPropertiesDetailView(DetailView):
    model = FluidProperties
    template_name = "core/fluid_properties/fluid_properties_detail.html"


class FluidPropertiesCreateView(CreateView):
    model = FluidProperties
    fields = '__all__'
    template_name = "core/fluid_properties/fluid_properties_create.html"


class FluidPropertiesUpdateView(UpdateView):
    model = FluidProperties
    template_name = "core/fluid_properties/fluid_properties_update.html"


class FluidPropertiesDeleteView(UpdateView):
    model = FluidProperties
    template_name = "core/fluid_properties/fluid_properties_delete.html"




