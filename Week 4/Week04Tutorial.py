import datetime

date_string_list = ['March 8, 2000', 'May 2, 2012', 'August 23, 2023']
date_list = []

for date_string in date_string_list:
    date = datetime.datetime.strptime(date_string, '%B %d, %Y')
    date_list.append(date)

print(date_list)




from pathlib import Path

file_path_string = r'/Users/macbookairfromboeing/Downloads/Penn/Capstone/Sample Data'

emissions_file_path = Path('/Users/macbookairfromboeing/Downloads/Penn/Capstone/Sample Data')
print(emissions_file_path.exists())

new_folder_path = Path('/Users/macbookairfromboeing/Downloads/Penn/Capstone/NewFOlder/F')

new_folder_path.mkdir(parents=True, exist_ok=True)

print(new_folder_path.exists())



from pathlib import Path
import csv

csv_path = (r'/Users/macbookairfromboeing/Downloads/Penn/Courses/2025 Fall/ENVS 5726/Week 04 - Iteration/Week04TutorialData/Haiti_Earthquake_Damage_Assessment.csv')
haiti_earthquake_table = []

with open(csv_path, encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file)

    headers = next(reader)

    for row in reader:
        haiti_earthquake_table.append(row)

print('These are headers:')
print(headers)
print('These are rows:')
for row in haiti_earthquake_table:
    print(row)



