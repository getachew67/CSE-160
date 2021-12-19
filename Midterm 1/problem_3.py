# Problem 4
def first_n_indices(s, target, n):
    '''
    Returns a list of the first n indices where target appears
    in the given string s. Returns an empty list if s does not
    contain the target character or n is 0. Assume target will
    always be a single character and n will be an int >= 0

    Arguments:
       s: an input string to find the first n indices of
       target: a target character. This will always be a single character
       n: an integer limiting how many indices we want to return
       from the function

    Returns: A list a list of the first n indices where target appears
    in the given string s.
    '''
    list_indices = []
    count = 0
    if target not in s:
        return []
    for i in s:
        if i == target:
            if len(list_indices) < n:
                list_indices.append(count)
        count = count + 1
    return list_indices


assert first_n_indices("abcde", "a", 2) == [0]
print(first_n_indices("a-be-c-", "-", 2))
assert first_n_indices("Go ea-ee-ee-ee-ee-ee-ee-sy on me baby~", "g", 2) == []