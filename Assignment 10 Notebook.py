from datetime import datetime as dt

from arcgis.gis import GIS
from arcgis.raster import analytics, band_arithmetic, colormap, extract_band, gbl, remap, slope
from ipywidgets import HBox, Layout

type(gis.content)

gis = GIS(user="DevonJohnson")

#wfusa = gis.content.search("title:USA_Current_Wildfires owner:esri",
#                         item_type="Feature_Layer")
search_result = gis.content.search(query="title:USA Current Wildfires owner:esri_livefeeds2", item_type="Feature Layer")
search_result

map1 = gis.map(location="-117.25, 47.39")
map1.layout = Layout(flex="1 1", height="500px", padding="10px")
map2 = gis.map(location="-117.25, 47.39")
map2.layout = Layout(flex="1 1", height="500px", padding="10px")
map2.content.add(search_result)
box1 = HBox([map1,map2])
box1

map1.zoom = 8
map2.zoom = 8


