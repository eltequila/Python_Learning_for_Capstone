import csv
from collections import namedtuple
from pathlib import Path
import datetime



# Task 2
csv_path = Path(r'/Users/macbookairfromboeing/Downloads/Penn/Courses/2025 Fall/ENVS 5726/Week 09 - Updated Version/Week09AssignmentData/Water_Mains.csv')


with open(csv_path, 'r', encoding='utf-8-sig') as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader)

    WaterMain = namedtuple(typename='WaterMain', field_names=headers)

    water_main_table = []

    for row in reader:
        water_main = WaterMain(*row)
        water_main_table.append(water_main)

NewWaterMain = namedtuple(
    typename='NewWaterMain',
    field_names=list(WaterMain._fields) + ['Age'] + ['Survival_Probability']
)

water_main_table_with_age_probability = []
for row in water_main_table:

    install_date = row.InstallDate
    cleaned_install_date = datetime.datetime.strptime(install_date, '%m/%d/%Y %H:%M')

    age = 2025-cleaned_install_date.year

    # Calculating survival_probability
    material = row.Material
    coefficients = material_coefficients[material]
    c, b, a = coefficients
    survival_probability = cumulative_density_function(age, c, b, a)

    new_row = NewWaterMain(
        *row,
        Age = age,
        Survival_Probability = survival_probability
    )

    water_main_table_with_age_probability.append(new_row)

print(water_main_table_with_age_probability[:2])

