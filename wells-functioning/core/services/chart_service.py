import os

import pandas as pd
from django.conf import settings

from core.models import WellExtraction


class WellExtractionChart:

    def __init__(self, chart_type: str, well_name: str):
        self.chart_type = chart_type
        self.well_name = well_name

    def build_chart(self) -> str:
        well_extractions = WellExtraction.objects.filter(well__name=self.well_name).order_by("year")
        df = pd.DataFrame(well_extractions.values("year", "gas_output_m3", "oil_output_t", "liquid_output_m3"))
        figure = df.plot(kind="bar", x="year", y=["gas_output_m3", "oil_output_t", "liquid_output_m3"]).get_figure()
        path = os.path.join(settings.MEDIA_ROOT, "chart.png")
        figure.savefig(path)
        return "chart.png"
