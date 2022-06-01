"""
Project 1

Class: CSCI 1913, Spring 2021, Section 10
Professor: Jerald Thomas
Student: Jacynda Alatoma (alato006)
"""


def read_events():
    """read an events csv file and returns a list of 3 element tuples"""
    data = open('events.csv')
    dataList = []
    for line in data:
        # split the csv file into a list of list and removing the commas
        dataList.append(tuple(line.strip().split(",")))

    # change the list of lists to lists of tuples
    resultData = tuple((int(x[0]), int(x[1]), x[2]) for x in dataList)

    return resultData


def compareTup(tup1, tup2):
    """Takes in two lists of dates and returns (T/F) if the dates are greater than or less than each other,
    this is for sorting"""
    if tup1[0] != tup2[0]:
        # check the dates
        return tup1[0] < tup2[0]
    return tup1[1] < tup2[1]


def sort_events(event_list):
    """Takes in the list of events and sorts them by date and return a sorted list of the events (selection sort)"""
    lenList = len(event_list)
    # change tuples to a list so it's easier to manipulate in coding
    eventList = [list(x) for x in event_list]

    # compare the lists from the above function and then switch them if it returns a false
    for i in range(lenList):
        for j in range(i + 1, lenList):
            if not compareTup(eventList[i], eventList[j]):
                temp = eventList[i]
                eventList[i] = eventList[j]
                eventList[j] = temp

    # change the lists to tuples
    eventTup = [tuple(x) for x in eventList]
    return eventTup


def sort_events_fast(event_list):
    """Takes in a list of tuples and sorts them by quick sort and returns a sorted list of tuples"""
    tuples = len(event_list)
    # change the tuples to a list so easier to manipulate
    eventList = [list(x) for x in event_list]
    if tuples < 2:
        return event_list

    curr_pos = 0

    # check the similarity of the lists by using the function defined above
    for i in range(1, tuples):
        if compareTup(eventList[i], eventList[0]):
            # switch the lists if true
            curr_pos += 1
            temp = eventList[i]
            eventList[i] = eventList[curr_pos]
            eventList[curr_pos] = temp

    # this is to switch the first value with current position
    temp = eventList[0]
    eventList[0] = eventList[curr_pos]
    eventList[curr_pos] = temp

    # create left and right partitions using the current position as a split
    left = sort_events_fast(eventList[0:curr_pos])
    right = sort_events_fast(eventList[curr_pos + 1:tuples])

    # merge the two lists together and change back from lists to tuples
    evenL = left + [eventList[curr_pos]] + right
    tupleL = [tuple(x) for x in evenL]
    return tupleL


def compareDates(date1, date2):
    """takes in two lists of dates and returns (T/F) if they are equal to each other"""
    if date1[0] == date2[0] and date1[1] == date2[1]:
        return True
    elif date1[0] != date2[0]:
        return False
    else:
        return False


def higherThan(date1, date2):
    """Takes in two list dates and returns (T/F) for if the one is higher than the other as a month or same month
    but higher date"""
    if date1[0] == date2[0]:
        return date1[1] > date2[1]
    else:
        return date1[0] > date2[0]


def get_events_binary_search(date):
    """Takes a target date and then outputs the events that match that day in a list"""
    # load in the events and sort them using selection sort
    events = read_events()
    sortedEvents = sort_events(events)

    # set min and max
    min = 0
    max = len(sortedEvents) - 1
    # create and event list to store the events
    eventList = []

    while min <= max:
        # set the mid
        mid = (min + max) // 2
        # use the comparison function to see if a date needs to be added to the events list
        if compareDates(date, sortedEvents[mid]):
            eventList.append(sortedEvents[mid][2])
            sortedEvents.remove(sortedEvents[mid])
            max = len(sortedEvents) - 1
        else:
            # compare the dates and change the max and min if it is lower or higher than the desired date
            if higherThan(sortedEvents[mid], date):
                max = mid - 1
            elif not higherThan(sortedEvents[mid], date):
                min = mid + 1
    return eventList
