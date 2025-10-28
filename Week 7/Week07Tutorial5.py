import urllib
import requests
from pprint import pprint

fema_hazard_zones_url = 'https://hazards.fema.gov/arcgis/rest/services/public/NFHL/MapServer/28/query'

query = {
    'geometry':'-90.050971,29.935670',
    'inSR':'4326',
    'geometryType':'esriGeometryPoint',
    'spatialRel':'esriSpatialRelIntersects',
    'outFields':'ZONE_SUBTY',
    'returnGeometry':'false',
    'f':'pjson'
}

encoded_query = urllib.parse.urlencode(query)

fema_hazard_zones_url = fema_hazard_zones_url + '?' + encoded_query

# print(fema_hazard_zones_url)

fema_hazard_zone_data = requests.get(url = fema_hazard_zones_url).json()

pprint(fema_hazard_zone_data, width = 100)
print(fema_hazard_zone_data['features'][0]['attributes']['ZONE_SUBTY'])



numbers_set_1 = (1,5,8,0)
numbers_set_2 = (1,6,8,0)
numbers = numbers_set_1 + numbers_set_2
num = 6

if num in numbers_set_1:
    print('num is in numbers')

elif num in numbers_set_2:
    print('num is in numbers')

else:
    print('num is not in numbers')

