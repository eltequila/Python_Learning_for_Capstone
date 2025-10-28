import csv
from pathlib import Path
import json


# Task 1
json_path = Path(r'/Users/macbookairfromboeing/Downloads/Penn/Courses/2025 Fall/ENVS 5726/Week 05 - Summarizations/Week05AssignmentData/Trase_CIV_Cocoa_SupplyChain_Data.json')

with open(json_path) as json_file:
    data = json.load(json_file)

data_headers = ['trader_group', 'country_of_destination', 'cocoa_deforestation_15_years_total_exposure', 'cocoa_net_emissions_15_years_total']
data_table = []

cocoas = data['cote_divoire_cocoa_v1_1_1']['data']

for record in cocoas:
    trader_group = record['supply_chain_data']['trader_group']
    country_of_destination = record['supply_chain_data']['country_of_destination']
    cocoa_deforestation_15_years_total_exposure = record['cocoa_data']['cocoa_deforestation_15_years_total_exposure']
    cocoa_net_emissions_15_years_total = record['cocoa_data']['cocoa_net_emissions_15_years_total']
    data_table.append([trader_group, country_of_destination, cocoa_deforestation_15_years_total_exposure, cocoa_net_emissions_15_years_total])

print(data_headers)
for row in data_table[:10]:
    print(row)

output_path = Path(r'/Users/macbookairfromboeing/Downloads/Penn/Courses/2025 Fall/ENVS 5726/Week 05 - Summarizations/Week05AssignmentData/task1_cocoa_data.csv')

with open(output_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows([data_headers]+data_table)



# Task 2 -- Summary Dictionary for trader_group
task1_csv_path = Path(r'/Users/macbookairfromboeing/Downloads/Penn/Courses/2025 Fall/ENVS 5726/Week 05 - Summarizations/Week05AssignmentData/task1_cocoa_data.csv')

summary_trader_group_dict = {}


with open(task1_csv_path) as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)

    # Creating the Summarization Dict
    for row in reader:
        trader_group, country_of_destination, cocoa_deforestation_15_years_total_exposure, cocoa_net_emissions_15_years_total = row

        deforestation_float = float(cocoa_deforestation_15_years_total_exposure)
        new_emission_float = float(cocoa_net_emissions_15_years_total)

        if trader_group not in summary_trader_group_dict:
            summary_trader_group_dict[trader_group] = {
                'cocoa_deforestation_list':[deforestation_float],
                'cocoa_net_emission_list':[new_emission_float]
            }
        else:
            summary_trader_group_dict[trader_group]['cocoa_deforestation_list'].append(deforestation_float)
            summary_trader_group_dict[trader_group]['cocoa_net_emission_list'].append(new_emission_float)



export_path_json1 = Path(r'/Users/macbookairfromboeing/Downloads/Penn/Courses/2025 Fall/ENVS 5726/Week 05 - Summarizations/Week05AssignmentData/task2_trade_group.json')

with open(export_path_json1, 'w') as json_file:
    json.dump(summary_trader_group_dict, json_file)


# Task 2 -- Summary Dictionary for country_of_destination

summary_destination_dict = {}

with open(task1_csv_path) as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)

    # Creating the Summarization Dict
    for row in reader:
        trader_group, country_of_destination, cocoa_deforestation_15_years_total_exposure, cocoa_net_emissions_15_years_total = row

        deforestation_float = float(cocoa_deforestation_15_years_total_exposure)
        new_emission_float = float(cocoa_net_emissions_15_years_total)

        if country_of_destination not in summary_destination_dict:
            summary_destination_dict[country_of_destination] = {
                'cocoa_deforestation_list': [deforestation_float],
                'cocoa_net_emission_list': [new_emission_float]
            }
        else:
            summary_destination_dict[country_of_destination]['cocoa_deforestation_list'].append(deforestation_float)
            summary_destination_dict[country_of_destination]['cocoa_net_emission_list'].append(new_emission_float)

export_path_json2 = Path(r'/Users/macbookairfromboeing/Downloads/Penn/Courses/2025 Fall/ENVS 5726/Week 05 - Summarizations/Week05AssignmentData/task2_destination.json')

with open(export_path_json2, 'w') as json_file_2:
    json.dump(summary_destination_dict, json_file_2)


# Task 3 Four Summarizations (Example)
task1_csv_path = Path(r'/Users/macbookairfromboeing/Downloads/Penn/Courses/2025 Fall/ENVS 5726/Week 05 - Summarizations/Week05AssignmentData/task1_cocoa_data.csv')

