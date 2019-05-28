# coding=utf-8

import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    results = []
    if path is None:
        results = None
    else:
        for pth in os.listdir(path):
            p = os.path.join(path, pth)
            if os.path.isdir(p):
                not_empty = find_files(suffix, p)
                if not_empty:
                    results.append(not_empty.pop())
            elif os.path.isfile(p):
                if p.endswith(suffix):
                    results.append(p)

    return results


# Empty directory returns ?
print(find_files(".c", None))

# Empty directory returns []
print(find_files(".c", "./test"))

# Sample directory returns
# ['./testdir/subdir3/subsubdir1/b.c',
# './testdir/t1.c',
# './testdir/subdir5/a.c',
# './testdir/subdir1/a.c']
print(find_files(".c", "./testdir"))
