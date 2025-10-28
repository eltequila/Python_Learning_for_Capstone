import sys
from random import sample

from datalib_T5 import join
from pathlib import Path
from typing import List
import csv
from collections import namedtuple

csv_path = Path(r'/Users/macbookairfromboeing/Downloads/Penn/Courses/2025 Fall/ENVS 5726/Week 08 - Object-Oriented Data Analysis/Week08TutorialData/GemStat_Ganges_Water_Quality_Samples.csv')

with open(csv_path, 'r', encoding='utf-8-sig') as csv_file:
    reader:csv.reader = csv.reader(csv_file)
    headers:List[str] = next(reader)

    water_sample_columns = ['GEMS_Station_Number', 'Analyte', 'Value', 'Units']
    WaterSample: namedtuple = namedtuple(typename='WaterSample',field_names=water_sample_columns)

    sample_location_columns = ['GEMS_Station_Number', 'Latitude', 'Longitude']
    SampleLocation: namedtuple = namedtuple(typename='SampleLocation',field_names=sample_location_columns)

    water_sample_table: List[WaterSample] = []
    sample_location_table: List[SampleLocation] = []

    for row in reader:

        water_sample_row: List[str] = [row[headers.index(column)] for column in water_sample_columns]
        water_sample_table.append(WaterSample(*water_sample_row))

        sample_location_row: List[str] = [row[headers.index(column)] for column in sample_location_columns]
        sample_location_table.append(SampleLocation(*sample_location_row))

for row in water_sample_table[:3]:
    print(row)

for row in sample_location_table[:3]:
    print(row)


sys.path.insert(1,r'/Users/macbookairfromboeing/Downloads/Penn/Courses/2025 Fall/ENVS 5726/Week 08 - Object-Oriented Data Analysis/Week08TutorialData')

joined_table = join(
    target_table = water_sample_table,
    join_table = sample_location_table,
    join_column_name = 'GEMS_Station_Number',
)

for row in joined_table[:5]:
    print(row)