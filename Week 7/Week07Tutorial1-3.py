import requests
from pprint import pprint

epqs_url = ('https://epqs.nationalmap.gov/v1/json?'
            'x=-75.191218&y=39.95140&units=Feet&wkid=4326&includeDate=False')

response = requests.get(url = epqs_url)

result = response.json()

pprint(result, width = 30)




nld_systems_url = 'https://levees.sec.usace.army.mil:443/api-local/systems/query?as=system&in=%40state%3Alouisiana&md=false'
nld_systems = requests.get(url = nld_systems_url).json()

# The response returns a LIST of DICTs.
print(f'There are {len(nld_systems)} levee systems in Louisiana.')

pprint(nld_systems, width = 60)


# Iterate the list of dictionaries in the response to get the wanted fields
nld_systems_headers = ['ID', 'Location', 'Accreditation Rating', 'Primary Purpose']
nld_systems_table = []

for nld_system in nld_systems:
    system_id = nld_system['id']
    location = nld_system['location']
    rating = nld_system['femaAccreditationRating']
    purpose = nld_system['primaryPurpose']

    nld_systems_table.append([system_id, location, rating, purpose])

print(nld_systems_headers)
for row in nld_systems_table:
    print(row)


# Dynamic Data Analysis using Python Requests
system_id = '4405000554'
nld_risk_screenings_url = (f'https://levees.sec.usace.army.mil:443/api-local/system/{system_id}/screenings')
screenings = requests.get(nld_risk_screenings_url).json()

pprint(screenings, width = 60)

nld_screenings_headers = ['ID', 'Location', 'Financial Risk', 'People at Risk', 'Structures at Risk']
nld_screenings_table = []

for nld_system in nld_systems:
    system_id = nld_system['id']
    location = nld_system['location']

    nld_risk_screenings_url = (f'https://levees.sec.usace.army.mil:443/api-local/system/{system_id}/screenings')
    screenings = requests.get(url = nld_risk_screenings_url).json()

    if screenings:
        print(f'{system_id} has the following screenings:')
        for screening in screenings:
            print(f'\t{str(screening)}')
            financial_risk = screening['financialRisk']
            people_at_risk = screening['peopleAtRisk']
            structures_at_risk = screening['structuresAtRisk']
            nld_screenings_table.append([system_id, location, financial_risk, people_at_risk, structures_at_risk])

    else:
        print(f'{system_id} has no screenings.')
        nld_screenings_table.append([system_id, location, None, None, None])

print(nld_screenings_headers)
for row in nld_screenings_table:
    print(row)