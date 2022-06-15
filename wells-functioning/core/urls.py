from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'core'

urlpatterns = [
    path('', login_required(TemplateView.as_view(template_name='core/main.html')), name="main"),
    path('chart-choice', TemplateView.as_view(template_name='core/chart_choice.html'), name="chart-choice"),
    path('wells/charts/grouped', views.GroupedWellExtractionChartView.as_view(), name='grouped-chart'),
    path('objects', TemplateView.as_view(template_name='core/objects.html'), name="objects"),
    path('wells/table', views.WellTableView.as_view(), name='table'),
    path('wells/charts/extraction', views.WellExtractionChartView.as_view(), name='wells-extraction-chart'),
    path('map', views.map_view, name="map")
]

urlpatterns += [
    path('wells', views.WellListView.as_view(), name='wells'),
    path('wells/<int:pk>', views.WellDetailView.as_view(), name='wells-detail'),
    path('wells/create', views.WellCreateView.as_view(), name='wells-create'),
    path('wells/<int:pk>/update', views.WellUpdateView.as_view(), name='well-update'),
    path('wells/<int:pk>/delete', views.WellDeleteView.as_view(), name='well-delete'),

    path('fields', views.FieldListView.as_view(), name='fields'),
    path('fields/<int:pk>', views.FieldDetailView.as_view(), name='fields-detail'),
    path('fields/create', views.FieldCreateView.as_view(), name='field-create'),
    path('fields/<int:pk>/update', views.FieldUpdateView.as_view(), name='field-update'),
    path('fields/<int:pk>/delete', views.FieldDeleteView.as_view(), name='field-delete'),

    path('organizations', views.OrganizationListView.as_view(), name='organizations'),
    path('organizations/<int:pk>', views.OrganizationDetailView.as_view(), name='organizations-detail'),
    path('organizations/create', views.OrganizationCreateView.as_view(), name='organization-create'),
    path('organizations/<int:pk>/update', views.OrganizationUpdateView.as_view(), name='organization-update'),
    path('organizations/<int:pk>/delete', views.OrganizationDeleteView.as_view(), name='organization-delete'),

    path('well-states', views.WellStateListView.as_view(), name='well-states'),
    path('well-states/<int:pk>', views.WellStateDetailView.as_view(), name='well-states-detail'),
    path('well-states/create', views.WellStateCreateView.as_view(), name='well-state-create'),
    path('well-states/<int:pk>/update', views.WellStateUpdateView.as_view(), name='well-state-update'),
    path('well-states/<int:pk>/delete', views.WellStateDeleteView.as_view(), name='well-state-delete'),

    path('pump-parameters', views.PumpParametersListView.as_view(), name='pump-parameters'),
    path('pump-parameters/<int:pk>', views.PumpParametersDetailView.as_view(), name='pump-parameters-detail'),
    path('pump-parameters/create', views.PumpParametersCreateView.as_view(), name='pump-parameters-create'),
    path('pump-parameters/<int:pk>/update', views.PumpParametersUpdateView.as_view(), name='pump-parameters-update'),
    path('pump-parameters/<int:pk>/delete', views.PumpParametersDeleteView.as_view(), name='pump-parameters-delete'),

    path('well-extractions', views.WellExtractionListView.as_view(), name='well-extractions'),
    path('well-extractions/<int:pk>', views.WellExtractionDetailView.as_view(), name='well-extractions-detail'),
    path('well-extractions/create', views.WellExtractionCreateView.as_view(), name='well-extractions-create'),
    path('well-extractions/<int:pk>/update', views.WellExtractionUpdateView.as_view(), name='well-extractions-update'),
    path('well-extractions/<int:pk>/delete', views.WellExtractionDeleteView.as_view(), name='well-extractions-delete'),

    path('core-samples', views.CoreSampleListView.as_view(), name='core-samples'),
    path('core-samples/<int:pk>', views.CoreSampleDetailView.as_view(), name='core-samples-detail'),
    path('core-samples/create', views.CoreSampleCreateView.as_view(), name='core-sample-create'),
    path('core-samples/<int:pk>/update', views.CoreSampleUpdateView.as_view(), name='core-sample-update'),
    path('core-samples/<int:pk>/delete', views.CoreSampleDeleteView.as_view(), name='core-sample-delete'),

    path('smushes', views.SmushListView.as_view(), name='smushes'),
    path('smushes/<int:pk>', views.SmushDetailView.as_view(), name='smushes-detail'),
    path('smushes/create', views.SmushCreateView.as_view(), name='smush-create'),
    path('smushes/<int:pk>/update', views.SmushUpdateView.as_view(), name='smush-update'),
    path('smushes/<int:pk>/delete', views.SmushDeleteView.as_view(), name='smush-delete'),

    path('clusters', views.ClusterListView.as_view(), name='clusters'),
    path('clusters/<int:pk>', views.ClusterDetailView.as_view(), name='clusters-detail'),
    path('clusters/create', views.ClusterCreateView.as_view(), name='cluster-create'),
    path('clusters/<int:pk>/update', views.ClusterUpdateView.as_view(), name='cluster-update'),
    path('clusters/<int:pk>/delete', views.ClusterDeleteView.as_view(), name='cluster-delete'),

    path('layers', views.LayerListView.as_view(), name='layers'),
    path('layers/<int:pk>', views.LayerDetailView.as_view(), name='layers-detail'),
    path('layers/create', views.LayerCreateView.as_view(), name='layer-create'),
    path('layers/<int:pk>/update', views.LayerUpdateView.as_view(), name='layer-update'),
    path('layers/<int:pk>/delete', views.LayerDeleteView.as_view(), name='layer-delete'),

]
