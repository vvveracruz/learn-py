import folium
import pandas

_initCoords = (43.09, -118.75)
_initZoom = 6

data = pandas.read_csv("volcanoes.txt")
lat = data["LAT"]
lon = data["LON"]
elev = data["ELEV"]
name = data["NAME"]

def get_marker_colour( elevation ):
    if elevation <= 1500:
        return "green"
    elif elevation > 1500 and elevation < 2500:
        return "orange"
    else:
        return "red"

print("\nCreating map..." )
map = folium.Map(
    location = _initCoords,
    zoom_start= _initZoom,
    tiles = "Stamen Terrain" )

featureGroup = folium.FeatureGroup( name = "My Map" )

print("\nCreating volcanoes marker group..." )
volcanoFeatureGroup = folium.FeatureGroup( name = "US Volcanoes" )
for lt, ln, el, n in zip( lat, lon, elev, name ):
    volcanoFeatureGroup.add_child( folium.CircleMarker(
        location = (lt, ln),
        radius = 6,
        popup = "<h6>%s</h6> %sm" % ( str(n), str(el) ),
        fill_colour = get_marker_colour( el ),
        color = get_marker_colour( el ),
        fill_opacity = 0.8,
        fill = True ) )
map.add_child( volcanoFeatureGroup )

print("\nCreating polygons...")
polygonFeatureGroup = folium.FeatureGroup( name = "Polygons" )
polygonFeatureGroup.add_child(
    folium.GeoJson( open( "world.json", 'r', encoding="utf-8-sig" ).read(),
    style_function = lambda x: { 'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange'} ) )
map.add_child( polygonFeatureGroup )

print("\nCreating layer toggles...")
map.add_child( folium.LayerControl()  )

map.save("map.html")

print("\nMap saved.\n")
