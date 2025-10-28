from collections import namedtuple

headers = ['column1','column2']
RowClass = namedtuple(typename='RowClass', field_names=headers)

my_row = RowClass(column1=10, column2=20)

column1_value = my_row.column1
column2_value = getattr(my_row,'column2')

print(column1_value)
print(column2_value)


