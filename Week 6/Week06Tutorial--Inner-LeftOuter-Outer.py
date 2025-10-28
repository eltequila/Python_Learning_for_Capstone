# Join Setup

target_headers = ['TRACT', 'POPULATION']
target_table = [
    [30101, 2646],
    [30103, 2375],
    [30104, 3424],
    [30200, 5346],
    [30300, 4428],
    [30400, 5543]
]

join_headers = ['TRACT', 'RISK_SCORE', 'RISK_RATING']
join_table = [
    [30101, 17.5, 'Very Low'],
    [30103, 5.1, 'Very Low'],
    [30104, 28.1, 'Relatively Low'],
    [30200, 54.7, 'Relatively Low'],
    [30700, 59.7, 'Relatively Low'],
    [30801, 22.6, 'Very Low']
]


unique_id_name = 'TRACT'

target_id_set = set(row[target_headers.index(unique_id_name)] for row in target_table)
join_id_set = set([row[join_headers.index(unique_id_name)] for row in join_table])

print(target_id_set.intersection(join_id_set))


# Implementing Inner Join
join_dict = {}
for row in join_table:

    unique_id = row[join_headers.index(unique_id_name)]

    join_dict[unique_id] = row

# Inner Join
joined_headers = target_headers + join_headers
inner_joined_table = []

for target_row in target_table:

    unique_id = target_row[target_headers.index(unique_id_name)]

    if unique_id in join_dict:

        join_row = join_dict[unique_id]
        inner_joined_table.append(target_row + join_row)

print(joined_headers)
for row in inner_joined_table:
    print(row)

print('\n')


# Implementing Left Outer Join
# Perform Inner Join FIRST
joined_headers = target_headers + join_headers
left_joined_table = []

for target_row in target_table:

    unique_id = target_row[target_headers.index(unique_id_name)]

    if unique_id in join_dict:
        join_row = join_dict[unique_id]

    else:
        join_row = [None] * len(join_headers)

    left_joined_table.append(target_row + join_row)

print(joined_headers)
for row in left_joined_table:
    print(row)

print('\n')



# Implementing Full Outer Join
# Step 1 -- Left Outer Join
joined_headers = target_headers + join_headers
outer_joined_table = []

for target_row in target_table:
    unique_id = target_row[target_headers.index(unique_id_name)]

    if unique_id in join_dict:
        join_row = join_dict[unique_id]

    else:
        join_row = [None] * len(join_headers)

    outer_joined_table.append(target_row + join_row)

# Step 2 -- Iterate every row in the Join Dict and
#           IF the unique ID is not in the Target Table, then append it to the Joined Table with a NULL Target Row.
target_id_set = set(row[target_headers.index(unique_id_name)] for row in target_table)

for unique_id in join_dict:

    if unique_id not in target_id_set:

        join_row = join_dict[unique_id]

        target_row = [None] * len(target_headers)
        outer_joined_table.append(target_row + join_row)
