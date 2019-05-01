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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

txt_incoming_number = texts[0][0]
txt_answering_number = texts[0][1]
txt_time = texts[0][2]

# 97424 22395,90365 06212,01-09-2016 06:03:22
print("First record of texts, {} texts {} at time {}".format(
    txt_incoming_number,
    txt_answering_number,
    txt_time))

call_incoming_number = calls[-1][0]
call_answering_number = calls[-1][1]
call_time = calls[-1][2]
call_duration = calls[-1][3]

# 98447 62998,(080)46304537,30-09-2016 23:57:15,2151
print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(
    call_incoming_number,
    call_answering_number,
    call_time,
    call_duration))

