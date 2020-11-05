dict_of_month = { "January": 31,
        "February" : 28,
        "March" : 31,
        "April" : 30,
        "May" : 31,
        "June" : 30,
        "July" : 31,
        "August" : 31,
        "September" : 30,
        "October" : 31,
        "November" : 30,
        "December" : 31}

def Sundays():
    day = 2   # 1st jan 1901 was a tuesday that's why i initialsed days with 2
    No_of_sundays = 0

    for year in range(1901,2001):

        for m in dict_of_month:

            day =day+ dict_of_month[m]
            if year % 4 == 0 and m == "February":  # Condition for leap year
                day += 1
            if day % 7 == 0:  #Sunday conidtion : starting from tueday at day=2, Each sunday falls on this condition
                No_of_sundays += 1
    return No_of_sundays
No_of_sundays=countingSundays()
print( No_of_sundays)
