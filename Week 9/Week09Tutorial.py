# Tutorial 1
from bs4 import BeautifulSoup

soup = BeautifulSoup('<html></html>', 'html.parser')
print('Successfully imported beautifulsoup4.')



# Tutorial 2
from openpyxl import load_workbook
sbti_xlsx_path = r'/Users/macbookairfromboeing/Downloads/Penn/Courses/2025 Fall/ENVS 5726/Week 09 - Updated Version/Week09TutorialData/SBTI_TargetsByCompany.xlsx'

workbook = load_workbook(filename=sbti_xlsx_path)
sheet = workbook['Data']

near_term_target_year_column = [cell.value for cell in sheet['k']
                                if isinstance(cell.value, (int, float, complex))]

print(near_term_target_year_column)


import matplotlib.pyplot as plt

bin_width = 1
bins = range(min(near_term_target_year_column),max(near_term_target_year_column)+bin_width, bin_width)

plt.hist(near_term_target_year_column, bins=bins, color='skyblue', edgecolor='black')

plt.xlabel('Near Term Target Year')
plt.ylabel('Number of Companies')
plt.title('Distribution of Near Term Target Year')

print('Creating histogram of Near Term Target Year.')
plt.savefig(r'/Users/macbookairfromboeing/Downloads/Penn/Courses/2025 Fall/ENVS 5726/Week 09 - Updated Version/Week09TutorialData/SBTI_Near_Term_Target_Year_Histogram.png', bbox_inches='tight')
plt.close()


