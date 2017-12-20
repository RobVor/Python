import folium

BaseMap = folium.Map(location=[-26,28],zoom_start=8, tiles="MapBox Bright")

# Can add child objects directly, but might become cumbersome
# BaseMap.add_child(folium.Marker(location=[-26.094805,27.99986], popup="You are here!", icon=folium.Icon("info-sign")))

# Create a feature group to overcome the above
Features = folium.FeatureGroup(name="Markers and Features")
Features.add_child(folium.Marker(location=[-26.094805,27.99986], popup="You are here!", icon=folium.Icon(color="green")))
Features.add_child(folium.Marker(location=[28.392218,-80.607713], popup="Far far away...", icon=folium.Icon(color="green")))
BaseMap.add_child(Features)

# Build Final Map and save
BaseMap.save("BaseMap.html")