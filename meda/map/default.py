"""
默认中国区域底图，使用 dongli/china-shapefiles 项目中的 Shapefile，已包含在本项目 resources 目录中。

项目地址：https://github.com/dongli/china-shapefiles
"""
import importlib.resources

import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.io.shapereader import Reader


def get_china_map():
    ref = importlib.resources.files("meda") / "resources/map/china-shapefiles/shapefiles/china.shp"
    with importlib.resources.as_file(ref) as china_shape_file:
        china_shape_reader = Reader(china_shape_file)

        projection = ccrs.PlateCarree()
        cn_feature = cfeature.ShapelyFeature(
            china_shape_reader.geometries(),
            projection,
            edgecolor='k',
            facecolor='none'
        )

    return [cn_feature]


def get_china_nine_map():
    ref = importlib.resources.files("meda") / "resources/map/china-shapefiles/shapefiles/china_nine_dotted_line.shp"
    with importlib.resources.as_file(ref) as china_nine_dotted_shape_file:
        china_nine_dotted_shape_reader = Reader(china_nine_dotted_shape_file)

        projection = ccrs.PlateCarree()
        nine_feature = cfeature.ShapelyFeature(
            china_nine_dotted_shape_reader.geometries(),
            projection,
            edgecolor='k',
            facecolor='none'
        )

    return [nine_feature]
