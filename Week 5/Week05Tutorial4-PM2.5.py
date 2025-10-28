import datetime
from pathlib import Path
import csv
import statistics

csv_path = Path(r'/Users/macbookairfromboeing/Downloads/Penn/Courses/2025 Fall/ENVS 5726/Week 05 - Summarizations/Week05TutorialData/CDC_Philadelphia_2019_PM25.csv')

month_by_mean_pm25_dict = {}

with open(csv_path, 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)

    # Creating the Summarization Dict
    for row in reader:
        year, date_string, statefips, countyfips, ctfips, lat, longti, mean_pm25,stdev_pm25 = row

        date = datetime.datetime.strptime(date_string, '%d%b%Y')
        month = date.strftime('%B')

        if month not in month_by_mean_pm25_dict:
            month_by_mean_pm25_dict[month] = [float(mean_pm25)]
        else:
            month_by_mean_pm25_dict[month].append(float(mean_pm25))

# Exporting the Summarization into a Table
summary_headers = ['Month', 'Mean PM2.5 (ug/m3)']
summary_table = []

for month in month_by_mean_pm25_dict:
    mean_pm25_list = month_by_mean_pm25_dict[month]
    monthly_mean_pm25 = statistics.mean(mean_pm25_list)
    summary_table.append([month, monthly_mean_pm25])

output_path = Path(r'/Users/macbookairfromboeing/Downloads/Penn/Courses/2025 Fall/ENVS 5726/Week 05 - Summarizations/Week05TutorialData/CDC_PHL_Summary.csv')
