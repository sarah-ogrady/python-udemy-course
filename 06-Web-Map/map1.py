import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")

lat = list(data["LAT"])

lon = list(data["LON"])

map = folium.Map(location=[38.2, -99.1], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for lat, lon in  zip(lat, lon):
    fg.add_child(folium.Marker(location=[lat, lon], popup="hi im a marker", icon=folium.Icon('green')))

map.add_child(fg)
map.save("Map1.html")

