"""
Project 1

Class: CSCI 1913, Spring 2021, Section 10
Professor: Jerald Thomas
Student: Jacynda Alatoma (alato006)
"""

dotw_index = {
    0: "Sunday",
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday"
}


def get_doomsday_dotw(year):
    """By the year given, find out the doomsday for that year and return index of that year"""
    # get the century of the year
    stringYear = str(year)
    century = stringYear[:2] + "00"
    century = int(century)

    # get the century index
    centuryIdx = century % 400
    if centuryIdx == 0:
        centuryNum = 2
    elif centuryIdx == 100:
        centuryNum = 0
    elif centuryIdx == 200:
        centuryNum = 5
    else:
        centuryNum = 3

    # get target year index
    targetYr = (year - century)
    targetYrRem = targetYr % 12
    targetYrDiv = targetYr // 12
    targetRemDiv = targetYrRem // 4

    # add up the 3 and get remainder of 7
    finalNum = centuryNum + targetYrDiv + + targetYrRem + targetRemDiv
    doomsdayIdx = finalNum % 7

    return doomsdayIdx


def get_dotw(date):
    """Takes a date tuple and outputs the DOTW index number"""
    # check for leap year
    leap_year = False
    if date[2] % 4 == 0 and date[2] % 100 != 0:
        leap_year = True
    elif date[2] % 4 == 0 and date[2] % 100 == 0 and date[2] % 400 == 0:
        leap_year = True

    # calculate the differences from the target date and doomsday date
    if date[0] == 1:
        if leap_year:
            difference = date[1] - 4
        else:
            difference = date[1] - 3
    elif date[0] == 2:
        if leap_year:
            difference = date[1] - 29
        else:
            difference = date[1] - 28
    elif date[0] == 3:
        difference = date[1] - 14
    elif date[0] == 4:
        difference = date[1] - 4
    elif date[0] == 5:
        difference = date[1] - 9
    elif date[0] == 6:
        difference = date[1] - 6
    elif date[0] == 7:
        difference = date[1] - 11
    elif date[0] == 8:
        difference = date[1] - 8
    elif date[0] == 9:
        difference = date[1] - 5
    elif date[0] == 10:
        difference = date[1] - 10
    elif date[0] == 11:
        difference = date[1] - 7
    else:
        difference = date[1] - 12

    # get the century index from the other function
    centuryIdx = get_doomsday_dotw(date[2])

    # calculate the date index
    dateIdx = (centuryIdx + difference % 7) % 7

    return dateIdx
