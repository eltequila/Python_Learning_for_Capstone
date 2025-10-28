from typing import List, Type
from collections import namedtuple

water_sample_headers: List[str] = ['GEMS_Station_Number', 'Water_Type', 'Value', 'Analyte', 'Units']

WaterSample:Type[tuple] = namedtuple(typename='WaterSample', field_names=water_sample_headers)

water_sample_table: List[tuple] = [
    WaterSample(
        GEMS_Station_Number='IND02375',
        Water_Type='River station',
        Value='1.63',
        Analyte='N03N',
        Units='mg/L'
    ),
    WaterSample(
        GEMS_Station_Number='IND00940',
        Water_Type='River station',
        Value='0.43',
        Analyte='N03N',
        Units='mg/L'
    )
]

sample_location_headers = ['GEMS_Station_Number','Latitude','Longitude']

SampleLocation: Type[tuple] = namedtuple(typename='SampleLocation', field_names=sample_location_headers)

sample_location_table: List[tuple] = [
    SampleLocation(
        GEMS_Station_Number='IND02375',
        Latitude='51.23450',
        Longitude='-78.23450',
    ),
    SampleLocation(
        GEMS_Station_Number='IND00940',
        Latitude='46.45965',
        Longitude='-66.24853',
    )
]


import sys
sys.path.insert(1,r'/Users/macbookairfromboeing/Python_Learning_for_Capstone/Week 8')


from datalib_T2 import filter_equals
from datalib_T2 import filter_null
from datalib_T2 import summarize
from datalib_T2 import join

filter_equals(table=water_sample_table,column_name='Water_Type',value='River Station')
filter_null(table=water_sample_table,column_name_list=['value','Date_Station_Opened','Distance_From_Bangladesh_Meters'])
summarize(table=water_sample_table, column_name='Value', summary_method='MEAN')
join(target_table=water_sample_table, join_table=sample_location_table, join_column_name='GEMS_Station_Number')



