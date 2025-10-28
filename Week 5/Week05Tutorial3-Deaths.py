from pathlib import Path
import csv

csv_path = Path(r'/Users/macbookairfromboeing/Downloads/Penn/Courses/2025 Fall/ENVS 5726/Week 05 - Summarizations/Week05TutorialData/EMDAT_Haiti_Disaster_Deaths_By_Year.csv')

disastertype_by_totaldeaths_dict = {}

with open(csv_path, 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)

    # Creating the Summarization Dict
    for row in reader:
        country, year, subgroup, disaster_type, total_deaths, injured_count, total_affected = row

        if not total_deaths:
            total_deaths = 0
        else:
            total_deaths = int(total_deaths.replace(',', ''))

        if disaster_type not in disastertype_by_totaldeaths_dict:
            disastertype_by_totaldeaths_dict[disaster_type] = [total_deaths]
        else:
            disastertype_by_totaldeaths_dict[disaster_type].append(total_deaths)


# Exporting the Summarization into a Table
summary_headers = ['Disaster Type', 'Total Death']
summary_table = []
for disaster_type in disastertype_by_totaldeaths_dict:
    deaths_by_disaster_list = disastertype_by_totaldeaths_dict[disaster_type]
    total_deaths_for_type = sum(deaths_by_disaster_list)

    summary_table.append([disaster_type, total_deaths_for_type])

output_path = Path(r'/Users/macbookairfromboeing/Downloads/Penn/Courses/2025 Fall/ENVS 5726/Week 05 - Summarizations/Week05TutorialData/EMDAT_Haiti_Disaster_Summary.csv')
with open(output_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows([summary_headers] + summary_table)