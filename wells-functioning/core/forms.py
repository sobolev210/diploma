from django.forms import ModelForm, Textarea, DateInput, TextInput
from .models import *


class DateInput(DateInput):
    input_type = 'date'

    def format_value(self, value):
        return value


class WellForm(ModelForm):
    class Meta:
        model = Well
        fields = "__all__"
        widgets = {
            'comment': Textarea(attrs={'cols': 50, 'rows': 3}),
            'operator': TextInput(attrs={'style': "width:300px"}),
            'start_date_of_drilling': DateInput(),
            'completion_date_of_drilling': DateInput(),
            'service_date': DateInput()
        }


class WellStateForm(ModelForm):
    class Meta:
        model = WellState
        fields = "__all__"
        widgets = {
            'record_date': DateInput()
        }


class PumpParametersForm(ModelForm):
    class Meta:
        model = PumpParameters
        fields = "__all__"
        widgets = {
            'pump_parameters_measurement_date': DateInput()
        }


class WellExtractionForm(ModelForm):
    class Meta:
        model = WellExtraction
        fields = "__all__"
        widgets = {
            'record_date': DateInput()
        }


class CoreSampleForm(ModelForm):

    class Meta:
        model = CoreSample
        fields = "__all__"
        widgets = {
            'sampling_date': DateInput()
        }
