import requests
from pathlib import Path
from pprint import pprint

wash_files_url = 'https://datasafe-h5afbhf4gwctabaa.z01.azurefd.net/api/Files/TOP/rep_wash'
wash_files_data = requests.get(wash_files_url).json()

pprint(wash_files_data, width = 60)


# Download a specific version of a data or metadata file
wash_files_download_url = f'https://datasafe-h5afbhf4gwctabaa.z01.azurefd.net/api/Download/TOP/rep_wash/2023-07-27/data'
wash_files_download_response = requests.get(url = wash_files_download_url)

wash_files_download = wash_files_download_response.content

export_file_path = Path(f'/Users/macbookairfromboeing/Downloads/Penn/Courses/2025 Fall/ENVS 5726/Week 07 - REST APIs/Week07TutorialData/WHO_WASH_Data_20230727.xlsx')

with open(export_file_path, 'wb') as export_file:
    export_file.write(wash_files_download)



# Use For Loop to download all the files in the HIDR WASH dataset using versionIds
for version in wash_files_data['versions']:
    file_date = version['versionId']
    print(f'Downloading WHO WASH data for {file_date}')

    wash_files_download_url_ALL = f'https://datasafe-h5afbhf4gwctabaa.z01.azurefd.net/api/Download/TOP/rep_wash/{file_date}/data'
    wash_files_download_response_ALL = requests.get(url = wash_files_download_url_ALL)
    wash_files_download_ALL = wash_files_download_response_ALL.content

    export_file_path = Path(f'/Users/macbookairfromboeing/Downloads/Penn/Courses/2025 Fall/ENVS 5726/Week 07 - REST APIs/Week07TutorialData/WHO_WASH_Data_{file_date}.xlsx')
    with open(export_file_path, 'wb') as export_file:
        export_file.write(wash_files_download_ALL)



# Downloading Zip Files
import zipfile
import io
import shutil

url = f'https://datasafe-h5afbhf4gwctabaa.z01.azurefd.net/api/Download/TOP/rep_wash'
response = requests.get(url = url)
content = response.content
zipfile_download = zipfile.ZipFile(io.BytesIO(content))

zip_directory = Path('/Users/macbookairfromboeing/Downloads/Penn/Courses/2025 Fall/ENVS 5726/Week 07 - REST APIs/Week07TutorialData/rep_wash')
zip_directory.mkdir(parents = True, exist_ok = True)
zipfile_download.extractall(path = zip_directory)