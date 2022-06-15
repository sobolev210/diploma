from django.conf import settings
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from core.models import *
from core.views.utils import DefaultCreateMixin
from core.forms import WellForm, WellExtractionForm, WellStateForm, PumpParametersForm, CoreSampleForm, OrganizationForm


class WellListView(ListView):
    model = Well
    template_name = "core/wells/wells.html"
    paginate_by = settings.DEFAULT_PAGE_SIZE
    ordering = ["-id"]


class WellDetailView(DetailView):
    model = Well
    template_name = "core/wells/wells_detail.html"


class WellCreateView(DefaultCreateMixin, CreateView):
    model = Well
    form_class = WellForm
    # redirect after creation
    # success_url = "wells/success-url"


class WellUpdateView(UpdateView):
    model = Well
    form_class = WellForm
    template_name = "core/wells/well_form.html"


class WellDeleteView(DeleteView):
    model = Well
    fields = '__all__'
    template_name = "core/base_delete.html"
    success_url = reverse_lazy('core:wells')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "message_str": "скважину", "return_url": reverse_lazy('core:wells')
        })
        return context


class FieldListView(ListView):
    model = Field
    template_name = "core/fields/fields.html"
    paginate_by = settings.DEFAULT_PAGE_SIZE
    ordering = ["-id"]


class FieldDetailView(DetailView):
    model = Field
    template_name = "core/fields/fields_detail.html"


class FieldCreateView(DefaultCreateMixin, CreateView):
    model = Field
    fields = '__all__'


class FieldUpdateView(UpdateView):
    model = Field
    fields = '__all__'
    template_name = "core/base_form.html"


class FieldDeleteView(DeleteView):
    model = Field
    fields = '__all__'
    template_name = "core/base_delete.html"
    success_url = reverse_lazy('core:fields')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "message_str": "месторождение", "return_url": reverse_lazy('core:fields')
        })
        return context


class OrganizationListView(ListView):
    model = Organization
    template_name = "core/organizations/organizations.html"
    paginate_by = settings.DEFAULT_PAGE_SIZE
    ordering = ["-id"]


class OrganizationDetailView(DetailView):
    model = Organization
    template_name = "core/organizations/organizations_detail.html"


class OrganizationCreateView(DefaultCreateMixin, CreateView):
    model = Organization
    form_class = OrganizationForm


class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = "core/base_form.html"


class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = "core/base_delete.html"
    success_url = reverse_lazy('core:organizations')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "message_str": "организацию", "return_url": reverse_lazy('core:organizations')
        })
        return context


class WellStateListView(ListView):
    model = WellState
    template_name = "core/well_state/well_states.html"
    paginate_by = settings.DEFAULT_PAGE_SIZE
    ordering = ["-id"]


class WellStateDetailView(DetailView):
    model = WellState
    template_name = "core/base_detail.html"


class WellStateCreateView(DefaultCreateMixin, CreateView):
    model = WellState
    fields = '__all__'


class WellStateUpdateView(UpdateView):
    model = WellState
    form_class = WellStateForm
    template_name = "core/base_form.html"


class WellStateDeleteView(DeleteView):
    model = WellState
    template_name = "core/base_delete.html"
    success_url = reverse_lazy('core:well-states')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "message_str": "запись",
            "return_url": reverse_lazy('core:well-states')
        })
        return context


class PumpParametersListView(ListView):
    model = PumpParameters
    template_name = "core/pump_parameters/pump_parameters.html"
    paginate_by = settings.DEFAULT_PAGE_SIZE
    ordering = ["-id"]


class PumpParametersDetailView(DetailView):
    model = PumpParameters
    template_name = "core/base_detail.html"


class PumpParametersCreateView(DefaultCreateMixin, CreateView):
    model = PumpParameters
    form_class = PumpParametersForm


class PumpParametersUpdateView(UpdateView):
    model = PumpParameters
    form_class = PumpParametersForm
    template_name = "core/base_form.html"


class PumpParametersDeleteView(DeleteView):
    model = PumpParameters
    template_name = "core/base_delete.html"
    success_url = reverse_lazy('core:pump-parameters')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "message_str": "", "return_url": reverse_lazy('core:pump-parameters')
        })
        return context


