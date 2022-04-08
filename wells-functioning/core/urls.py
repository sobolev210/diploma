from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'core'

urlpatterns = [
    path('', TemplateView.as_view(template_name='core/main.html'), name="main"),
    path('open', views.OpenView.as_view(), name='open'),
    path('apereo', views.ApereoView.as_view(), name='apereo'),
    path('manual', views.ManualProtect.as_view(), name='manual'),
    path('protect', views.ProtectView.as_view(), name='protect'),
    path('python', views.DumpPython.as_view(), name='python'),
    path('wells', views.WellListView.as_view(), name='wells'),
    path('wells/create', views.WellCreateView.as_view(), name='wells-create'),
    path('wells/table', views.WellTableView.as_view(), name='wells-table'),
    path('wells/charts/extraction', views.WellExtractionChartView.as_view(), name='wells-extraction-chart'),
    #path('wells/extended-table', views.ExtendedWellTableView.as_view(), name='wells-extended-table'),
    #path('wells/sucess-url', views.WellCreateView.as_view(), name='wells-create'),
    path('wells/<int:pk>', views.WellDetailView.as_view(), name='wells-detail'),
    path('fields/<int:pk>', views.FieldDetailView.as_view(), name='fields-detail'),
    path('fields/create', views.FieldCreateView.as_view(), name='fields-create'),
]
