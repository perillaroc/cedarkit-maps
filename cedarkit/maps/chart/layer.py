from typing import Optional, TYPE_CHECKING

import xarray as xr
import matplotlib.axes
import matplotlib.contour
import matplotlib.quiver
import cartopy.crs as ccrs

from cedarkit.maps.style import ContourStyle, BarbStyle, ContourLabelStyle
from cedarkit.maps.graph import (
    add_contourf,
    add_contour,
    add_contour_label,
    add_barb,
)

if TYPE_CHECKING:
    from cedarkit.maps.chart import Chart


class Layer:
    """
    A layer is a map box in a ``Chart``. Each layer has a ``matplotlib.axes.Axes`` attribute to draw plots.

    Attributes
    ----------
    ax
    projection
    chart
    """
    def __init__(self, projection: ccrs.Projection, chart: Optional["Chart"] = None):
        self.ax: Optional[matplotlib.axes.Axes] = None
        self.projection = projection

        if chart is not None:
            self.set_chart(chart)
        else:
            self.chart = None

    def add_axes(self, ax: matplotlib.axes.Axes):
        self.ax = ax

    def set_chart(self, chart: "Chart"):
        """
        Add ``Layer`` to a ``Chart``.

        Parameters
        ----------
        chart
        """
        self.chart = chart
        self.chart.add_layer(self)

    def contourf(self, data: xr.DataArray, style: ContourStyle, **kwargs) -> matplotlib.contour.QuadContourSet:
        contour = add_contourf(
            self.ax,
            field=data,
            projection=self.projection,
            levels=style.levels,
            cmap=style.colors,
            **kwargs
        )
        if style.label:
            label = Layer.contour_label(self.ax, contour, style.label_style)
        return contour

    def contour(self, data: xr.DataArray, style: ContourStyle, **kwargs) -> matplotlib.contour.QuadContourSet:
        contour = add_contour(
            self.ax,
            field=data,
            projection=self.projection,
            levels=style.levels,
            colors=style.colors,
            linewidths=style.linewidths,
            **kwargs
        )
        if style.label:
            label = Layer.contour_label(self.ax, contour, style.label_style)

        return contour

    @classmethod
    def contour_label(cls, ax, contour, style: ContourLabelStyle):
        kwargs = dict(
            fontsize=style.fontsize,
            inline=style.inline,
            inline_spacing=style.inline_spacing,
            fmt=style.fmt,
            colors=style.colors,
            manual=style.manual,
            zorder=style.zorder,
        )

        label = add_contour_label(
            ax,
            contour=contour,
            **kwargs
        )
        return label

    def barb(self, x: xr.DataArray, y: xr.DataArray, style: BarbStyle, **kwargs) -> matplotlib.quiver.Barbs:
        barb = add_barb(
            self.ax,
            x_field=x,
            y_field=y,
            projection=self.projection,
            barb_increments=style.barb_increments,
            length=style.length,
            linewidth=style.linewidth,
            pivot=style.pivot,
            barbcolor=style.barbcolor,
            flagcolor=style.flagcolor,
            regrid_shape=20,
            **kwargs,
        )
        return barb
