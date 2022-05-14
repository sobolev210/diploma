
def get_field_names(model, exclude_ids=True, exclude_foreign_keys=True, exclude_fields=[], invert=False):
    if not exclude_ids and not exclude_foreign_keys:
        fields = tuple(model._meta.fields)
    else:
        fields = tuple(
            filter(lambda field:
                   (exclude_foreign_keys is False or field.get_internal_type() != "ForeignKey") and
                   (exclude_ids is False or field.verbose_name != "ID"),
                   model._meta.fields))
    if invert:
        result = {field.name: field.verbose_name for field in fields if field.verbose_name not in exclude_fields}
    else:
        result = {field.verbose_name: field.name for field in fields if field.verbose_name not in exclude_fields}
    return result
