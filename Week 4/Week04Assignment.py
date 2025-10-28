# Task 1
from email import header
from pathlib import Path

path_sec_sdgar_10k = Path(r'/Users/macbookairfromboeing/Downloads/Penn/Courses/2025 Fall/ENVS 5726/Week 04 - Iteration/Week04AssignmentData/SEC_EDGAR_10K')
headers = ['Company Name', 'Year', 'Count Sustainability', 'Count AI']

table_sec_sdgar_10k = []

for path_sec_sdgar_10k in path_sec_sdgar_10k.glob('*'):

    raw_company_name = path_sec_sdgar_10k.stem
    cleaned_company_name = raw_company_name.split('-')[0]
    updated_company_name = cleaned_company_name.replace(
        'msft', 'Microsoft'
    ).replace(
        'amzn', 'Amazon'
    ).replace(
        'nvda','NVIDIA'
    ).replace(
        'goog','Google'
    )

    year_str = str(raw_company_name[-8:-4])


    with open(path_sec_sdgar_10k, 'r', encoding='utf-8-sig', errors = 'replace') as file_iterations:
        uppercase_files = file_iterations.read().upper()
        sustainability_count = uppercase_files.count('SUSTAINABILITY')
        ai_count = uppercase_files.count('ARTIFICIAL INTELLIGENCE')

    table_sec_sdgar_10k.append([updated_company_name, year_str, sustainability_count, ai_count])

print(headers)
for row in table_sec_sdgar_10k[:10]:
    print(row)


# Task 2
import statistics

def get_average_by_company(header, table, column_name_to_average, company_name):

    values_list = []

    for row in table:
        if row[headers.index('Company Name')] == company_name:
            values_list.append(row[header.index(column_name_to_average)])

    average_values = statistics.mean(values_list)
    return average_values


for company_name in ['NVIDIA','Microsoft','Amazon','Google']:
    for column_name_to_average in ['Count Sustainability','Count AI']:
        column_average = get_average_by_company(header = headers, table = table_sec_sdgar_10k, column_name_to_average = column_name_to_average, company_name = company_name)
        print(f'The average {column_name_to_average} for {company_name} is {column_average}.')



# Task 3

import csv

export_company_name = ['NVIDIA','Microsoft','Amazon','Google']

export_path = Path(r'/Users/macbookairfromboeing/Downloads/Penn/Courses/2025 Fall/ENVS 5726/Week 04 - Iteration/10K_Report')
export_path.mkdir(exist_ok = True)

for company in export_company_name:

    company_table = [row for row in table_sec_sdgar_10k if row[headers.index('Company Name')] == company]

    file_name = f'SEC_10K_{company}.csv'
    file_path = export_path / file_name

    with open(file_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(company_table)


# total_table_10k_amazon = [headers] + [row for row in table_sec_sdgar_10k if row[headers.index('Company Name')] == 'Amazon']
# total_table_10k_google = [headers] + [row for row in table_sec_sdgar_10k if row[headers.index('Company Name')] == 'Google']
# total_table_10k_nvidia = [headers] + [row for row in table_sec_sdgar_10k if row[headers.index('Company Name')] == 'NVIDIA']
# total_table_10k_microsoft = [headers] + [row for row in table_sec_sdgar_10k if row[headers.index('Company Name')] == 'Microsoft']
#
#
# path_total_table_10k_amazon = Path(r'/Users/macbookairfromboeing/Downloads/Penn/Courses/2025 Fall/ENVS 5726/Week 04 - Iteration/10k/SEC_10K_Amazon_Metrics.csv')
# with open(path_total_table_10k_amazon, 'w', newline='', encoding='utf-8') as f:
#     writer = csv.writer(f)
#     writer.writerows(total_table_10k_amazon)
#
# path_total_table_10k_google = Path(r'/Users/macbookairfromboeing/Downloads/Penn/Courses/2025 Fall/ENVS 5726/Week 04 - Iteration/10k/SEC_10K_Google_Metrics.csv')
# with open(path_total_table_10k_google, 'w', newline='', encoding='utf-8') as f:
#     writer = csv.writer(f)
#     writer.writerows(total_table_10k_google)
#
# path_total_table_10k_nvidia = Path(r'/Users/macbookairfromboeing/Downloads/Penn/Courses/2025 Fall/ENVS 5726/Week 04 - Iteration/10k/SEC_10K_NVIDIA_Metrics.csv')
# with open(path_total_table_10k_nvidia, 'w', newline='', encoding='utf-8') as f:
#     writer = csv.writer(f)
#     writer.writerows(total_table_10k_nvidia)
#
# path_total_table_10k_microsoft = Path(r'/Users/macbookairfromboeing/Downloads/Penn/Courses/2025 Fall/ENVS 5726/Week 04 - Iteration/10k/SEC_10K_Microsoft_Metrics.csv')
# with open(path_total_table_10k_microsoft, 'w', newline='', encoding='utf-8') as f:
#     writer = csv.writer(f)
#     writer.writerows(total_table_10k_microsoft)


