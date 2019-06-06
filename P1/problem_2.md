Problem 2: File Recursion
------------

Find all files beneath path with file name suffix.

Note that a path may contain further subdirectories and those subdirectories may also contain further subdirectories.

There are no limit to the depth of the subdirectories can be.

The program has to walk the entire directory to get the results so O(n) complexity.

Args:

      suffix(str): suffix if the file name to be found
      path(str): path of the file system

Returns:

       a list[] of paths
       
