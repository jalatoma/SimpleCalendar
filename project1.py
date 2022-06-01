"""
Project 1

Class: CSCI 1913, Spring 2021, Section 10
Professor: Jerald Thomas
Student: Jacynda Alatoma (alato006)
"""
from project1_dotw import get_dotw
from project1_events import get_events_binary_search


def validate_input(date_string):
    """Takes in a date string and sees if it is a valid date input, returns a tuple with the same date"""
    # checks for a valid input of a date, just counted the amount of digits entered return None if wrong or empty
    digitCount = 0
    for character in date_string:
        if character.isdigit():
            digitCount += 1
    if 6 <= digitCount <= 8:
        # split the date into a list to reference later in if statements
        split = date_string.split("-", 2)
        map_object = map(int, split)
        date = list(map_object)
        # make sure the first number is a valid month
        if 12 >= date[0] > 0:
            # check for valid days in the months with 31 days
            if date[0] == 1 or date[0] == 3 or date[0] == 5 or date[0] == 7 or date[0] == 8 or date[0] == 10 or \
                    date[0] == 12:
                if 31 < date[1] or date[1] <= 0:
                    return None
                if date[2] < 1000:
                    return None
                # return a tuple if everything is correct
                else:
                    date_tuple = (date[0], date[1], date[2])
                    return date_tuple
            # check months with 30 days
            if date[0] == 4 or date[0] == 6 or date[0] == 9 or date[0] == 11:
                if 30 < date[1] or date[1] <= 0:
                    return None
                if date[2] < 1000:
                    return None
                else:
                    date_tuple = (date[0], date[1], date[2])
                    return date_tuple
            # check for leap years
            if date[0] == 2 and date[2] % 4 == 0 and date[2] % 100 != 0:
                if 29 < date[1] or date[1] <= 0:
                    return None
                if date[2] < 1000:
                    return None
                else:
                    date_tuple = (date[0], date[1], date[2])
                    return date_tuple
            # check for more leap years
            if date[0] == 2 and date[2] % 4 == 0 and date[2] % 100 == 0 and date[2] % 400 == 0:
                if 29 < date[1] or date[1] <= 0:
                    return None
                if date[2] < 1000:
                    return None
                else:
                    date_tuple = (date[0], date[1], date[2])
                    return date_tuple
            # check for leap years
            if date[0] == 2 and date[2] % 4 != 0 or (date[2] % 4 == 0 and date[2] % 100 == 0):
                if 28 < date[1] or date[1] <= 0:
                    return None
                if date[2] < 1000:
                    return None
                else:
                    date_tuple = (date[0], date[1], date[2])
                    return date_tuple
        return None  # return None for if everything checked does not fit what I want
    return None


def next_date(date):
    """takes in a date and outputs the next date as a tuple"""
    # changed the tuple to a list
    dateList = list(date)
    leap_year = False

    # checks for a leap year
    if dateList[2] % 4 == 0 and dateList[2] % 100 != 0:
        leap_year = True
    elif dateList[2] % 4 == 0 and dateList[2] % 100 == 0 and dateList[2] % 400 == 0:
        leap_year = True

    # next day of months with 31 days
    if dateList[0] == 1 or dateList[0] == 3 or dateList[0] == 5 or dateList[0] == 7 or dateList[0] == 8 or \
            dateList[0] == 10:
        if 31 > dateList[1] > 0:
            dateList[1] += 1
            nextDay = (dateList[0], dateList[1], dateList[2])
            return nextDay
        elif dateList[1] == 31:
            dateList[1] = 1
            dateList[0] += 1
            nextDay = (dateList[0], dateList[1], dateList[2])
            return nextDay
    # next day for the month of february with leap and non leap years
    elif dateList[0] == 2 and leap_year:
        if 29 > dateList[1] > 0:
            dateList[1] += 1
            nextDay = (dateList[0], dateList[1], dateList[2])
            return nextDay
        elif dateList[1] == 29:
            dateList[1] = 1
            dateList[0] = 3
            nextDay = (dateList[0], dateList[1], dateList[2])
            return nextDay
    elif dateList[0] == 2 and not leap_year:
        if 28 > dateList[1] > 0:
            dateList[1] += 1
            nextDay = (dateList[0], dateList[1], dateList[2])
            return nextDay
        elif dateList[1] == 28:
            dateList[1] = 1
            dateList[0] = 3
            nextDay = (dateList[0], dateList[1], dateList[2])
            return nextDay
    # next day with months with 30 days
    elif dateList[0] == 4 or dateList[0] == 6 or dateList[0] == 9 or dateList[0] == 11:
        if 30 > dateList[1] > 0:
            dateList[1] += 1
            nextDay = (dateList[0], dateList[1], dateList[2])
            return nextDay
        elif dateList[1] == 30:
            dateList[1] = 1
            dateList[0] = 3
            nextDay = (dateList[0], dateList[1], dateList[2])
            return nextDay
    # next day for the month of december since year has to change
    else:
        if dateList[1] == 31:
            dateList[0] = 1
            dateList[1] = 1
            dateList[2] += 1
            nextDay = (dateList[0], dateList[1], dateList[2])
            return nextDay
        else:
            dateList[1] += 1
            nextDay = (dateList[0], dateList[1], dateList[2])
            return nextDay
    return None


