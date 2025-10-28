from pathlib import Path
import csv
from pprint import pprint

# Task 1
socvul_path = Path(r'/Users/macbookairfromboeing/Downloads/Penn/Courses/2025 Fall/ENVS 5726/Week 06 - Joins/Week06AssignmentData/EJScreen_BlockGroup_SocialVulnerability.csv')
with open(socvul_path, 'r', encoding='utf-8') as SocialVulnerabilityFile:
    reader = csv.reader(SocialVulnerabilityFile)
    social_vul_headers = next(reader)
    social_vul_table = list(reader)

# print(social_vul_headers)
# for row in social_vul_table[:2]：
#     print(row)


haz_path = Path(r'/Users/macbookairfromboeing/Downloads/Penn/Courses/2025 Fall/ENVS 5726/Week 06 - Joins/Week06AssignmentData/EJSCREEN_BlockGroup_Hazards.csv')
with open(haz_path, 'r', encoding='utf-8') as HazFile:
    reader = csv.reader(HazFile)
    haz_headers = next(reader)
    haz_table = list(reader)

# print(haz_headers)
# for row in haz_table[:2]:
#     print(row)

left_id_name = 'ID_SOCVUL'
right_id_name = 'ID_HAZ'

target_id_set = set([row[social_vul_headers.index(left_id_name)] for row in social_vul_table])
join_id_set = set([row[haz_headers.index(right_id_name)] for row in haz_table])

# print(target_id_set.intersection(join_id_set))

# Step 1: Implementing Inner Join
join_dict = {}
for row in haz_table:
    join_id = row[haz_headers.index(right_id_name)]
    join_dict[join_id] = row

joined_headers = social_vul_headers + haz_headers
joined_table = []

for target_row in social_vul_table:
    target_id = target_row[social_vul_headers.index(left_id_name)]

    if target_id in join_dict:

        join_row = join_dict[target_id]

# Step 2: Left Outer Join
    else:
        join_row = [None] * len(haz_headers)

    joined_table.append(target_row + join_row)

# Step 3: Iterate every row in the Join Dict and
#           IF the unique ID is not in the Target Table, then append it to the Joined Table with a NULL Target Row.
target_id_set = set([row[social_vul_headers.index(left_id_name)] for row in social_vul_table])
for join_id in join_dict:

    if join_id not in target_id_set:

        join_row = join_dict[join_id]

        target_row = [None] * len(social_vul_headers)
        joined_table.append(target_row + join_row)

joined_table_export_path = Path(r'/Users/macbookairfromboeing/Downloads/Penn/Courses/2025 Fall/ENVS 5726/Week 06 - Joins/Week06AssignmentData/task_1_joined_table_socvul_haz.csv')
with open(joined_table_export_path, 'w', newline='', encoding='utf-8') as JoinedFile:
    writer = csv.writer(JoinedFile)
    writer.writerows([joined_headers]+joined_table)



# Task 2
total_rows = len(joined_table)

valid_socvul_table = [row for row in joined_table if row[joined_headers.index(left_id_name)]]
valid_socvul_only_rows = len(valid_socvul_table)

valid_haz_table = [row for row in joined_table if row[joined_headers.index(right_id_name)]]
valid_haz_only_rows = len(valid_haz_table)

print(f'There are {valid_socvul_only_rows} valid ID_SOCVUL out of {total_rows} total joined rows.')
print(f'There are {valid_haz_only_rows} valid ID_HAZ out of {total_rows} total joined rows.')
print('\n')


# Task 3
valid_inner_join_only_table = [row for row in joined_table if row[joined_headers.index(left_id_name)] and
                               row[joined_headers.index(right_id_name)]]
valid_inner_join_only_rows = len(valid_inner_join_only_table)
print(f'There are {valid_inner_join_only_rows} inner joined rows of {total_rows} total Block Groups.')


# Task 4
inner_join_only_table_output_path = Path(r'/Users/macbookairfromboeing/Downloads/Penn/Courses/2025 Fall/ENVS 5726/Week 06 - Joins/Week06AssignmentData/task_4_inner_join_table.csv')
with open(inner_join_only_table_output_path, 'w', newline='', encoding='utf-8') as InnerJoinFile:
    writer = csv.writer(InnerJoinFile)
    writer.writerows([joined_headers] + valid_inner_join_only_table)