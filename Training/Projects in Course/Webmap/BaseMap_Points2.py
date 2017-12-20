import folium
import random

BaseMap = folium.Map(location=[-26,28],zoom_start=8, tiles="MapBox Bright")

# Can add child objects directly, but might become cumbersome
# BaseMap.add_child(folium.Marker(location=[-26.094805,27.99986], popup="You are here!", icon=folium.Icon("info-sign")))

# Create a feature group to overcome the above
Features = folium.FeatureGroup(name="Markers and Features")
for i in range(10):
    Features.add_child(folium.Marker(location=[random.randrange(-90,90),random.randrange(-180,180)], popup="Far far away", icon=folium.Icon(color="green")))
BaseMap.add_child(Features)

# Build Final Map and save
BaseMap.save("BaseMap.html")