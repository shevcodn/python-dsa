def max_depth(lst):
    if not isinstance(lst, list):
        return 0
    elif not lst:
        return 1
    else:
        return 1 + max(max_depth(item) for item in lst)
    
print(max_depth([1, 2, 3]))
print(max_depth([1, [2, 3]]))
print(max_depth([[1, 2], [3, 4]]))
print(max_depth([[1, 2], [3, 4]]))
