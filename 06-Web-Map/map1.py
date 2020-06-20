import folium
map = folium.Map(location=[38.2, -99.1], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for coordinates in [[38.2, -99.1], [32.2, -97.1]]:
    fg.add_child(folium.Marker(location=coordinates, popup="hi im a marker", icon=folium.Icon('green')))

map.add_child(fg)
map.save("Map1.html")