trader_group_deforestation_value_dict_no1 = {}

with open(task1_csv_path) as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)

    for row in reader:
        trader_group, country_of_destination, cocoa_deforestation_15_years_total_exposure, cocoa_net_emissions_15_years_total = row

        deforestation_float = float(row[header.index('cocoa_deforestation_15_years_total_exposure')])

        if trader_group not in trader_group_deforestation_value_dict_no1:
            trader_group_deforestation_value_dict_no1[trader_group] = [deforestation_float]
        else:
            trader_group_deforestation_value_dict_no1[trader_group].append(deforestation_float)


no1_summary_headers = ['trader_group','total_cocoa_deforestation']
trader_group_deforestation_summary_table = []

for group in trader_group_deforestation_value_dict_no1:
    deforestation_value_list = trader_group_deforestation_value_dict_no1[group]
    deforestation_value_sum = sum(deforestation_value_list)
    trader_group_deforestation_summary_table.append([group, deforestation_value_sum])


all_sums = [row[1] for row in trader_group_deforestation_summary_table]
max_sum = max(all_sums)

filtered_trader_group_deforestation_summary_table = [row for row in trader_group_deforestation_summary_table
                                                     if row[1] > max_sum*0.1]

output_path_tg_deforestation = Path(r"/Users/macbookairfromboeing/Downloads/Penn/Courses/2025 Fall/ENVS 5726/Week 05 - Summarizations/Week05AssignmentData/TG_Deforestation.csv")

with open(output_path_tg_deforestation, 'w', newline='', encoding='utf-8') as output_file:
    writer = csv.writer(output_file)
    writer.writerows([no1_summary_headers] + filtered_trader_group_deforestation_summary_table)


# Generalized Function
def task3_summarization_func(column_name:str, value_list_name:str, targeted_output_path):

    function_csv_path = Path(
        r'/Users/macbookairfromboeing/Downloads/Penn/Courses/2025 Fall/ENVS 5726/Week 05 - Summarizations/Week05AssignmentData/task1_cocoa_data.csv')

    targeted_dict = {}

    with open(function_csv_path) as function_csv:
        function_csv_reader = csv.reader(function_csv)
        function_csv_header = next(function_csv_reader)

        for row in function_csv_reader:
            trader_group, country_of_destination, cocoa_deforestation_15_years_total_exposure, cocoa_net_emissions_15_years_total = row

            targeted_column = row[function_csv_header.index(column_name)]
            value = float(row[function_csv_header.index(value_list_name)])

            if targeted_column not in targeted_dict:
                targeted_dict[targeted_column] = [value]
            else:
                targeted_dict[targeted_column].append(value)


    targeted_summary_table_headers = [f'{column_name}',f'{value_list_name}']
    targeted_summary_table = []

    for targeted_column in targeted_dict:
        value_list = targeted_dict[targeted_column]
        value_sum = sum(value_list)
        targeted_summary_table.append([targeted_column, value_sum])

    all_sum = [row[1] for row in targeted_summary_table]
    max_sum = max(all_sum)

    filtered_targeted_summary_table = [row for row in targeted_summary_table if row[1] > max_sum*0.1]


    targeted_output_path = Path(targeted_output_path)

    with open(targeted_output_path, 'w', newline='', encoding='utf-8') as output_file:
        writer = csv.writer(output_file)
        writer.writerows([targeted_summary_table_headers] + filtered_targeted_summary_table)

# Trader_Group vs. Net Emissions
task3_summarization_func('trader_group', 'cocoa_net_emissions_15_years_total',
                         '/Users/macbookairfromboeing/Downloads/Penn/Courses/2025 Fall/ENVS 5726/Week 05 - Summarizations/Week05AssignmentData/TG_Emissions.csv')

# Destination vs. Deforestation
task3_summarization_func('country_of_destination', 'cocoa_deforestation_15_years_total_exposure',
                         '/Users/macbookairfromboeing/Downloads/Penn/Courses/2025 Fall/ENVS 5726/Week 05 - Summarizations/Week05AssignmentData/DES_Deforestation.csv')

# Destination vs. Net Emissions
task3_summarization_func('country_of_destination', 'cocoa_net_emissions_15_years_total',
                         '/Users/macbookairfromboeing/Downloads/Penn/Courses/2025 Fall/ENVS 5726/Week 05 - Summarizations/Week05AssignmentData/DES_Emissions.csv')