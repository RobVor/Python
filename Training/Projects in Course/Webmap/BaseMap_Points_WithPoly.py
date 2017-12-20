import folium
import random
import pandas
import json

BaseMap = folium.Map(location=[40.76,-111.89],zoom_start=6, tiles="MapBox Bright")

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

POPS = {}
with open("world.json", "r", encoding='utf-8-sig') as DataSource:
    DataSource.seek(0)
    Source = DataSource.read()
    Content = json.loads(Source)
for i in range(len(Content["features"])):
     POPS[Content["features"][i]["properties"]["NAME"]]=Content["features"][i]["properties"]["POP2005"]
print(POPS)

# Can add child objects directly, but might become cumbersome
# BaseMap.add_child(folium.Marker(location=[-26.094805,27.99986], popup="You are here!", icon=folium.Icon("info-sign")))

# Create a feature group to overcome the above
Volcanoes = folium.FeatureGroup(name="Markers and Features - Volcanoes")
for i,j,k,l,m in zip(LAT,LON,VOLC_Names,ELEV,CCodes):
    Names = folium.Popup(k+", "+str(l)+"m",parse_html=True)
    Volcanoes.add_child(folium.CircleMarker(location=[i,j],radius=4,popup=Names,color=m,fill=True,fill_opacity=0.5))
    #Features.add_child(folium.Marker(location=[i, j], popup=Names, icon=folium.Icon(color=m, prefix="fa", icon="circle-thin")))

Population = folium.FeatureGroup(name="Markers and Features - Population")
#Features.add_child(folium.GeoJson(data=open('world.json', 'r',encoding='utf-8-sig').read(),
#                                  style_function= lambda x: {'fillColor':'yellow' if x['properties']['POP2005'] < 5000000 else 'orange'}))
Population.add_child(folium.GeoJson(data=open('world.json', 'r',encoding='utf-8-sig').read(),
                                  style_function= lambda x: {'fillColor':'blue' if x['properties']['POP2005'] < 1000000
                                                             else 'orange' if x['properties']['POP2005']>= 1000001 and x['properties']['POP2005'] <= 5000000
                                                             else 'green' if x['properties']['POP2005'] >= 5000001 and x['properties']['POP2005'] <= 10000000
                                                             else 'yellow' if x['properties']['POP2005'] >= 10000001 and x['properties']['POP2005'] <= 100000000
                                                             else 'red'}))

BaseMap.add_child(Volcanoes)
BaseMap.add_child(Population)
BaseMap.add_child(folium.LayerControl())

# Build Final Map and save
BaseMap.save("BaseMap.html")