def round_value(value):
    if isinstance(value, float):
        value = round(value, 2)
    return value


def get_fields(model_obj, exclude_ids=True, exclude_foreign_keys=True):
    if not exclude_ids and not exclude_foreign_keys:
        fields = tuple(model_obj._meta.fields)
    else:
        fields = tuple(
            filter(lambda field:
                   (exclude_foreign_keys is False or field.get_internal_type() != "ForeignKey") and
                   (exclude_ids is False or field.verbose_name != "ID"),
                   model_obj._meta.fields))
    return fields


def get_field_names(model, exclude_ids=True, exclude_foreign_keys=True, exclude_fields=[], invert=False):
    fields = get_fields(model, exclude_ids, exclude_foreign_keys)
    if invert:
        result = {field.name: field.verbose_name for field in fields if field.name not in exclude_fields}
    else:
        result = {field.verbose_name: field.name for field in fields if field.name not in exclude_fields}
    return result


def get_field_values(model_object, exclude_ids=True, exclude_foreign_keys=True, exclude_fields=[]):
    fields = get_fields(model_object, exclude_ids, exclude_foreign_keys)
    result = [(field.verbose_name, round_value(field.value_from_object(model_object))) for field in fields if
              field.verbose_name not in exclude_fields]

    return result
