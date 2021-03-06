"""
Project for Week 4 of "Python Data Analysis".
Processing CSV files with baseball stastics.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import csv

##
## Provided code from Week 3 Project
##

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
    with open(filename, newline='') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=separator, quotechar=quote)
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
    with open(filename, newline='') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=separator, quotechar=quote)
        for row in csvreader:
            rowid = row[keyfield]
            table[rowid] = row
    return table

##
## Provided formulas for common batting statistics
##

# Typical cutoff used for official statistics
MINIMUM_AB = 500

def batting_average(info, batting_stats):
    """
    Inputs:
      batting_stats - dictionary of batting statistics (values are strings)
    Output:
      Returns the batting average as a float
    """
    hits = float(batting_stats[info["hits"]])
    at_bats = float(batting_stats[info["atbats"]])
    if at_bats >= MINIMUM_AB:
        return hits / at_bats
    else:
        return 0

def onbase_percentage(info, batting_stats):
    """
    Inputs:
      batting_stats - dictionary of batting statistics (values are strings)
    Output:
      Returns the on-base percentage as a float
    """
    hits = float(batting_stats[info["hits"]])
    at_bats = float(batting_stats[info["atbats"]])
    walks = float(batting_stats[info["walks"]])
    if at_bats >= MINIMUM_AB:
        return (hits + walks) / (at_bats + walks)
    else:
        return 0

def slugging_percentage(info, batting_stats):
    """
    Inputs:
      batting_stats - dictionary of batting statistics (values are strings)
    Output:
      Returns the slugging percentage as a float
    """
    hits = float(batting_stats[info["hits"]])
    doubles = float(batting_stats[info["doubles"]])
    triples = float(batting_stats[info["triples"]])
    home_runs = float(batting_stats[info["homeruns"]])
    singles = hits - doubles - triples - home_runs
    at_bats = float(batting_stats[info["atbats"]])
    if at_bats >= MINIMUM_AB:
        return (singles + 2 * doubles + 3 * triples + 4 * home_runs) / at_bats
    else:
        return 0


##
## Part 1: Functions to compute top batting statistics by year
##

def filter_by_year(statistics, year, yearid):
    """
    Inputs:
      statistics - List of batting statistics dictionaries
      year       - Year to filter by
      yearid     - Year ID field in statistics
    Outputs:
      Returns a list of batting statistics dictionaries that
      are from the input year.
    """
    return list(filter(lambda row: row[yearid] == str(year), statistics))


def top_player_ids(info, statistics, formula, numplayers):
    """
    Inputs:
      info       - Baseball data information dictionary
      statistics - List of batting statistics dictionaries
      formula    - function that takes an info dictionary and a
                   batting statistics dictionary as input and
                   computes a compound statistic
      numplayers - Number of top players to return
    Outputs:
      Returns a list of tuples, player ID and compound statistic
      computed by formula, of the top numplayers players sorted in
      decreasing order of the computed statistic.
    """
    big_list = []
    for player_stats in statistics:
        comp_stat = formula(info, player_stats)
        player = (player_stats[info['playerid']], comp_stat)
        big_list.append(player)
    big_list.sort(key = lambda pair: pair[1], reverse = True)
    return big_list[:numplayers]


def lookup_player_names(info, top_ids_and_stats):
    """
    Inputs:
      info              - Baseball data information dictionary
      top_ids_and_stats - list of tuples containing player IDs and
                          computed statistics
    Outputs:
      List of strings of the form "x.xxx --- FirstName LastName",
      where "x.xxx" is a string conversion of the float stat in
      the input and "FirstName LastName" is the name of the player
      corresponding to the player ID in the input.
    """
    master_list = read_csv_as_nested_dict(info['masterfile'],
                                            info['playerid'],
                                            info['separator'],
                                            info['quote'])

    output = []
    for player in top_ids_and_stats:
        comp_stat_str = "{:1.3f} --- {} {}".format(player[1],
                                                master_list[player[0]][info['firstname']],
                                                master_list[player[0]][info['lastname']])
        output.append(comp_stat_str)
    return output


def compute_top_stats_year(info, formula, numplayers, year):
    """
    Inputs:
      info        - Baseball data information dictionary
      formula     - function that takes an info dictionary and a
                    batting statistics dictionary as input and
                    computes a compound statistic
      numplayers  - Number of top players to return
      year        - Year to filter by
    Outputs:
      Returns a list of strings for the top numplayers in the given year
      according to the given formula.
    """
    bat_stats_ = read_csv_as_list_dict(info['battingfile'],
                                        info['separator'],
                                        info['quote'])
    bat_stats_in_yr = filter_by_year(bat_stats_, year, info['yearid'])
    top_players = top_player_ids(info, bat_stats_in_yr, formula, numplayers)
    top_player_stats = lookup_player_names(info, top_players)
    return top_player_stats


##
## Part 2: Functions to compute top batting statistics by career
##

def aggregate_by_player_id(statistics, playerid, fields):
    """
    Inputs:
      statistics - List of batting statistics dictionaries
      playerid   - Player ID field name
      fields     - List of fields to aggregate
    Output:
      Returns a nested dictionary whose keys are player IDs and whose values
      are dictionaries of aggregated stats.  Only the fields from the fields
      input will be aggregated in the aggregated stats dictionaries.
    """
    # build an empty dict with just the playerid
    player_stats = {}
    for player in statistics:
        player_stats[player[playerid]] = {}

    # collect stats by looping through them for playerid
    for player_id, dummy in player_stats.items():
        flds = []
        for player in statistics:
            if player[playerid] == player_id:
                # build list of stats for each field for playerid
                for stat in fields:
                    if stat in player.keys():
                        flds.append([stat, int(player[stat])])
        player_stats[player_id] = flds

    # sum up the values for each stat for each player
    for p_id, p_stats in player_stats.items():
        fld_list = {}
        f_values = []
        for field in fields:
            f_values = []
            for pair in p_stats:
                if field == pair[0]:
                    f_values.append(pair[1])
                    fld_list[pair[0]] = sum(f_values)
                    fld_list[playerid] = p_id
                    player_stats[p_id] =  fld_list

    return player_stats

def compute_top_stats_career(info, formula, numplayers):
    """
    Inputs:
      info        - Baseball data information dictionary
      formula     - function that takes an info dictionary and a
                    batting statistics dictionary as input and
                    computes a compound statistic
      numplayers  - Number of top players to return
    Output:
    Returns a list of strings of the same form as returned
    by lookup_player_names that correspond to the numplayers players
    with the highest compound statistic computed by formula for their
    careers.
    """
    bat_stats = read_csv_as_list_dict(info['battingfile'],
                                        info['separator'],
                                        info['quote'])

    stat_aggregate = aggregate_by_player_id(bat_stats, info['playerid'], info['battingfields'])
    stats = list(stat_aggregate.values())
    top_players = top_player_ids(info, stats, formula, numplayers)
    top_player_stats = lookup_player_names(info, top_players)
    return top_player_stats


##
## Provided testing code
##

def test_baseball_statistics():
    """
    Simple testing code.
    """

    #
    # Dictionary containing information needed to access baseball statistics
    # This information is all tied to the format and contents of the CSV files
    #
    baseballdatainfo = {"masterfile": "Master_2016.csv",   # Name of Master CSV file
                        "battingfile": "Batting_2016.csv", # Name of Batting CSV file
                        "separator": ",",                  # Separator character in CSV files
                        "quote": '"',                      # Quote character in CSV files
                        "playerid": "playerID",            # Player ID field name
                        "firstname": "nameFirst",          # First name field name
                        "lastname": "nameLast",            # Last name field name
                        "yearid": "yearID",                # Year field name
                        "atbats": "AB",                    # At bats field name
                        "hits": "H",                       # Hits field name
                        "doubles": "2B",                   # Doubles field name
                        "triples": "3B",                   # Triples field name
                        "homeruns": "HR",                  # Home runs field name
                        "walks": "BB",                     # Walks field name
                        "battingfields": ["AB", "H", "2B", "3B", "HR", "BB"]}

    print("Top 5 batting averages in 1923")
    top_batting_average_1923 = compute_top_stats_year(baseballdatainfo, batting_average, 5, 1923)
    for player in top_batting_average_1923:
        print(player)
    print("")

    print("Top 10 batting averages in 2010")
    top_batting_average_2010 = compute_top_stats_year(baseballdatainfo, batting_average, 10, 2010)
    for player in top_batting_average_2010:
        print(player)
    print("")

    print("Top 10 on-base percentage in 2010")
    top_onbase_2010 = compute_top_stats_year(baseballdatainfo, onbase_percentage, 10, 2010)
    for player in top_onbase_2010:
        print(player)
    print("")

    print("Top 10 slugging percentage in 2010")
    top_slugging_2010 = compute_top_stats_year(baseballdatainfo, slugging_percentage, 10, 2010)
    for player in top_slugging_2010:
        print(player)
    print("")

    # You can also use lambdas for the formula
    #  This one computes onbase plus slugging percentage
    print("Top 10 OPS in 2010")
    top_ops_2010 = compute_top_stats_year(baseballdatainfo,
                                          lambda info, stats: (onbase_percentage(info, stats) +
                                                               slugging_percentage(info, stats)),
                                          10, 2010)
    for player in top_ops_2010:
        print(player)
    print("")

    print("Top 20 career batting averages")
    top_batting_average_career = compute_top_stats_career(baseballdatainfo, batting_average, 20)
    for player in top_batting_average_career:
        print(player)
    print("")


# Make sure the following call to test_baseball_statistics is
# commented out when submitting to OwlTest/CourseraTest.

# test_baseball_statistics()
baseballdatainfo = {"masterfile": "baseballdatabank-2017.1/isp_baseball_files_small/master2.csv",   # Name of Master CSV file
                    "battingfile": "baseballdatabank-2017.1/isp_baseball_files_small/batting2.csv", # Name of Batting CSV file
                    "separator": ",",                  # Separator character in CSV files
                    "quote": '"',                      # Quote character in CSV files
                    "playerid": "playerID",            # Player ID field name
                    "firstname": "nameFirst",          # First name field name
                    "lastname": "nameLast",            # Last name field name
                    "yearid": "yearID",                # Year field name
                    "atbats": "AB",                    # At bats field name
                    "hits": "H",                       # Hits field name
                    "doubles": "2B",                   # Doubles field name
                    "triples": "3B",                   # Triples field name
                    "homeruns": "HR",                  # Home runs field name
                    "walks": "BB",                     # Walks field name
                    "battingfields": ["AB", "H", "2B", "3B", "HR", "BB"]}

def print_table(lst):
    """
    Formats display the of the table for readability.
    """
    my_cols = "{:4} " * 22
    for rw in lst:
        cl = []
        for k,v in rw.items():
            cl.append(rw[k])
        print(my_cols.format(*cl))

# Get list of batting stats in the form of a list of dictionaries.
bat_stats = read_csv_as_list_dict("baseballdatabank-2017.1/isp_baseball_files_small/batting2.csv", ",", '"')
#bat_stats = read_csv_as_list_dict("baseballdatabank-2017.1/core/Batting_2016.csv", ",", '"')

print("----- filter_by_year -----")
print('bat_stats_by_yr = filter_by_year(bat_stats, 2007, "yearID")')
bat_stats_by_yr = filter_by_year(bat_stats, 2006, "yearID")
for rw in bat_stats_by_yr:
    print(rw)

#~ #def top_player_ids(info, statistics, formula, numplayers):
print("----- top_player_ids -----")
print("my_top_players = top_player_ids(baseballdatainfo, bat_stats_by_yr, batting_average, 10)")
my_top_players = top_player_ids(baseballdatainfo, bat_stats_by_yr, batting_average, 10)
print(my_top_players)

#def lookup_player_names(info, top_ids_and_stats):
print("----- lookup_player_names -----")
print("my_lookup_players = lookup_player_names(baseballdatainfo, my_top_players)")
my_lookup_players = lookup_player_names(baseballdatainfo, my_top_players)
print(my_lookup_players)

#def compute_top_stats_year(info, formula, numplayers, year):
print("----- compute_top_stats_year -----")
print("top_player_stats = compute_top_stats_year(baseballdatainfo, batting_average, 10, 2007)")
top_player_stats = compute_top_stats_year(baseballdatainfo, batting_average, 10, 2006)
for rw in top_player_stats:
    print(rw)


#def aggregate_by_player_id(statistics, playerid, fields):
print("----- aggregate_by_player_id -----")
print("aggregate_by_player = aggregate_by_player_id(statistics, playerid, fields)")
aggregate_by_player = aggregate_by_player_id(
[{'stat3': '5', 'stat1': '3', 'player': '1', 'stat2': '4'},
{'stat3': '8', 'stat1': '2', 'player': '1', 'stat2': '1'},
{'stat3': '4', 'stat1': '5', 'player': '1', 'stat2': '7'}],
'player', ['stat1', 'stat2'])
print(aggregate_by_player)
