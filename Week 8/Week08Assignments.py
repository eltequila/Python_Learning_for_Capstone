from typing import NamedTuple, List, Any, Dict
from pathlib import Path
from collections import namedtuple
import csv

csv_path: Path = Path(r'/Users/macbookairfromboeing/Downloads/Penn/Courses/2025 Fall/ENVS 5726/Week 08 - Object-Oriented Data Analysis/Week08AssignmentData/'
                      r'IOM_Rohingya_WASH_Survey.csv')



# Task 1

survey_table_t1: List[tuple] = []

with open(csv_path, 'r', encoding='utf-8-sig') as csvfile:
    reader:csv.reader = csv.reader(csvfile)
    headers: List[str] = next(reader)

    target_headers:List[str] = [header for header in headers if header.startswith('G')]

    SurveyTable = namedtuple(typename='SurveyTable', field_names=target_headers)

    for row in reader:
        target_rows = [row[headers.index(header)] for header in target_headers]
        survey_table = SurveyTable(*target_rows)
        survey_table_t1.append(survey_table)

print(survey_table_t1[0])



# Task 2
from W8_A_T2_lib import convert_yesno_to_binary
binary_survey_table_t2 = convert_yesno_to_binary(survey_table_t1)
print(binary_survey_table_t2[0])


# Task 3
from W8_A_T2_lib import get_categories
print(get_categories(table=binary_survey_table_t2,category_column='G1_1'))
print(get_categories(table=binary_survey_table_t2,category_column='G4_1'))
print(get_categories(table=binary_survey_table_t2,category_column='G5_1'))
print(get_categories(table=binary_survey_table_t2,category_column='G10_1'))
print(get_categories(table=binary_survey_table_t2,category_column='G15_1'))



# Task 4
G1_1_map = {
    'Storage Tanks tap / tap stand': 1,
    'Tube wells / handpump': 2,
    'Piped water tap / tap stand': 3,
    'No water accessible': 4,
    'Surface water pond, stream, etc.': 5,
    'Unprotected Well': 6
}

# Adding G2_11_map according to the result from Task 5
G2_11_map = {
    'Sometimes tubewell are damaged.':1,
    'We need more deep tubewell.': 2,
    'Water source is at the bottom of hill':3
}

# Adding G3_10_map according to the result from Task 5
G3_10_map = {
    'Reduces wastage':1
}

G4_1_map = {
    'Most girls and women bathe in communal/public bathing facilities':1,
    'Most girls and women shower outdoors or in open areas':2,
    'Most girls and women bathe in private bathing facilities in their shelters':3
}

G5_1_map = {
    'Most boys and men bathe in private bathing facilities in their shelters':1,
    'Most boys and men shower outdoors or in open areas':2,
    'Most boys and men bathe in communal/public bathing facilities':3
}

G10_1_map = {
    'Most people defecate in plastic bags':1,
    'Most people defecate in communal latrines':2,
    'Most people defecate outdoors or in open areas':3,
    'Most people defecate in clustered family latrines':4,
    'Most people defecate in household latrines':5
}

G15_1_map = {
    'Most people in this location use household bins to dispose of rubbish':1,
    'Most people in this location use open/discriminate dumping to dispose of rubbish':2,
    'Most people in this location use a communal dumping site to dispose of rubbish':3
}

num_survey_table = []

for survey in binary_survey_table_t2:

    updated_survey = survey

    if updated_survey.G1_1 in G1_1_map:
        updated_survey = updated_survey. _replace(G1_1=G1_1_map[updated_survey.G1_1])

    if updated_survey.G2_11 in G2_11_map:
        updated_survey = updated_survey. _replace(G2_11=G2_11_map[updated_survey.G2_11])

    if updated_survey.G3_10 in G3_10_map:
        updated_survey = updated_survey._replace(G3_10=G3_10_map[updated_survey.G3_10])

    if updated_survey.G4_1 in G4_1_map:
        updated_survey = updated_survey. _replace(G4_1=G4_1_map[updated_survey.G4_1])

    if updated_survey.G5_1 in G5_1_map:
        updated_survey = updated_survey. _replace(G5_1=G5_1_map[updated_survey.G5_1])

    if updated_survey.G10_1 in G10_1_map:
        updated_survey = updated_survey. _replace(G10_1=G10_1_map[updated_survey.G10_1])

    if updated_survey.G15_1 in G15_1_map:
        updated_survey = updated_survey. _replace(G15_1=G15_1_map[updated_survey.G15_1])

    num_survey_table.append(updated_survey)

print(num_survey_table[0])



# Task 5
from W8_A_T2_lib import get_non_numeric_values
error_list = get_non_numeric_values(table=num_survey_table)
print(error_list)



# Task 6
# from factor_analyzer import FactorAnalyzer
# fa = FactorAnalyzer(rotation='varimax')
# data = num_survey_table
# fa.fit(data)



# Task 7
import pandas as pd
import numpy as np
from W8_A_T2_lib import _findCorrelation_fast
from W8_A_T2_lib import _findCorrelation_exact

df = pd.DataFrame.from_records(
    data = num_survey_table,
    columns = num_survey_table[0]._fields
)

print(df)

corr_matrix = df.corr()
print(corr_matrix)

constant_columns = [col for col in df.columns if df[col].nunique() == 1]
df_no_constants = df.drop(columns=constant_columns)
print(df_no_constants)

corr_matrix = df_no_constants.corr()
print(corr_matrix)


# Codes from Assignment 8 Task 8
from factor_analyzer import FactorAnalyzer

data = df_no_constants

# Create factor analysis object and perform factor analysis
fa = FactorAnalyzer(rotation='varimax')
fa.fit(data)

# Perform factor analysis with the determined number of factors
number_of_factors = 5
fa = FactorAnalyzer(n_factors=number_of_factors,rotation='varimax')
fa.fit(data)

factor_names = [f'Factor{i+1}' for i in range(number_of_factors)]

loadings_df = pd.DataFrame(fa.loadings_, columns=factor_names, index=[data.columns])

# Get variance of each factor
index_names = ['Sum of Squared Loadings','Proportional Variance','Cumulative Variance']
variance_df = pd.DataFrame(fa.get_factor_variance(),columns = factor_names, index=index_names)

loadings_df.to_csv('/Users/macbookairfromboeing/Downloads/Penn/Courses/2025 Fall/ENVS 5726/Week 08 - Object-Oriented Data Analysis/Week08AssignmentData/IOM_Rohingya_WASH_Loadings.csv')
variance_df.to_csv('/Users/macbookairfromboeing/Downloads/Penn/Courses/2025 Fall/ENVS 5726/Week 08 - Object-Oriented Data Analysis/Week08AssignmentData/IOM_Rohingya_WASH_Loadings.csv')