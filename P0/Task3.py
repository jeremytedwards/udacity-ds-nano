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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>

The list of codes should be print out one per line in lexicographic order 
with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."

The percentage should have 2 decimal digits
"""

# (04344)228249 - Fixed line
# (080)62164823 - Fixed line, Bangalore (080)
# 78290 99865 - Mobile numbers, prefix = 7829
# 1408371942 - Telemarketers starts with 140

# Part A:
# To number, from Bangalore fixed line

codes_fm_080 = []
total_fm_080 = 0
total_to_and_fm_080 = 0


for line in calls:
    if line[0].startswith("(08"):
        total_fm_080 += 1
        # ternary:? if the call from number contains ")", split + ")",
        # else split on " " taking the first item in either case (area code)
        area_code = (line[1].split(" ")[0], line[1].split(")")[0]+")")[")" in line[1]]
        codes_fm_080.append(area_code)
        if line[1].startswith("(08"):
            total_to_and_fm_080 += 1


print("The numbers called by people in Bangalore have codes:")
print(*sorted(set(codes_fm_080)), sep="\n")


# Part B:
# Percentage from fixed line to fixed line on (080)
# print(total_fm_080, "/", total_to_and_fm_080, "=", total_fm_080/total_to_and_fm_080)

percentage = (total_fm_080/total_to_and_fm_080)

print("\n")
print("{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed "
      "lines in Bangalore.".format(percentage))
