"""
Project for Week 3 of "Python Data Analysis".
Read and write CSV files using a dictionary of dictionaries.

This module contains various methods for reading and writing data files.
"""

import csv

def read_csv_fieldnames(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Ouput:
      A list of strings corresponding to the field names in
      the given CSV file.
    """
    column_names = []
    with open(filename) as csvfile:
        csvreader = csv.DictReader(csvfile,
                                    delimiter=separator,
                                    quotechar=quote)
        column_names = csvreader.fieldnames
    return column_names

def read_csv_as_list_dict(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a list of dictionaries where each item in the list
      corresponds to a row in the CSV file.  The dictionaries in the
      list map the field names to the field values for that row.
    """
    table = []
    with open(filename) as csvfile:
        csvreader = csv.DictReader(csvfile,
                                    delimiter = separator,
                                    quotechar = quote)
        for row in csvreader:
            table.append(row)

    return table


def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      keyfield  - field to use as key for rows
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a dictionary of dictionaries where the outer dictionary
      maps the value in the key_field to the corresponding row in the
      CSV file.  The inner dictionaries map the field names to the
      field values for that row.
    """
    table = {}
    with open(filename) as csvfile:
        csvreader = csv.DictReader(csvfile,
                                    delimiter = separator,
                                    quotechar = quote)
        for row in csvreader:
            table[row[keyfield]] = row

    return table


def write_csv_from_list_dict(filename, table, fieldnames, separator, quote):
    """
    Inputs:
      filename   - name of CSV file
      table      - list of dictionaries containing the table to write
      fieldnames - list of strings corresponding to the field names in order
      separator  - character that separates fields
      quote      - character used to optionally quote fields
    Output:
      Writes the table to a CSV file with the name filename, using the
      given fieldnames.  The CSV file should use the given separator and
      quote characters.  All non-numeric fields will be quoted.
    """
    with open(filename, 'wt') as csvfile:
        writer = csv.DictWriter(csvfile,
                                fieldnames = fieldnames,
                                delimiter = separator,
                                quotechar = quote,
                                quoting = csv.QUOTE_NONNUMERIC)

        writer.writeheader()
        for row in table:
            writer.writerow(row)

file_name = 'table1.csv'
separator = ","
quoter = '"'
field_names = read_csv_fieldnames(file_name, separator, quoter)
print(field_names)

table = read_csv_as_nested_dict(file_name, 'Field1', separator, quoter)
print(table)

table = read_csv_as_list_dict(file_name, separator, quoter)
print(table)

field_names = ('Field1', 'Field2', 'Field3', 'Field4')
quoter = "'"
write_csv_from_list_dict("output.txt", table, field_names, separator, quoter)
