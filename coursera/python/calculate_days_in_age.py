"""
This program calculates the number of days since a person's birthdate.
"""

import datetime

def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """
    # Save month attributes.
    selected_date = datetime.date(year, month, 1)

    # Use the day attribute of the datetime.date object
    # to get the last day.
    # We already know that there are 31 days in December.
    if selected_date.month == 12:
        days = datetime.date(selected_date.year, selected_date.month, 31).day
    else:
        # For months other than December, work backwards by getting the
        # subtracting the first day of the following month to get the
        # last day of the selected month.
        # This doesn't work for December because we have to know the
        # year of the previous month.
        month_after_selected_month = datetime.date(
            selected_date.year, 
            selected_date.month + 1, 
            1)
        selected_month = month_after_selected_month - datetime.timedelta(days=1)
        days = selected_month.day
    return days

def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day

    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    
    # First validate in order the year, month, and day.
    if year >= datetime.MINYEAR and year <= datetime.MAXYEAR:
        if month >= 1 and month <= 12:
            if day >=1 and day <= days_in_month(year, month):
                return True
    return False

def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date

    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is
      before the first date.
    """

    # Valid both dates and then ensure that date1 is before date2.
    if is_valid_date(year1, month1, day1):
        if is_valid_date(year2, month2, day2):
            date_1 = datetime.date(year1, month1, day1)
            date_2 = datetime.date(year2, month2, day2)
            if date_1 < date_2:
                return abs((date_1 - date_2).days)
    
    return 0

