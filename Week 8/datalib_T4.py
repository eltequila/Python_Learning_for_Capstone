from collections import namedtuple
from typing import List, Dict, Any, Type, Union
import statistics

def summarize(table:List[tuple],summary_method:str, value_column:str) -> Union[float, int]:

    column_values = [getattr(row, value_column) for row in table]

    print(f'Summarzing {len(table)} rows by the {summary_method} of {value_column}.')

    assert summary_method in ['MEAN', 'MCOUNT', 'MIN', 'MAX']

    if summary_method == 'MEAN':
        return statistics.mean(column_values)

    if summary_method == 'COUNT':
        return len(column_values)

    if summary_method == 'MIN':
        return min(column_values)

    if summary_method == 'MAX':
        return max(column_values)

    return 0


def summrize_by_category(table:List[tuple], summary_method: str, value_column:str, category_column:str) -> List[tuple]:
    assert summary_method in ['MEAN', 'COUNT', 'MIN', 'MAX']

    print(f'Summarizing {len(table)} rows by {summary_method} of {value_column} by category {category_column}.')

    values_by_category: Dict[Any, List[Any]] = {}

    for row in table:
        value = getattr(row, value_column)
        category = getattr(row, category_column)
        if category not in values_by_category:
            values_by_category[category] = [value]
        else:
            values_by_category[category].append(value)

    summary_column_name = f'{summary_method}_{value_column}'

    Summary: Type[tuple] = namedtuple(typename='Summary', field_names=[category_column, summary_column_name])
    summary_table: List[tuple] = []

    for category in values_by_category:
        value_list = values_by_category[category]

        if summary_method == 'MEAN':
            summarized_value = statistics.mean(value_list)
        if summary_method == 'COUNT':
            summarized_value = len(value_list)
        if summary_method == 'MIN':
            summarized_value = min(value_list)
        if summary_method == 'MAX':
            summarized_value = max(value_list)

        summary = Summary(category, summarized_value)
        summary_table.append(summary)

    return summary_table


