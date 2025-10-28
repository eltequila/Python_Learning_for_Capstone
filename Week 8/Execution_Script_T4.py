from pathlib import Path
from typing import List
import csv
from collections import namedtuple

csv_path:Path = Path(r'/Users/macbookairfromboeing/Downloads/Penn/Courses/2025 Fall/ENVS 5726/Week 08 - Object-Oriented Data Analysis/Week08TutorialData/GemStat_Ganges_Water_Quality_Samples.csv')

with open(csv_path,'r',encoding='utf-8-sig') as csvfile:
    reader:csv.reader = csv.reader(csvfile)
    headers:List[str] = next(reader)

    WaterSample:namedtuple = namedtuple(typename='WaterSample',field_names=headers)

    water_sample_table: List[WaterSample] = []

    for row in reader:
        water_sample:WaterSample = WaterSample(*row)
        calculated_water_sample:WaterSample = water_sample._replace(Value=float(water_sample.Value))
        water_sample_table.append(calculated_water_sample)

import sys
sys.path.insert(1,r'/Users/macbookairfromboeing/Python_Learning_for_Capstone/Week 8')

from datalib_T4 import summarize
mean_value:float = summarize(table = water_sample_table, summary_method = 'MEAN', value_column = 'Value')
print(mean_value)






from datalib_T4 import summrize_by_category

values_by_agency_table: List[tuple] = summrize_by_category(
    table = water_sample_table,
    summary_method='COUNT',
    value_column = 'Value',
    category_column = 'Responsible_Collection_Agency'
)

for row in values_by_agency_table:
    print(row)



