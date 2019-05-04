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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no 
duplicates.
"""

set_of_outgoing_numbers = set([row[0] for row in calls])
set_of_incoming_numbers = set([row[1] for row in calls])
set_of_send_text_numbers = set([row[0] for row in texts])
set_of_receive_text_numbers = set([row[1] for row in texts])

set_of_numbers = set_of_outgoing_numbers \
                  - set_of_incoming_numbers \
                  - set_of_send_text_numbers \
                  - set_of_receive_text_numbers

print("These numbers could be telemarketers: ")
print(*sorted(set_of_numbers), sep="\n")
