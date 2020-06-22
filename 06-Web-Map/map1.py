import folium
import pandas
import fontawesome as fa

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
elev = list(data["ELEV"])

html = """<h4>Volcano information:</h4>
Name: <a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a>
<p>Height: %s m</p>
"""

map = folium.Map(location=[38.2, -99.1], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

def what_color(elevation):
  if elevation <= 1000:
    return 'lightblue'
  elif elevation > 1000 and elevation < 2000:
    return 'blue'
  elif elevation >= 2000 and elevation <= 3000:
    return 'cadetblue'
  else:
    return 'darkblue'


for lt, ln, el, nm in  zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (nm, nm, el), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color=what_color(el), icon='fa-tree', prefix='fa')))


fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x["properties"]["POP2005"] < 20000000 else 'red'}))

map.add_child(fg)
map.save("Map1.html")

