Problem 1: Square root of the integer
------------
Find the square root of the integer without using any Python library. You have to find the 
floor value of the square root.

For example if the given number is 16, then the answer would be 4.

If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value 
is 5.

The expected time complexity is O(log(n))

https://en.wikipedia.org/wiki/Methods_of_computing_square_roots

Taking advantage of bit shifts we can quickly double (left shift) or half a number (right shift) 
by simply shifting the bits.