class WellExtractionListView(ListView):
    model = WellExtraction
    template_name = "core/well_extraction/well_extractions.html"
    paginate_by = settings.DEFAULT_PAGE_SIZE
    ordering = ["-id"]


class WellExtractionDetailView(DetailView):
    model = WellExtraction
    template_name = "core/base_detail.html"


class WellExtractionCreateView(DefaultCreateMixin, CreateView):
    model = WellExtraction
    form_class = WellExtractionForm


class WellExtractionUpdateView(UpdateView):
    model = WellExtraction
    form_class = WellExtractionForm
    template_name = "core/base_form.html"


class WellExtractionDeleteView(DeleteView):
    model = WellExtraction
    template_name = "core/base_delete.html"
    success_url = reverse_lazy('core:well-extractions')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "message_str": "запись",
            "return_url": reverse_lazy('core:well-extractions')
        })
        return context


class CoreSampleListView(ListView):
    model = CoreSample
    template_name = "core/core_samples/core_samples.html"
    paginate_by = settings.DEFAULT_PAGE_SIZE
    ordering = ["-id"]


class CoreSampleDetailView(DetailView):
    model = CoreSample
    template_name = "core/base_detail.html"


class CoreSampleCreateView(DefaultCreateMixin, CreateView):
    model = CoreSample
    form_class = CoreSampleForm


class CoreSampleUpdateView(UpdateView):
    model = CoreSample
    form_class = CoreSampleForm
    template_name = "core/base_form.html"


class CoreSampleDeleteView(DeleteView):
    model = CoreSample
    template_name = "core/base_delete.html"
    success_url = reverse_lazy('core:core-samples')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "message_str": "",
            "return_url": reverse_lazy('core:core-samples')
        })
        return context


class SmushListView(ListView):
    model = Smush
    template_name = "core/smushes/smushes.html"
    paginate_by = settings.DEFAULT_PAGE_SIZE
    ordering = ["-id"]


class SmushDetailView(DetailView):
    model = Smush
    template_name = "core/base_detail.html"


class SmushCreateView(DefaultCreateMixin, CreateView):
    model = Smush
    fields = '__all__'


class SmushUpdateView(UpdateView):
    model = Smush
    fields = '__all__'
    template_name = "core/base_form.html"


class SmushDeleteView(DeleteView):
    model = Smush
    template_name = "core/base_delete.html"
    success_url = reverse_lazy('core:smushes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "message_str": "",
            "return_url": reverse_lazy('core:smushes')
        })
        return context


class ClusterListView(ListView):
    model = Cluster
    template_name = "core/clusters/clusters.html"
    paginate_by = settings.DEFAULT_PAGE_SIZE
    ordering = ["-id"]


class ClusterDetailView(DetailView):
    model = Cluster
    template_name = "core/clusters/clusters_detail.html"


class ClusterCreateView(DefaultCreateMixin, CreateView):
    model = Cluster
    fields = '__all__'


class ClusterUpdateView(UpdateView):
    model = Cluster
    fields = '__all__'
    template_name = "core/base_form.html"


class ClusterDeleteView(DeleteView):
    model = Cluster
    template_name = "core/base_delete.html"
    success_url = reverse_lazy('core:clusters')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "message_str": "куст скважин",
            "return_url": reverse_lazy('core:clusters')
        })
        return context


class LayerListView(ListView):
    model = Layer
    template_name = "core/layers/layers.html"
    paginate_by = settings.DEFAULT_PAGE_SIZE
    ordering = ["-id"]


class LayerDetailView(DetailView):
    model = Layer
    template_name = "core/base_detail.html"


class LayerCreateView(DefaultCreateMixin, CreateView):
    model = Layer
    fields = '__all__'


class LayerUpdateView(UpdateView):
    model = Layer
    fields = '__all__'
    template_name = "core/base_form.html"


class LayerDeleteView(DeleteView):
    model = Layer
    template_name = "core/base_delete.html"
    success_url = reverse_lazy('core:layers')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "message_str": "пласт",
            "return_url": reverse_lazy('core:layers')
        })
        return context
