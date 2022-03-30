from django.contrib import admin
from core.models import *

admin.site.site_header = "Администрирование ТрансГазНефть"


@admin.register(Well)
class WellAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'purpose',
        'drilling_mud',
        'profile',
        'sank_amount',
        'drilling_cost',
        'developing_cost',
        'field'
    ]


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = [
        'status',
        'created_at',
        'downtime',
        'reason',
        'well'
    ]


@admin.register(Extraction)
class ExtractionAdmin(admin.ModelAdmin):
    list_display = [
        'created_at',
        'oil_output',
        'gas_output',
        'well'
    ]


@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'x_coordinate',
        'y_coordinate',
        'reservoir_age',
        'formation_saturation',
        'organisation'
    ]


@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'amount_of_workers',
        'description'
    ]


@admin.register(ImportSchema)
class ImportSchemaAdmin(admin.ModelAdmin):
    pass


@admin.register(ImportSchemaAttribute)
class ImportSchemaAttributeAdmin(admin.ModelAdmin):
    list_display = [
        "column_position",
        "type_name",
        "attr_name",
        "import_schema"
    ]





