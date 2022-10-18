"""Dictionary related utility functions."""

__author__ = "730571332"

from csv import DictReader

# Define your functions below


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a CSV into a 'table'."""
    result: list[dict[str, str]] = []

    # Open the file
    file_handle = open(filename, "r", encoding="utf8")
    
    # Read the file
    csv_reader = DictReader(file_handle)

    # Append each row of csv_reader to result
    for row in csv_reader:
        result.append(row)
    
    
    # Close the file
    file_handle.close()    

    return result

def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []

    for row in table:
        result.append(row[column])

    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(table: dict[str, list[str]], count: int) -> dict[str, list[str]]:
    """Shows the first few rows of data for each column."""
    result: dict[str, list[str]] = {}

    for column in table:
        values = []
        for value in table[column]:
            if len(values) < count:
                values.append(value)
        result[column] = values
    return result


def select(table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produces a new table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}

    for name in names:
        result[name] = table[name]
    return result


def concat(firsttable: dict[str, list[str]], secondtable: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produces a new table comprised of two combined tables."""
    result: dict[str, list[str]] = {}

    for column in firsttable:
        result[column] = firsttable[column]
    for column in secondtable:
        if column in result:
            result[column] += secondtable[column]
        else:
            result[column] = secondtable[column]
    return result


def count(xs: list[str]) -> dict[str, int]:
    """Counts the number of times a value appears in an input list."""
    result: dict[str, int] = {}

    for x in xs:
        if x in result:
            result[x] += 1
        else:
            result[x] = 1
    return result