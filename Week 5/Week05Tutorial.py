my_string = 'aaabbaacddd'

count_dict = {}

for char in my_string:

    if char not in count_dict:
        count_dict[char] = 1

    else:
        count_dict[char] += 1

print(count_dict)



from pathlib import Path
import csv

csv_path = Path(r'/Users/macbookairfromboeing/Downloads/Penn/Courses/2025 Fall/ENVS 5726/Week 05 - Summarizations/Week05TutorialData/FPC_PHS_Trees_By_Mature_Height.csv')

genus_by_heights_dict = {}

with open(csv_path, 'r', encoding='utf-8') as csvfile:

    reader = csv.reader(csvfile)
    tree_headers = next(reader)
    for row in reader:
        genus, species, height_ft = row

        if genus not in genus_by_heights_dict:
            genus_by_heights_dict[genus] = [int(height_ft)]
        else:
            genus_by_heights_dict[genus].append(int(height_ft))

print(genus_by_heights_dict['Acer'])

genus_by_species_count = {}

for genus in genus_by_heights_dict:

    genus_by_species_count[genus] = len(genus_by_heights_dict[genus])

print(genus_by_species_count)


import statistics
genus_by_mean_height_dict = {genus:statistics.mean(genus_by_heights_dict[genus])
                             for genus in genus_by_heights_dict}
print(genus_by_mean_height_dict)

summary_table_headers = ['Genus','Species Count','Min Height(ft)','Max height(ft)','Mean height(ft)']
summary_table = []
for genus in genus_by_heights_dict:
    heights_list = genus_by_heights_dict[genus]

    species_count = len(heights_list)
    min_height = min(heights_list)
    max_height = max(heights_list)
    mean_height = statistics.mean(heights_list)

    summary_table.append([genus, species_count, min_height, max_height, mean_height])

summarized_table_path = Path(r'/Users/macbookairfromboeing/Downloads/Penn/Courses/2025 Fall/ENVS 5726/Week 05 - Summarizations/Week05TutorialData/FPC_PHS_Tree_Genus_Summary.csv')

with open(summarized_table_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows([summary_table_headers] + summary_table)

