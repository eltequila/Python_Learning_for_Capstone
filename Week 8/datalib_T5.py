from typing import List, Dict, Any, Tuple, Type
from collections import namedtuple

def join(target_table: List[tuple], join_table: List[tuple], join_column_name: str) -> List[tuple]:

    assert join_column_name in target_table[0]._fields
    assert join_column_name in join_table[0]._fields

    print(f'Joining {len(join_table)} rows to {len(target_table)} rows based on column{join_column_name}.')

    join_rows_by_id: Dict[Any, Tuple[Any]] = {}

    for join_row in join_table:
        join_id = getattr(join_row, join_column_name)

        join_rows_by_id[join_id] = join_row

    joined_row_class_name = f'{type(target_table[0]).__name__}_{type(join_table[0]).__name__}'

    target_columns = list(target_table[0]._fields)
    join_columns_no_dup = [f'{column}_joined'
                            if column in target_columns
                            else column for column in join_table[0]._fields]

    JoinRowClass: Type[tuple] = namedtuple(typename=joined_row_class_name,
                                           field_names=target_columns+join_columns_no_dup)

    joined_table:List[JoinRowClass] = []

    for target_row in target_table:
        target_id = getattr(target_row, join_column_name)

        if target_id in join_rows_by_id:
            join_row = join_rows_by_id[target_id]
            joined_row = JoinRowClass(*target_row, *join_row)
        else:
            join_row = [None]*len(join_table[0]._fields)
            joined_row = JoinRowClass(*target_row, *join_row)
        joined_table.append(joined_row)

    return joined_table