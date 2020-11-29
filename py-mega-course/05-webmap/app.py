import folium
import pandas

_dataFilepath = 'volcanoes.txt'
_initCoordinates = (43.09, -118.75)
_initZoom = 6

def get_popup_info( data, index ):
    name = data["NAME"][index]
    status = data["STATUS"][index]
    type = data["TYPE"][index]
    elevation = data["ELEV"][index]

    # info = "Name: " + str(name[ index ]) + " | Status: " + str(status[ index ]) + " | Type: " + str(type[ index ]) + " | Elevation: " + str(elevation[ index ]) + "m"
    html = ''' <h5>%s</h5>
    <p><strong>Status:</strong> %s</p>
    <p><strong>Type:</strong> %s</p>
    <p><strong>Elevation:</strong> %sm</p>
    '''
    info = html % (name, status, type, elevation)
    return info

def get_icon_colour( data, index):
    elevation = data["ELEV"][index]

    if elevation <= 1500:
        return "green"
    elif elevation > 1500 and elevation < 2500:
        return "orange"
    else:
        return "red"

def get_marker_group( groupName = "Volcanoes", dataFilepath = _dataFilepath ):
    print("\nCreating marker group for " + str(groupName) + "..." )

    data = pandas.read_csv( dataFilepath )
    lat = list( data["LAT"] )
    lon = list( data["LON"])

    dataCoords = []
    for i, j in zip( lat, lon ):
        dataCoords.append( ( i, j ) )

    markerGroup = folium.FeatureGroup( name = groupName )
    index = 0
    for coord in dataCoords:
        popupInfo = get_popup_info( data, index )
        iconColour = get_icon_colour( data, index)
        index += 1
        #markerGroup.add_child( folium.Marker( location = coord, popup = popupInfo, icon = folium.Icon( color = iconColour, icon='ellipse' ) ) )
        markerGroup.add_child( folium.CircleMarker( location = coord, radius=7, popup = popupInfo, color = iconColour, fill_colour=iconColour, fill=True, fill_opacity=0.7) )

    return markerGroup

def run( initCoordinates = _initCoordinates, initZoom = _initZoom ):

    print( "\nCreating base map...")
    map = folium.Map( location = initCoordinates, zoom_start = initZoom, tiles = "Stamen Terrain" )

    volcanoMarkerGroup = get_marker_group()

    map.add_child( volcanoMarkerGroup )

    map.save("map.html")

    print( "\nMap created.\n")

run()
