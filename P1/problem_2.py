# coding=utf-8

import os

# os.path.isdir(path)
# os.path.isfile(path)
# os.listdir(directory)
# os.path.join(...)


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
    if not os.listdir(path):
        results.append("")
        # yield ""
    else:
        for pth in os.listdir(path):
            p = os.path.join(path, pth)
            if os.path.isdir(p):
                find_files(suffix, p)
                # yield find_files(suffix, p)
            elif os.path.isfile(p):
                if p.endswith(suffix):
                    results.append(p)
                    # yield p
    return results


# files_with_suffix = [].append(find_files(".c", "./testdir"))

files_with_suffix = find_files(".c", "./testdir")

# files_with_suffix = [match for match in find_files(".c", "./testdir") if match is not ""]

print(files_with_suffix)

# Empty directory returns ?
# print(find_files(".c", None))

# Empty directory returns []
# print(find_files(".c", "./test"))

# Full directory returns []
# print(find_files(".c", "./testdir"))
