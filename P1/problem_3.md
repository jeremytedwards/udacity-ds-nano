Problem 3: Huffman Coding
------------

A Huffman Coding is method of compressing by computing an optimal number of bits for a 
given input taking advantage of frequency of each input. In our case we're working with 
strings.

The steps to accomplish this were:
 
 Encoding:
 1. Build list of tuples representing the frequency of each character, using Python 
 collections.counter(), with uses the subclass of dict. _Constructing it is usually O(n)_.
 2. Sort the list and convert to a list representation of a binary tree, frequencies(total)
 as the nodes and frequency + characters at the leaves. 
 3. Following that trim the frequencies and assigned the codes by walking the object.
 "0" for left and "1" for right.

_(If the symbols are sorted by probability, there is a linear-time O(n) method to 
create the Huffman tree, O(log n) average lookup)_

 Decoding:
 1. Take the tree representation and the frequency bits and walk the tree till a character
 is found, starting over after each find. _O(log n) average lookup_.