def previous_date(date):
    """Takes in a date as a tuple and outputs the previous day as a tuple"""
    # changes tuple to a list so can be modified
    dateList = list(date)
    # checks for a leap year
    leap_year = False
    if dateList[2] % 4 == 0 and dateList[2] % 100 != 0:
        leap_year = True
    elif dateList[2] % 4 == 0 and dateList[2] % 100 == 0 and dateList[2] % 400 == 0:
        leap_year = True

    # checks for january just in case year needs to be modified
    if dateList[0] == 1:
        if dateList[1] == 1:
            dateList[0] = 12
            dateList[2] -= 1
            dateList[1] = 31
            previousDay = (dateList[0], dateList[1], dateList[2])
            return previousDay
        else:
            dateList[1] -= 1
            previousDay = (dateList[0], dateList[1], dateList[2])
            return previousDay
    # previous day for months whose previous months have 31 days
    elif dateList[0] == 2 or dateList[0] == 4 or dateList[0] == 6 or dateList[0] == 8 or dateList[0] == 9 or \
            dateList[0] == 11:
        if dateList[1] == 1:
            dateList[1] = 31
            dateList[0] -= 1
            previousDay = (dateList[0], dateList[1], dateList[2])
            return previousDay
        else:
            dateList[1] -= 1
            previousDay = (dateList[0], dateList[1], dateList[2])
            return previousDay
    # previous day for march on leap and non leap years
    elif dateList[0] == 3 and leap_year:
        if dateList[1] == 1:
            dateList[1] = 29
            dateList[0] = 2
            previousDay = (dateList[0], dateList[1], dateList[2])
            return previousDay
        else:
            dateList[1] -= 1
            previousDay = (dateList[0], dateList[1], dateList[2])
            return previousDay
    elif dateList[0] == 3 and not leap_year:
        if dateList[1] == 1:
            dateList[1] = 28
            dateList[0] -= 1
            previousDay = (dateList[0], dateList[1], dateList[2])
            return previousDay
        else:
            dateList[1] -= 1
            previousDay = (dateList[0], dateList[1], dateList[2])
            return previousDay
    # previous day for months whose previous month has 30 days
    elif dateList[0] == 5 or dateList[0] == 7 or dateList[0] == 10 or dateList[0] == 12:
        if dateList[1] == 1:
            dateList[1] = 30
            dateList[0] -= 1
            previousDay = (dateList[0], dateList[1], dateList[2])
            return previousDay
        else:
            dateList[1] -= 1
            previousDay = (dateList[0], dateList[1], dateList[2])
            return previousDay
    return None


