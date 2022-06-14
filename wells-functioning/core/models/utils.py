from core.utils import get_field_values


class GetFieldsMixin:
    def get_fields(self):
        return get_field_values(self)
