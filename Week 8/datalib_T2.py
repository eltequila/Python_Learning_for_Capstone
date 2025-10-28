from typing import List, Any

def filter_equals (table:List[tuple], column_name:str, value:Any) -> List[tuple]:

    print(f'Filtering {len(table)} rows where {column_name} equals {value}.')

    return table


def filter_null(table:List[tuple], column_name_list: List[str]) -> List[tuple]:

    print(f'Filtering {len(table)} rows where {column_name_list} are null.')

    return table


def summarize(table:List[tuple], column_name: str, summary_method: str) -> List[tuple]:

    print(f'Summarizing {len(table)} rows by the {summary_method} of {column_name}.')

    return table


def join(target_table: List[tuple], join_table: List[tuple], join_column_name: str) -> List[tuple]:

    print(f'Joining {len(join_table)} rows to {len(target_table)} rows based on column {join_column_name}.')

    return target_table


