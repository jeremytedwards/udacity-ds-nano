"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

calls_made = [(row[0], row[3]) for row in calls]
calls_received = [(row[1], row[3]) for row in calls]
all_calls = calls_made + calls_received


def total_call_durations(list_of_calls):
    """

    Takes a list to tuples and creates a unique set of tuples where tuple[0] is the caller
    phone number and tuple[1] is the total of callers total duration in seconds.

    :param list_of_calls:
    :return returns a list of unique calls with call times totaled:
    """
    dict_of_calls = {}
    for tup in list_of_calls:
        total_duration = int(tup[1]) + int(dict_of_calls.get(tup[0], 0))
        dict_of_calls[tup[0]] = total_duration
    return list(dict_of_calls.items())


# sort the calls by duration descending and unpack the top tuple
telephone_number, total_time = sorted(total_call_durations(all_calls),
                                      key=lambda x: x[1], reverse=True)[0]

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(
    telephone_number, total_time))
