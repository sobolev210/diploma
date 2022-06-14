from django.contrib import admin
from core.models import *

admin.site.site_header = "Администрирование Нефть и газ"


@admin.register(Well)
class WellAdmin(admin.ModelAdmin):
    pass


@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    pass


@admin.register(Organization)
class OrganisationAdmin(admin.ModelAdmin):
    pass


@admin.register(WellState)
class StateAdmin(admin.ModelAdmin):
    pass


@admin.register(WellExtraction)
class ExtractionAdmin(admin.ModelAdmin):
    pass


@admin.register(CoreSample)
class CoreSampleAdmin(admin.ModelAdmin):
    pass


@admin.register(Smush)
class SmushAdmin(admin.ModelAdmin):
    pass


@admin.register(Cluster)
class ClusterAdmin(admin.ModelAdmin):
    pass


@admin.register(Layer)
class LayerAdmin(admin.ModelAdmin):
    pass


# @admin.register(ImportSchema)
# class ImportSchemaAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(ImportSchemaAttribute)
# class ImportSchemaAttributeAdmin(admin.ModelAdmin):
#     list_display = [
#         "column_position",
#         "type_name",
#         "attr_name",
#         "import_schema"
#     ]
