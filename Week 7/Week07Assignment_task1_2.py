import csv
import urllib
import requests
from pathlib import Path
from pprint import pprint

csv_path = Path (r'/Users/macbookairfromboeing/Downloads/Penn/Courses/2025 Fall/ENVS 5726/Week 07 - REST APIs/Week07AssignmentData/USEIA_Petroleum_Refineries_By_Nearest_Major_City.csv')

with open(csv_path, 'r', encoding='utf-8') as RefineryFile:
    reader = csv.reader(RefineryFile)
    headers = next(reader)
    table = list(reader)

    base_fema_hazard_zones_url = 'https://hazards.fema.gov/arcgis/rest/services/public/NFHL/MapServer/28/query'

    for row in table:
        query = {
            'geometry': f'{row[headers.index('Longitude')]},{row[headers.index('Latitude')]}',
            'inSR': '4326',
            'geometryType': 'esriGeometryPoint',
            'spatialRel': 'esriSpatialRelIntersects',
            'outFields': 'ZONE_SUBTY',
            'returnGeometry': 'false',
            'f': 'pjson'
        }

        encoded_query = urllib.parse.urlencode(query)

        fema_hazard_zones_url = base_fema_hazard_zones_url + '?' + encoded_query

        response = requests.get(url=fema_hazard_zones_url)

        fema_hazard_zone_data = response.json()

        if len(fema_hazard_zone_data['features']) > 0:

            data_status = fema_hazard_zone_data['features'][0]['attributes']['ZONE_SUBTY']

            if data_status is None:
                data_status = 'No Data'

        else:
            data_status = 'No Data'

        row.append(data_status)

new_headers = headers + ['ZONE_SUBTY']

# print(new_headers)
# for row in table:
#     print(row)

export_path = Path(r'/Users/macbookairfromboeing/Downloads/Penn/Courses/2025 Fall/ENVS 5726/Week 07 - REST APIs/Week07AssignmentData/task1_table.csv')
with open(export_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows([new_headers] + table)