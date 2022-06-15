# import itertools
#
# import pandas as pd
# from abc import ABC, abstractmethod
# from itertools import groupby
# import operator
#
# from django.apps import apps
#
# from core.models import ImportSchema, ImportSchemaAttribute
#
#
#
# class DataImporter(ABC):
#
#     def __init__(self, schema_id, filename):
#         self._schema_id = schema_id
#         self._filename = filename
#
#
#     @abstractmethod
#     def parse_file(self) -> pd.DataFrame:
#         raise NotImplementedError
#
#
# class CsvDataImporter(DataImporter):
#
#     def parse_file(self) -> pd.DataFrame:
#         df = pd.read_csv(self._filename)
#         return df
#
#
# class ExcelDataImporter(DataImporter):
#
#     def parse_file(self) -> pd.DataFrame:
#         df = pd.read_excel(self._filename)
#         return df
#
#     def iter_rows(self):
#         df = self.parse_file()
#         return df.iter_rows(values_only=True)
#
#     def prepare_attrs_for_model(self, model, attr_names):
#         result = []
#         print(attr_names)
#         for field in model._meta.fields:
#             print(field.verbose_name)
#             if field.verbose_name in attr_names:
#                 result.append((field, attr_names[field.verbose_name]))
#         print(result)

#     def prepare_import_schema(self):
#         #todo move to init
#         type_name_index = 2
#         import_schema = ImportSchema.objects.filter(pk=self._schema_id).first()
#         if not import_schema:
#             pass
#             # raise (f"Undefined project with pk={self._schema_id}")
#         values_list = import_schema.attributes.values_list()
#         print(import_schema.attributes.values())
#         sorted_values_list = sorted(values_list, key=operator.itemgetter(type_name_index))
#         grouped_dict = {
#             model_name: [item for item in items]
#             for model_name, items in itertools.groupby(sorted_values_list, key=operator.itemgetter(type_name_index))
#         }
#         models = []
#         for model_name, items in grouped_dict.items():
#             model = apps.get_model(app_label='core', model_name=model_name)
#             # атрибут и столбик
#             attr_names = [{item[3]: item[1]} for item in items]
#             attributes = self.prepare_attrs_for_model(model, attr_names)

# a = ExcelDataImporter(schema_id=1, filename="123")
# a.prepare_import_schema()

