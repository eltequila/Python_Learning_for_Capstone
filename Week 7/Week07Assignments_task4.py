import csv
import urllib
import requests
from pathlib import Path

csv_path = Path (r'/Users/macbookairfromboeing/Downloads/Penn/Courses/2025 Fall/ENVS 5726/Week 07 - REST APIs/Week07AssignmentData/USEIA_Petroleum_Refineries_By_Nearest_Major_City.csv')

with open(csv_path, 'r', encoding='utf-8') as RefineryFile:
    reader = csv.reader(RefineryFile)
    headers = next(reader)
    table = list(reader)

    for row in table:

        origin_coordinates = f'{row[headers.index('Longitude')]},{row[headers.index('Latitude')]}'
        destination_coordinates = f'{row[headers.index('NearestMajorCity_Longitude')]},{row[headers.index('NearestMajorCity_Latitude')]}'

        nav_base_url = f'https://routing.openstreetmap.de/routed-car/route/v1/driving/{origin_coordinates};{destination_coordinates}'

        query = {
            'overview':'false',
            'alternatives':'false',
            'steps':'false'
        }

        encoded_query = urllib.parse.urlencode(query)

        full_url = nav_base_url + '?' + encoded_query

        response = requests.get(url = full_url)

        nav_result = response.json()

        drive_duration = nav_result['routes'][0]['duration']

        row.append(drive_duration)

updated_headers = headers + ['DriveDuration_Seconds']

export_path = Path(r'/Users/macbookairfromboeing/Downloads/Penn/Courses/2025 Fall/ENVS 5726/Week 07 - REST APIs/Week07AssignmentData/task4_table_with_duration.csv')
with open(export_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows([updated_headers] + table)