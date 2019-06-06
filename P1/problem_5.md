Problem 5: Blockchain
------------

A Blockchain is a sequential chain of records, similar to a linked list. Each block contains some information and how 
it is connected related to the other blocks in the chain. Each block contains a cryptographic hash of the previous block, 
a timestamp, and transaction data. For this blockchain I used a SHA-256 hash, the Greenwich Mean Time (GMT) when the 
block was created, and text strings as the data.

This operates as a Linked List and only "inserts" at the head which is Θ(1).
(additional operations would vary)