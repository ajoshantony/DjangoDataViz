from myFunctions import *
import re
newUnit = str(readUnit())
if newUnit.endswith('None'):
    newUnit = newUnit[:-4]




Data =  {
    'geometry': {'coordinates': [-117.6718333, 35.9995, 2.17], 'type': 'Point'}, 
    'id': 'ci38173768', 
    'type': 'Feature', 
    'properties': 
    {'dmin': 0.05435, 'code': '38173768', 'sources': ',ci,', 'tz': -480, 'mmi': None, 'type': 'earthquake', 'title': 'M 2.0 - 22km ENE of Little Lake, CA', 'magType': 'ml', 'nst': 23, 'sig': 60, 'tsunami': 0, 'mag': 1.97, 'alert': None, 'gap': 55, 'rms': 0.15, 'place': '22km ENE of Little Lake, CA', 'net': 'ci', 'types': ',focal-mechanism,geoserve,nearby-cities,origin,phase-data,scitech-link,', 'felt': None, 'cdi': None, 'url': 'https://earthquake.usgs.gov/earthquakes/eventpage/ci38173768', 'ids': ',ci38173768,', 'time': 1526432517070, 'detail': 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/ci38173768.geojson', 'updated': 1526433186900, 'status': 'automatic'}}


print(Data)