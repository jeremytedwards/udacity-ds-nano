"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

# get a list of all the texted FROM phone numbers from the texts file
texts_fm_tel = [item[0] for item in texts]

# get a list of all the texted TO phone numbers from the texts file
texts_to_tel = [item[1] for item in texts]


# get a list of all the dialed FROM phone numbers from the calls file
calls_fm_tel = [item[0] for item in calls]

# get a list of all the dialed TO phone numbers from the calls file
calls_to_tel = [item[1] for item in calls]


# the length of a unique set of these numbers
count = len(set(texts_fm_tel + texts_to_tel + calls_fm_tel + calls_to_tel))

# 570 (517 from numbers only)
print("There are {} different telephone numbers in the records.".format(count))
