import folium
import random
import pandas

BaseMap = folium.Map(location=[-26,28],zoom_start=8, tiles="MapBox Bright")
PointSource = pandas.read_csv("Volcanoes_USA.txt")
LAT = list(PointSource["LAT"])
LON = list(PointSource["LON"])
VOLC_Names = list(PointSource["NAME"])
ELEV = list(PointSource["ELEV"])
CCodes = []
for c in ELEV:
    if c <= 1500:
        CCodes.append("green")
    elif c <= 2500 and c >= 1501:
        CCodes.append("blue")
    elif c <= 3500 and c >= 2501:
        CCodes.append("orange")
    else:
        CCodes.append("red")

# Can add child objects directly, but might become cumbersome
# BaseMap.add_child(folium.Marker(location=[-26.094805,27.99986], popup="You are here!", icon=folium.Icon("info-sign")))

# Create a feature group to overcome the above
Features = folium.FeatureGroup(name="Markers and Features")
for i,j,k,l,m in zip(LAT,LON,VOLC_Names,ELEV,CCodes):
    Names = folium.Popup(k+", "+str(l)+"m",parse_html=True)
    Features.add_child(folium.CircleMarker(location=[i,j],radius=4,popup=Names,color=m,fill=True,fill_opacity=0.5))
    #Features.add_child(folium.Marker(location=[i, j], popup=Names, icon=folium.Icon(color=m, prefix="fa", icon="circle-thin")))
BaseMap.add_child(Features)

# Build Final Map and save
BaseMap.save("BaseMap.html")
print(help(folium.CircleMarker))