def month(date):
    """takes in a date tuple and returns the string of the month"""
    # checking the month of the inputted tuple
    if date[0] == 1:
        return "January"
    elif date[0] == 2:
        return "February"
    elif date[0] == 3:
        return "March"
    elif date[0] == 4:
        return "April"
    elif date[0] == 5:
        return "May"
    elif date[0] == 6:
        return "June"
    elif date[0] == 7:
        return "July"
    elif date[0] == 8:
        return "August"
    elif date[0] == 9:
        return "September"
    elif date[0] == 10:
        return "October"
    elif date[0] == 11:
        return "November"
    else:
        return "December"


def printDate(sun, sunEvents, mon, monEvents, tues, tuesEvents, wed, wedEvents, thurs, thursEvents, fri, friEvents, sat,
              satEvents):
    """Takes in every day of the week and the events and prints the format for the calendar"""
    # calculate the month for each tuple
    sunmonth = month(sun)
    monmonth = month(mon)
    tuesmonth = month(tues)
    wedmonth = month(wed)
    thursmonth = month(thurs)
    frimonth = month(fri)
    satmonth = month(sat)

    # print in the format as in README and check for events/print them if there is any
    print("Sunday, " + sunmonth + " " + str(sun[1]))
    if not sunEvents:
        print("- No events")
    else:
        for event in sunEvents:
            print("- " + event)
    print("Monday, " + monmonth + " " + str(mon[1]))
    if not monEvents:
        print("- No events")
    else:
        for event in monEvents:
            print("- " + event)
    print("Tuesday, " + tuesmonth + " " + str(tues[1]))
    if not tuesEvents:
        print("- No events")
    else:
        for event in tuesEvents:
            print("- " + event)
    print("Wednesday, " + wedmonth + " " + str(wed[1]))
    if not wedEvents:
        print("- No events")
    else:
        for event in wedEvents:
            print("- " + event)
    print("Thursday, " + thursmonth + " " + str(thurs[1]))
    if not thursEvents:
        print("- No events")
    else:
        for event in thursEvents:
            print("- " + event)
    print("Friday, " + frimonth + " " + str(fri[1]))
    if not friEvents:
        print("- No events")
    else:
        for event in friEvents:
            print("- " + event)
    print("Saturday, " + satmonth + " " + str(sat[1]))
    if not satEvents:
        print("- No events")
    else:
        for event in satEvents:
            print("- " + event)


