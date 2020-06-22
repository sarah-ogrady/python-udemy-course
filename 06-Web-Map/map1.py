import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
elev = list(data["ELEV"])

html = """<h4>Volcano information:</h4>
<p>Name: %s</p>
<p>Height: %s m</p>
"""

map = folium.Map(location=[38.2, -99.1], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for lt, ln, el, nm in  zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (nm, el), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon('blue')))

map.add_child(fg)
map.save("Map1.html")

