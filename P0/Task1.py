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

texts_fm_tel = []
texts_to_tel = []
calls_fm_tel = []
calls_to_tel = []

# get a list of all the texted FROM and TO phone numbers from the texts file list
for item in texts:
    texts_fm_tel.append(item[0])
    texts_to_tel.append(item[1])

# get a list of all the dialed FROM and TO phone numbers from the calls file list
for item in calls:
    calls_fm_tel.append(item[0])
    calls_to_tel.append(item[1])

# the length of a unique set of these numbers
count = len(set(texts_fm_tel + texts_to_tel + calls_fm_tel + calls_to_tel))

# 570 (517 FROM numbers only)
print("There are {} different telephone numbers in the records.".format(count))