def main():
    # check for valid input and get the dotw
    print("Enter a date:")
    date = input()
    dateTuple = validate_input(date)
    dayoftw = get_dotw(dateTuple)
    # depending on the day of the week, calculate other days using functions we wrote, then use the print function we
    # wrote to print the weekly calendar in the format we want
    if dayoftw == 0:
        sun = dateTuple
        sunEvents = get_events_binary_search(sun)
        mon = next_date(sun)
        monEvents = get_events_binary_search(mon)
        tues = next_date(mon)
        tuesEvents = get_events_binary_search(tues)
        wed = next_date(tues)
        wedEvents = get_events_binary_search(wed)
        thurs = next_date(wed)
        thursEvents = get_events_binary_search(thurs)
        fri = next_date(thurs)
        friEvents = get_events_binary_search(fri)
        sat = next_date(fri)
        satEvents = get_events_binary_search(sat)
        printDate(sun, sunEvents, mon, monEvents, tues, tuesEvents, wed, wedEvents, thurs, thursEvents, fri, friEvents,
                  sat,
                  satEvents)
    elif dayoftw == 1:
        mon = dateTuple
        monEvents = get_events_binary_search(mon)
        sun = previous_date(mon)
        sunEvents = get_events_binary_search(sun)
        tues = next_date(mon)
        tuesEvents = get_events_binary_search(tues)
        wed = next_date(tues)
        wedEvents = get_events_binary_search(wed)
        thurs = next_date(wed)
        thursEvents = get_events_binary_search(thurs)
        fri = next_date(thurs)
        friEvents = get_events_binary_search(fri)
        sat = next_date(fri)
        satEvents = get_events_binary_search(sat)
        printDate(sun, sunEvents, mon, monEvents, tues, tuesEvents, wed, wedEvents, thurs, thursEvents, fri, friEvents,
                  sat,
                  satEvents)
    elif dayoftw == 2:
        tues = dateTuple
        tuesEvents = get_events_binary_search(tues)
        mon = previous_date(tues)
        monEvents = get_events_binary_search(mon)
        sun = previous_date(mon)
        sunEvents = get_events_binary_search(sun)
        wed = next_date(tues)
        wedEvents = get_events_binary_search(wed)
        thurs = next_date(wed)
        thursEvents = get_events_binary_search(thurs)
        fri = next_date(thurs)
        friEvents = get_events_binary_search(fri)
        sat = next_date(fri)
        satEvents = get_events_binary_search(sat)
        printDate(sun, sunEvents, mon, monEvents, tues, tuesEvents, wed, wedEvents, thurs, thursEvents, fri, friEvents,
                  sat,
                  satEvents)
    elif dayoftw == 3:
        wed = dateTuple
        wedEvents = get_events_binary_search(wed)
        tues = previous_date(wed)
        tuesEvents = get_events_binary_search(tues)
        mon = previous_date(tues)
        monEvents = get_events_binary_search(mon)
        sun = previous_date(mon)
        sunEvents = get_events_binary_search(sun)
        thurs = next_date(wed)
        thursEvents = get_events_binary_search(thurs)
        fri = next_date(thurs)
        friEvents = get_events_binary_search(fri)
        sat = next_date(fri)
        satEvents = get_events_binary_search(sat)
        printDate(sun, sunEvents, mon, monEvents, tues, tuesEvents, wed, wedEvents, thurs, thursEvents, fri, friEvents,
                  sat,
                  satEvents)
    elif dayoftw == 4:
        thurs = dateTuple
        thursEvents = get_events_binary_search(thurs)
        wed = previous_date(thurs)
        wedEvents = get_events_binary_search(wed)
        tues = previous_date(wed)
        tuesEvents = get_events_binary_search(tues)
        mon = previous_date(tues)
        monEvents = get_events_binary_search(mon)
        sun = previous_date(mon)
        sunEvents = get_events_binary_search(sun)
        fri = next_date(thurs)
        friEvents = get_events_binary_search(fri)
        sat = next_date(fri)
        satEvents = get_events_binary_search(sat)
        printDate(sun, sunEvents, mon, monEvents, tues, tuesEvents, wed, wedEvents, thurs, thursEvents, fri, friEvents,
                  sat,
                  satEvents)
    elif dayoftw == 5:
        fri = dateTuple
        friEvents = get_events_binary_search(fri)
        thurs = previous_date(fri)
        thursEvents = get_events_binary_search(thurs)
        wed = previous_date(thurs)
        wedEvents = get_events_binary_search(wed)
        tues = previous_date(wed)
        tuesEvents = get_events_binary_search(tues)
        mon = previous_date(tues)
        monEvents = get_events_binary_search(mon)
        sun = previous_date(mon)
        sunEvents = get_events_binary_search(sun)
        sat = next_date(fri)
        satEvents = get_events_binary_search(sat)
        printDate(sun, sunEvents, mon, monEvents, tues, tuesEvents, wed, wedEvents, thurs, thursEvents, fri, friEvents,
                  sat,
                  satEvents)
    else:
        sat = dateTuple
        satEvents = get_events_binary_search(sat)
        fri = previous_date(sat)
        friEvents = get_events_binary_search(fri)
        thurs = previous_date(fri)
        thursEvents = get_events_binary_search(thurs)
        wed = previous_date(thurs)
        wedEvents = get_events_binary_search(wed)
        tues = previous_date(wed)
        tuesEvents = get_events_binary_search(tues)
        mon = previous_date(tues)
        monEvents = get_events_binary_search(mon)
        sun = previous_date(mon)
        sunEvents = get_events_binary_search(sun)
        printDate(sun, sunEvents, mon, monEvents, tues, tuesEvents, wed, wedEvents, thurs, thursEvents, fri, friEvents,
                  sat,
                  satEvents)


if __name__ == "__main__":
    main()