from typing import List, TYPE_CHECKING

from .map_domain import parse_domain

from meda.style import Style, ContourStyle

if TYPE_CHECKING:
    from .panel import Panel
    from .sub_chart import SubChart


class Chart:
    def __init__(self, panel: "Panel", domain: str):
        self.panel = panel
        self.subcharts: List["SubChart"] = []

        self.map_domain = parse_domain(domain)
        self.map_domain.set_chart(self)
        self.map_domain.render_chart()

    @property
    def fig(self):
        return self.panel.fig

    def add_subchart(self, sub_chart: "SubChart"):
        self.subcharts.append(sub_chart)

    def plot(self, data, style: "Style"):
        for sub_chart in self.subcharts:
            if isinstance(style, ContourStyle):
                if style.fill:
                    sub_chart.contourf(data=data, style=style)
                else:
                    sub_chart.contour(data=data, style=style)
            else:
                raise NotImplementedError("style is not implemented")