"""
Week 3 practice project template for Python Data Analysis
Reading and writing CSV files using lists
"""
import csv

#########################################################
# Part 1 - Week 3

def print_table(table):
    """
    Echo a nested list to the console
    """
    for row in table:
        print(row)


def read_csv_file(file_name):
    """
    Given a CSV file, read the data into a nested list
    Input: String corresponding to comma-separated  CSV file
    Output: Lists of lists consisting of the fields in the CSV file
    """
    table = []
    with open(file_name) as csvfile:
        csvreader = csv.reader(csvfile,
                                skipinitialspace=True,
                                delimiter=",",
                                quoting=csv.QUOTE_ALL)
        for line in csvreader:
            table.append(line)

    return table

def write_csv_file(csv_table, file_name):
    """
    Input: Nested list csv_table and a string file_name
    Action: Write fields in csv_table into a comma-separated CSV file
    with the name file_name
    """
    with open(file_name,'w',newline='') as csvfile:
        csvwriter = csv.writer(csvfile,
                                skipinitialspace=True,
                                delimiter=',',
                                quoting=csv.QUOTE_ALL)

        for row in csv_table:
            csvwriter.writerow(row)

def test_part1_code():
    """
    Run examples that test the functions for part 1
    """

    # Simple test for reader
    test_table = read_csv_file("test_case.csv")  # create a small CSV for this test
    print_table(test_table)
    write_csv_file(test_table, "test_table.csv")
    test_table_2 = read_csv_file("test_table.csv")
    if test_table == test_table_2:
        print("They match")

    # Test the writer
    cancer_risk_table = read_csv_file("cancer_risk05_v4_county.csv")
    #~ print(cancer_risk_table)
    write_csv_file(cancer_risk_table, "cancer_risk05_v4_county_copy.csv")
    cancer_risk_copy = read_csv_file("cancer_risk05_v4_county_copy.csv")
    if cancer_risk_table == cancer_risk_copy:
        print("data matches")

    # Test whether two tables are the same

test_part1_code()

