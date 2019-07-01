Problem 6: Union and Intersection
------------

Using a list for our data structure means we have to walk it every time we want 
to learn something so I choose to bear the cost of the time early on, sorting it, and reducing 
to a set so that we could benefit from not having to walk the an entire list for every value we 
wanted to compare. We can benefit from knowing everything smaller has been compared. 

For UNION if there is a long list and a short list we only have to check as many items as the 
shorter list has then handle the remaining.

For INTERSECTION, similarly we just need to check the length of the shorter list, only in this 
case we're done and don't have to handle the remaining list items. 