from typing import NamedTuple

class MyRowTuple(NamedTuple):
    column1: str
    column2: int
    column3: float

my_table_namedtuple = [
    MyRowTuple(column1='a', column2=1, column3=0.5),
    MyRowTuple(column1='b', column2=10, column3=0.5),
    MyRowTuple(column1='c', column2=100, column3=0.5),
]

row_2_column2 = my_table_namedtuple[1].column2
print(row_2_column2)


from pathlib import Path
import csv

class WaterSample(NamedTuple):
    station_number: str
    analyte: str
    value: str
    units: str

csv_path = Path(r'/Users/macbookairfromboeing/Downloads/Penn/Courses/2025 Fall/ENVS 5726/Week 08 - Object-Oriented Data Analysis/Week08TutorialData/GemStat_Ganges_Water_Quality_Samples.csv')
water_sample_table = []

with open(csv_path, 'r', encoding = 'utf-8-sig') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)

    for row in reader:
        water_sample = WaterSample(
            station_number = row[header.index('GEMS_Station_Number')],
            analyte = row[header.index('Analyte')],
            value = row[header.index('Value')],
            units = row[header.index('Units')],
        )
        water_sample_table.append(water_sample)

for row in water_sample_table[:4]:
    print(row)



# Defined NamedTuples
import datetime

class WaterSample(NamedTuple):
    station_number: str
    analyte: str
    collection_date: datetime.datetime
    value: float
    units: str

    @classmethod
    def load_from_row(cls, row, header):
        return WaterSample(
            station_number = row[header.index('GEMS_Station_Number')],
            analyte = row[header.index('Analyte')],
            collection_date = datetime.datetime.strptime(
                row[header.index('Collection_Date')],
                '%m/%d/%Y 0:00')
            if row[header.index('Collection_Date')]
            else None,
            value = float(row[header.index('Value')]),
            units = row[header.index('Units')]
        )

csv_path = Path(r'/Users/macbookairfromboeing/Downloads/Penn/Courses/2025 Fall/ENVS 5726/Week 08 - Object-Oriented Data Analysis/Week08TutorialData/GemStat_Ganges_Water_Quality_Samples.csv')
water_sample_table = []

with open(csv_path, 'r', encoding = 'utf-8-sig') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)

    for row in reader:
        water_sample = WaterSample.load_from_row(row, header)
        water_sample_table.append(water_sample)

for row in water_sample_table[:4]:
    print(row)


# Dynamic NamedTuples with Argument List Unpacking
from collections import namedtuple

csv_path = Path(r'/Users/macbookairfromboeing/Downloads/Penn/Courses/2025 Fall/ENVS 5726/Week 08 - Object-Oriented Data Analysis/Week08TutorialData/GemStat_Ganges_Water_Quality_Samples.csv')
water_sample_table = []

with open(csv_path, 'r', encoding = 'utf-8-sig') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)

    WaterSample = namedtuple(typename='WaterSample', field_names=header)

    for row in reader:
        water_sample = WaterSample(*row)
        water_sample_table.append(water_sample)

for row in water_sample_table[:4]:
    print(row)



# Filtering NamedTuples
from typing import List

csv_path:Path = Path(r'/Users/macbookairfromboeing/Downloads/Penn/Courses/2025 Fall/ENVS 5726/Week 08 - Object-Oriented Data Analysis/Week08TutorialData'
                     r'/GemStat_Ganges_Water_Quality_Samples.csv')

with open(csv_path, 'r', encoding = 'utf-8-sig') as csvfile:
    reader:csv.reader = csv.reader(csvfile)
    headers:List[str] = next(reader)

    WaterSample = namedtuple(typename='WaterSample', field_names=headers)
    water_sample_table: List[WaterSample] = []

    for row in reader:
        water_sample:WaterSample = WaterSample(*row)
        water_sample_table.append(water_sample)


filtered_water_samples:List[WaterSample] = []
for row in water_sample_table:

    collection_agency:str = row.Responsible_Collection_Agency

    if collection_agency == 'Government of India - Central Water Commission':
        filtered_water_samples.append(row)

print(f'Filtered {len(filtered_water_samples)} '
      f'out of {len(water_sample_table)} rows '
      f'where Responsible_Collection_Agency = "Government of India - Central Water Commission"')


# Filtering using List Comprehension
filtered_water_sample_table:List[WaterSample] = [row for row in water_sample_table if float(row.Value) > 0.45]
print(f'Filtered {len(filtered_water_sample_table)} '
      f'out of {len(water_sample_table)} rows '
      f'where nitrate mg/L > 0.45.')



# Calculating NamedTuples
calculated_water_sample_table: List[WaterSample] = []
for row in water_sample_table:

    calculated_row:WaterSample = row._replace(Value = float(row.Value))

    calculated_water_sample_table.append(calculated_row)

print(calculated_water_sample_table[0])

calculated_water_sample_table:List[WaterSample] = [
    row._replace(
        Value = float(row.Value),
        Collection_Date = datetime.datetime.strptime(row.Collection_Date, '%m/%d/%Y 0:00')
        if row.Collection_Date else None,
    )
    for row in water_sample_table
]

print(calculated_water_sample_table[0])



# Calculating New Columns with NamedTuples
NewWaterSample:namedtuple = namedtuple(
    typename='NewWaterSample',
    field_names=list(WaterSample._fields) + ['Above_BIS_Limit']
)

water_sample_table_with_bis_limit: List[NewWaterSample] = []
for row in calculated_water_sample_table:

    above_bis_limit:bool = True if row.Value >0.45 else False

    water_sample_with_bis_limit:NewWaterSample = NewWaterSample(*row, Above_BIS_Limit = above_bis_limit)

    water_sample_table_with_bis_limit.append(water_sample_with_bis_limit)

print(water_sample_table_with_bis_limit[0])


# Filtering Columns with NamedTuples
SampleLocation: namedtuple = namedtuple(
    typename='SampleLocation',
    field_names=('GEMS_Station_Number','Latitude', 'Longitude','Distance_From_Bangladesh_Meters')
)

sample_location_table:List[SampleLocation] = []
for row in water_sample_table:

    sample_location:SampleLocation = SampleLocation(
        GEMS_Station_Number=row.GEMS_Station_Number,
        Latitude=row.Latitude,
        Longitude=row.Longitude,
        Distance_From_Bangladesh_Meters=row.Distance_From_Bangladesh_Meters,
    )

    sample_location_table.append(sample_location)

print(sample_location_table[0])

# Using Index
expected_columns = ['GEMS_Station_Number','Latitude', 'Longitude','Distance_From_Bangladesh_Meters']
indices_to_keep = [WaterSample._fields.index(column) for column in expected_columns]

new_field_names = [headers[i] for i in indices_to_keep]

SampleLocation: namedtuple = namedtuple(
    typename='SampleLocation',
    field_names=new_field_names
)

sample_location_table:List[SampleLocation] = []
for row in water_sample_table:

    new_rows = [row[i] for i in indices_to_keep]
    sample_location:SampleLocation = SampleLocation(*new_rows)

    sample_location_table.append(sample_location)

print(sample_location_table[0])