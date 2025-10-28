# Task 1

def is_main_ratio_toilets_to_people_met(ratio_string):

    parts = ratio_string.split('/')
    toilet_num = int(parts[0].replace("t",""))
    people_num = int(parts[1].replace("p",""))
    toilet_ratio = toilet_num / people_num

    if toilet_ratio >= 1/20:
        return True

    else:
        return False

print(is_main_ratio_toilets_to_people_met('1t/37p'))
print(is_main_ratio_toilets_to_people_met('1t/12p'))



# Task 2

def is_population_disabled(disabled : int, total_population : int):

    disabled_ratio = disabled / total_population

    if disabled_ratio < 1/10:
        return False
    else:
        return True

print(is_population_disabled(0, 32))
print(is_population_disabled(52, 392))



# Task 3

def is_gp_religious_or_academic(gp_name_string):

    keywords = {'Mosque','Church','School','Institute','Education','Faculty'}

    set_gp_name_string = set(gp_name_string.split(' '))

    keywords_capture = set_gp_name_string.intersection(keywords)

    if keywords_capture:
        return True
    else:
        return False

print(is_gp_religious_or_academic('Faculty of Earch Sciences and Mining'))
print(is_gp_religious_or_academic('Almorada Church'))
print(is_gp_religious_or_academic('Health Insulation Building'))



# Task 4

def get_sanitation_priority(ratio:str, disabled:int, pop:int, gp:str):

    is_main_ratio_toilets_to_people_met(ratio)
    is_population_disabled(disabled, pop)
    is_gp_religious_or_academic(gp)

    if (is_main_ratio_toilets_to_people_met(ratio) == False and
        is_population_disabled(disabled, pop) == True and
        is_gp_religious_or_academic(gp) == True
    ):
        return "High Priority"

    elif (is_main_ratio_toilets_to_people_met(ratio) == True and
        is_population_disabled(disabled, pop) == False and
        is_gp_religious_or_academic(gp) == False
    ):
        return "Low Priority"

    else:
        return "Medium Priority"



print(get_sanitation_priority(ratio='1t/49p', disabled=52, pop=392, gp='Faculty - Students Dwelling'))
print(get_sanitation_priority(ratio='1t/29p', disabled=0, pop=178, gp='Mohamed Ali Abbas Secondary School for Girls'))
print(get_sanitation_priority(ratio='1t/17p', disabled=0, pop=52, gp='Alsalam Old Mosque'))
print(get_sanitation_priority(ratio='1t/6p', disabled=0, pop=12, gp='Nile Club'))


# Task 7
print(is_main_ratio_toilets_to_people_met('1t/395p'))
print(get_sanitation_priority(ratio = '1t/395p',disabled=0, pop=1580, gp='Almuntazah'))