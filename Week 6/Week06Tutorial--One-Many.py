target_headers = ['COUNTYFIPS', 'POPULATION']
target_table = [
    [1, 103797],
    [39, 83927],
    [43, 286115]
]

join_headers = ['COUNTYFIPS', 'TRACT', 'RISK_RATING']
join_table = [
    [1, 30101, 'Very Low'],
    [1, 30104, 'Relatively Low'],
    [39, 111300, 'Relatively Moderate'],
    [39, 111600, 'Relatively High'],
    [43, 21100, 'Very High']
]

join_id_name = 'COUNTYFIPS'


one_to_one_join_dict = {}
for row in join_table:
    join_id = row[join_headers.index(join_id_name)]
    one_to_one_join_dict[join_id] = row

joined_headers = target_headers + join_headers
one_to_one_joined_table = []
for target_row in target_table:
    join_id = target_row[joined_headers.index(join_id_name)]
    if join_id in one_to_one_join_dict:
        join_row = one_to_one_join_dict[join_id]
        one_to_one_joined_table.append(target_row + join_row)

from pprint import pprint
pprint(one_to_one_join_dict, width=60)

print(joined_headers)
for row in one_to_one_joined_table:
    print(row)


# One_to_Many Join
one_to_many_join_dict = {}
for row in join_table:
    join_id = row[joined_headers.index(join_id_name)]

    if join_id not in one_to_many_join_dict:
        one_to_many_join_dict[join_id] = [row]

    else:
        one_to_many_join_dict[join_id].append(row)

joined_headers = target_headers + join_headers
one_to_many_joined_table = []
for target_row in target_table:

    join_id = target_row[joined_headers.index(join_id_name)]

    if join_id in one_to_many_join_dict:

        for join_row in one_to_many_join_dict[join_id]:
            one_to_many_joined_table.append(target_row + join_row)

print(joined_headers)
for row in one_to_many_joined_table:
    print(row)