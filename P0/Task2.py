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
all_calls = []


def process_list_of_calls(list_of_calls):
    dict_of_calls = {}
    for tup in list_of_calls:
        total_duration = int(tup[1]) + int(dict_of_calls.get(tup[0], 0))
        dict_of_calls[tup[0]] = str(total_duration)
    holder = list(dict_of_calls)
    return holder

all_calls.append(process_list_of_calls(calls_made))
all_calls.append(process_list_of_calls(calls_received))

hold = set(all_calls)
# telephone_number, total_time = sorted(set(all_calls, 1))

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(
    telephone_number, total_time))
