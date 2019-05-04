Task0 - O(1)
------------

Selection of a item in a list is O(1)

txt_incoming_number : **O(1)**
txt_answering_number : **O(1)** 
txt_time : **O(1)**

Task1 - O(n)
------------

In this Task I walk each list once and collect the numbers then combine 
the lists a get a count of the unique set.

Get a list of all the texted FROM and TO phone numbers from the texts 
file list : **O(n)**

Get a list of all the dialed FROM and TO phone numbers from the calls 
file list: **O(n)**


The length of a unique set of these numbers:

**len = O(1)**

**set = O(n)**


Task2 - O(n log n)
------------

In this task I walked each list once to collect the calls made and 
received then put them in one list. Then I sorted that list by the 
second value of the tuple and grabbed the top pair.

calls_made : **O(n)**

calls_received : **O(n)**

all_calls : **O(1)**

sorted(allcalls) : **O(n log n)**



Task3 - O(n log n)
------------

For this task I walk the list, split and count, so I can answer both 
parts in one pass. Then I create a set of the results to get uniques 
and sort them to satisfy the additional requirements.

for loop : **O(n)**

sorted(set(codes_fm_080))

set() : **O(n)**

sorted() : **O(n log n)**


Task4 - O(n^2)
------------

For this task I gather up a set of outgoing numbers then I remove the 
sets of numbers from it that would negate the outgoing from being a 
telemarketer based on the provided requirement.

set_of_outgoing_numbers = set([row[0] for row in calls])
set_of_incoming_numbers = set([row[1] for row in calls])
set_of_send_text_numbers = set([row[0] for row in texts])
set_of_receive_text_numbers = set([row[1] for row in texts])

For loop : **O(n)**

set() : **O(n)**

Difference operator on lists : **O(n^2)**
(could be faster if lists were sorted subsets)

sorted() : **O(n log n)**

