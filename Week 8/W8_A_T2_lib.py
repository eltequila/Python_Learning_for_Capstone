from collections import namedtuple
from typing import List,  Any, Type, Union, NamedTuple

def convert_yesno_to_binary(table: List[tuple]):

    FinalConvertedNamedTuple:type[tuple] = type(table[0])

    converted_table: List[tuple] = []


    list_of_lists_from_namedtuple = [list(survey) for survey in table]

    for row in list_of_lists_from_namedtuple:

         converted_list:List[Any] = []

         for value in row:
             if value == 'Yes':
                 converted_list.append(1)
             elif value in ('No', '', 'Do not know'):
                 converted_list.append(0)
             else:
                 converted_list.append(value)

         final_converted_namedtuple = FinalConvertedNamedTuple(*converted_list)

         converted_table.append(final_converted_namedtuple)

    return converted_table



def get_categories(table:List[tuple], category_column:str) :

    all_values = []
    for row in table:
        specific_value = getattr(row, category_column)
        all_values.append(specific_value)

    unique_value_set = set(all_values)
    return unique_value_set



def get_non_numeric_values(table:List[tuple]) :

    row_index = 0
    columns = table[0]._fields
    master_alarm = []

    for row in table:

        for column in columns :
            value = getattr(row, column)

            if isinstance(value,(int,float,complex)) is False:
                alarm_triggered = f'Non-numeric value found at column {column} at row {row_index}, with contents _{value}_. Check corresponding cell.'
                master_alarm.append(f'{alarm_triggered}')

        row_index += 1

    return master_alarm



import pandas as pd
import numpy as np

def _findCorrelation_fast(corr, avg, cutoff):

    combsAboveCutoff = corr.where(lambda x: (np.tril(x) == 0) & (x > cutoff)).stack().index

    rowsToCheck = combsAboveCutoff.get_level_values(0)
    colsToCheck = combsAboveCutoff.get_level_values(1)

    msk = avg[colsToCheck] > avg[rowsToCheck].values
    deletecol = pd.unique(np.r_[colsToCheck[msk], rowsToCheck[~msk]]).tolist()

    return deletecol

def _findCorrelation_exact(corr, avg, cutoff):

    x = corr.loc[(*[avg.sort_values(ascending=False).index] * 2,)]

    if (x.dtypes.values[:, None] == ['int64', 'int32', 'int16', 'int8']).any():
        x = x.astype(float)

    x.values[(*[np.arange(len(x))] * 2,)] = np.nan

    deletecol = []
    for ix, i in enumerate(x.columns[:-1]):
        for j in x.columns[ix + 1:]:
            if x.loc[i, j] > cutoff:
                if x[i].mean() > x[j].mean():
                    deletecol.append(i)
                    x.loc[i] = x[i] = np.nan
                else:
                    deletecol.append(j)
                    x.loc[j] = x[j] = np.nan
    return deletecol