def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid or if the input
      date is in the future.
    """
    
    birth_date = datetime.date(year, month, day)
    if is_valid_date(year, month, day):
        today = datetime.date.today()
        return days_between(year, 
                            month, 
                            day, 
                            today.year, 
                            today.month, 
                            today.day)
        
    return 0

yr, mon, days = 2018, 1, 31
month = str(yr) + "-" + str(mon) + "-" + str(days)
print("Days in month " + month + ": " + str(month == str(yr) + "-" + str(mon) + "-" + str(days_in_month(yr, mon))))

yr, mon, days = 2018, 2, 28
month = str(yr) + "-" + str(mon) + "-" + str(days)
print("Days in month " + month + ": " + str(month == str(yr) + "-" + str(mon) + "-" + str(days_in_month(yr, mon))))

yr, mon, days = 2018, 3, 31
month = str(yr) + "-" + str(mon) + "-" + str(days)
print("Days in month " + month + ": " + str(month == str(yr) + "-" + str(mon) + "-" + str(days_in_month(yr, mon))))

yr, mon, days = 2018, 4, 30
month = str(yr) + "-" + str(mon) + "-" + str(days)
print("Days in month " + month + ": " + str(month == str(yr) + "-" + str(mon) + "-" + str(days_in_month(yr, mon))))

yr, mon, days = 2018, 5, 31
month = str(yr) + "-" + str(mon) + "-" + str(days)
print("Days in month " + month + ": " + str(month == str(yr) + "-" + str(mon) + "-" + str(days_in_month(yr, mon))))

yr, mon, days = 2018, 6, 30
month = str(yr) + "-" + str(mon) + "-" + str(days)
print("Days in month " + month + ": " + str(month == str(yr) + "-" + str(mon) + "-" + str(days_in_month(yr, mon))))

yr, mon, days = 2018, 7, 31
month = str(yr) + "-" + str(mon) + "-" + str(days)
print("Days in month " + month + ": " + str(month == str(yr) + "-" + str(mon) + "-" + str(days_in_month(yr, mon))))

yr, mon, days = 2018, 8, 31
month = str(yr) + "-" + str(mon) + "-" + str(days)
print("Days in month " + month + ": " + str(month == str(yr) + "-" + str(mon) + "-" + str(days_in_month(yr, mon))))

yr, mon, days = 2018, 12, 31
month = str(yr) + "-" + str(mon) + "-" + str(days)
print("Days in month " + month + ": " + str(month == str(yr) + "-" + str(mon) + "-" + str(days_in_month(yr, mon))))

yr, mon, days = 2020, 2, 29
month = str(yr) + "-" + str(mon) + "-" + str(days)
print("Days in month " + month + ": " + str(month == str(yr) + "-" + str(mon) + "-" + str(days_in_month(yr, mon))))

yr, mon, days = 2018, 1, 32
month = str(yr) + "-" + str(mon) + "-" + str(days)
print("Days in month " + month + ": " + str(month == str(yr) + "-" + str(mon) + "-" + str(days_in_month(yr, mon))))

yr, mon, days = 2018, 1, 31
month = str(yr) + "-" + str(mon) + "-" + str(days)
print("Valid " + month + ": " + str(is_valid_date(yr, mon, days)))

yr, mon, days = 2018, 2, 31
month = str(yr) + "-" + str(mon) + "-" + str(days)
print("Valid " + month + ": " + str(is_valid_date(yr, mon, days)))

yr, mon, days = 2020, 2, 29
month = str(yr) + "-" + str(mon) + "-" + str(days)
print("Valid " + month + ": " + str(is_valid_date(yr, mon, days)))

yr, mon, days = 2020, 12, 31
month = str(yr) + "-" + str(mon) + "-" + str(days)
print("Valid " + month + ": " + str(is_valid_date(yr, mon, days)))

yr, mon, days = 0, 12, 32
month = str(yr) + "-" + str(mon) + "-" + str(days)
print("Valid " + month + ": " + str(is_valid_date(yr, mon, days)))

yr1, mon1, days1, yr2, mon2, days2 = 2018, 1, 1, 2018, 1, 31
print(days_between(yr1, mon1, days1, yr2, mon2, days2))

yr1, mon1, days1, yr2, mon2, days2 = 2018, 1, 1, 2018, 1, 31
date_1 = str(yr1) + "-" + str(mon1) + "-" + str(days1)
date_2 = str(yr2) + "-" + str(mon2) + "-" + str(days2)
print("Days between " + date_1 + " and " + date_2 + ": " + str(days_between(yr1, mon1, days1, yr2, mon2, days2)))

yr1, mon1, days1, yr2, mon2, days2 = 2018, 1, 1, 2018, 1, 1
date_1 = str(yr1) + "-" + str(mon1) + "-" + str(days1)
date_2 = str(yr2) + "-" + str(mon2) + "-" + str(days2)
print("Days between " + date_1 + " and " + date_2 + ": " + str(days_between(yr1, mon1, days1, yr2, mon2, days2)))

yr1, mon1, days1, yr2, mon2, days2 = 2018, 1, 1, 2018, 12, 31
date_1 = str(yr1) + "-" + str(mon1) + "-" + str(days1)
date_2 = str(yr2) + "-" + str(mon2) + "-" + str(days2)
print("Days between " + date_1 + " and " + date_2 + ": " + str(days_between(yr1, mon1, days1, yr2, mon2, days2)))

yr1, mon1, days1, yr2, mon2, days2 = 2020, 1, 1, 2020, 12, 31
date_1 = str(yr1) + "-" + str(mon1) + "-" + str(days1)
date_2 = str(yr2) + "-" + str(mon2) + "-" + str(days2)
print("Days between " + date_1 + " and " + date_2 + ": " + str(days_between(yr1, mon1, days1, yr2, mon2, days2)))

yr1, mon1, days1, yr2, mon2, days2 = 2020, 1, 1, 2019, 12, 31
date_1 = str(yr1) + "-" + str(mon1) + "-" + str(days1)
date_2 = str(yr2) + "-" + str(mon2) + "-" + str(days2)
print("Days between " + date_1 + " and " + date_2 + ": " + str(days_between(yr1, mon1, days1, yr2, mon2, days2)))

yr1, mon1, days1, yr2, mon2, days2 = 0, 1, 1, 2020, 12, 31
date_1 = str(yr1) + "-" + str(mon1) + "-" + str(days1)
date_2 = str(yr2) + "-" + str(mon2) + "-" + str(days2)
print("Days between " + date_1 + " and " + date_2 + ": " + str(days_between(yr1, mon1, days1, yr2, mon2, days2)))

yr1, mon1, days1, yr2, mon2, days2 = 0, 0, 1, 2020, 12, 31
date_1 = str(yr1) + "-" + str(mon1) + "-" + str(days1)
date_2 = str(yr2) + "-" + str(mon2) + "-" + str(days2)
print("Days between " + date_1 + " and " + date_2 + ": " + str(days_between(yr1, mon1, days1, yr2, mon2, days2)))

yr1, mon1, days1, yr2, mon2, days2 = 0, 0, 0, 2020, 12, 31
date_1 = str(yr1) + "-" + str(mon1) + "-" + str(days1)
date_2 = str(yr2) + "-" + str(mon2) + "-" + str(days2)
print("Days between " + date_1 + " and " + date_2 + ": " + str(days_between(yr1, mon1, days1, yr2, mon2, days2)))

yr1, mon1, days1, yr2, mon2, days2 = 1, 1, 1, 2020, 12, 31
date_1 = str(yr1) + "-" + str(mon1) + "-" + str(days1)
date_2 = str(yr2) + "-" + str(mon2) + "-" + str(days2)
print("Days between " + date_1 + " and " + date_2 + ": " + str(days_between(yr1, mon1, days1, yr2, mon2, days2)))

yr1, mon1, days1, yr2, mon2, days2 = 1, 1, 1, 0, 1, 1
date_1 = str(yr1) + "-" + str(mon1) + "-" + str(days1)
date_2 = str(yr2) + "-" + str(mon2) + "-" + str(days2)
print("Days between " + date_1 + " and " + date_2 + ": " + str(days_between(yr1, mon1, days1, yr2, mon2, days2)))

yr1, mon1, days1, yr2, mon2, days2 = 1, 1, 1, 0, 0, 1
date_1 = str(yr1) + "-" + str(mon1) + "-" + str(days1)
date_2 = str(yr2) + "-" + str(mon2) + "-" + str(days2)
print("Days between " + date_1 + " and " + date_2 + ": " + str(days_between(yr1, mon1, days1, yr2, mon2, days2)))

yr1, mon1, days1, yr2, mon2, days2 = 1, 1, 1, 0, 0, 0
date_1 = str(yr1) + "-" + str(mon1) + "-" + str(days1)
date_2 = str(yr2) + "-" + str(mon2) + "-" + str(days2)
print("Days between " + date_1 + " and " + date_2 + ": " + str(days_between(yr1, mon1, days1, yr2, mon2, days2)))

yr1, mon1, days1, yr2, mon2, days2 = 2018, 1, 6, 2018, 1, 7
date_1 = str(yr1) + "-" + str(mon1) + "-" + str(days1)
date_2 = str(yr2) + "-" + str(mon2) + "-" + str(days2)
print("Days between " + date_1 + " and " + date_2 + ": " + str(days_between(yr1, mon1, days1, yr2, mon2, days2)))

yr1, mon1, days1, yr2, mon2, days2 = 2018, 2, 1, 2018, 3, 1
date_1 = str(yr1) + "-" + str(mon1) + "-" + str(days1)
date_2 = str(yr2) + "-" + str(mon2) + "-" + str(days2)
print("Days between " + date_1 + " and " + date_2 + ": " + str(days_between(yr1, mon1, days1, yr2, mon2, days2)))

yr1, mon1, days1, yr2, mon2, days2 = 2020, 2, 1, 2020, 3, 1
date_1 = str(yr1) + "-" + str(mon1) + "-" + str(days1)
date_2 = str(yr2) + "-" + str(mon2) + "-" + str(days2)
print("Days between " + date_1 + " and " + date_2 + ": " + str(days_between(yr1, mon1, days1, yr2, mon2, days2)))

birth_date = datetime.date(1900, 1, 1)
bdate = str(birth_date.year) + "-" + str(birth_date.month) + "-" + str(birth_date.day)
print("Days since birthdate " 
        + bdate + ": " 
        + str(age_in_days(birth_date.year, birth_date.month, birth_date.day)))

birth_date = datetime.date(1900, 1, 2)
bdate = str(birth_date.year) + "-" + str(birth_date.month) + "-" + str(birth_date.day)
print("Days since birthdate " 
        + bdate + ": " 
        + str(age_in_days(birth_date.year, birth_date.month, birth_date.day)))

birth_date = datetime.date(2018, 1, 8)
bdate = str(birth_date.year) + "-" + str(birth_date.month) + "-" + str(birth_date.day)
print("Days since birthdate " 
        + bdate + ": " 
        + str(age_in_days(birth_date.year, birth_date.month, birth_date.day)))
