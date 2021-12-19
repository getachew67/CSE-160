# Name: Agnes Li
# CSE 160
# Autumn 2021
# Midterm Exam


# Problem 1
def check_same_parity(nums_lst):
    '''
    Takes in a list of lists of integers and returns True if every number
    in each sublist has the same parity. Otherwise, the function should
    return False. Assume that nums_lst is not empty and each sublist
    contains at least one integer.

    Arguments:
        nums_lst: a list of lists of integers.

    Returns: a boolean value indicating if all numbers in each sublist
    shares the same parity
    '''
    def is_row_even(row):
        remainders = sum(i % 2 for i in row)
        if remainders != 0:
            return False
        return True

    def is_row_odd(row):
        remainders = sum(i % 2 for i in row)
        if remainders != len(row):
            return False
        return True

    for row in nums_lst:
        if not is_row_even(row) and not is_row_odd(row):
            return False
    return True


assert check_same_parity([[3, 9, 7], [2, 4], [1]]) is True
assert check_same_parity([[2, 4], [3, 4, 5]]) is False


# Problem 2
def max_nucleotide_freq(frequency_list):
    '''
    Takes a list of lists containing a unique nucleotide and its frequency
    in a dataset. Returns a string describing the valid nucleotide (A, C, T, G)
    with the highest frequency and its associated frequency. Assume there is
    at least one pair that has both a valid nucleotide base and frequency >= 1

    Arguments:
        frequency_list: a list of lists, where each list has a nucleotide
        base as a string in the first index, and the frequency of that
        base as an integer in the second index

    Returns: "{base} has {max frequency} occurrences!", where {base} represents
    the nucleotide base with the max frequency
    Return "No data!" if frequency_list is empty.
    '''
    highest_freq = 0
    base = ""
    for i in frequency_list:
        if i[0] == "A" or "G" or "C" or "T":
            if i[1] > highest_freq:
                highest_freq = i[1]
                base = i[0]
    if len(frequency_list) == 0:
        return "No data!"
    return str(base) + " has " + str(highest_freq) + " occurrences!"


assert max_nucleotide_freq([['A', 2], ['G', 6], ['C', 20]]) ==\
     "C has 20 occurrences!"
assert max_nucleotide_freq([['A', 14], ['G', 6]]) ==\
     "A has 14 occurrences!"
assert max_nucleotide_freq([['A', 1]]) == "A has 1 occurrences!"


# Problem 3
def find_activity(weather):
    '''
    Takes in a string that represents a weather condition.
    Returns the corresponding activity as a string.

    Arguments:
        weather: a string representing the current weather

    Returns: A string representing the appropriate activity to participate in
    '''
    if 'sunny' in weather:
        return "play tennis"
    elif 'cloudy' in weather:
        return "do homework"
    elif 'rainy' in weather:
        return "make food"
    else:
        return "take a nap"


assert find_activity("sunny") == "play tennis"
assert find_activity("cloudy") == "do homework"
assert find_activity("rainy") == "make food"


def create_schedule(forecast):
    '''
    Takes in a forecast that is a list of weather predictions.
    Returns a list of strings representing an appropriate schedule
    given the forecast.

    Arguments:
        forecast: a non-empty list of strings representing upcoming
        weather forecasts

    Returns: A list of strings representing appropriate activities for each
    weather condition
    '''
    schedule = []
    for i in forecast:
        schedule.append(find_activity(i))
    return schedule


assert create_schedule(["cloudy", "still cloudy", "sunny", "drizzly",
                        "rainy"]) == ["do homework", "do homework",
                                      "play tennis", "take a nap", "make food"]
assert create_schedule(["super sunny", "considerably cloudy"]) ==\
     ["play tennis", "do homework"]


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
assert first_n_indices("a-be-c-", "-", 2) == [1, 4]
assert first_n_indices("Go ea-ee-ee-ee-ee-ee-ee-sy on me baby~", "g", 2) == []


# Problem 5
def squash_in_half(grid):
    '''
    Takes in a grid that is a list of lists of integers representating a
    rectangular grid. Returns a new 'squashed' version of the given grid,
    where every two consecutive rows in the original grid have been
    combined into a single row in the output grid. Assume grid and its sublists
    are all non-empty.

    Arguments:
        grid: a list of lists representating a rectangular grid.

    Returns: a list of lists representing a squashed grid
    '''
    new_list = []
    if len(grid) % 2 == 0:
        toSubtract = 0
    else:
        toSubtract = 1
    for i in range(0, len(grid) - toSubtract, 2):
        toAppend = []
        for j in range(0, len(grid[i])):
            toAppend.append(grid[i][j] + grid[i + 1][j])
        new_list.append(toAppend)
    if toSubtract == 1:
        new_list.append(grid[len(grid) - 1])
    return new_list


assert squash_in_half([[1, 1], [0, 1], [0, 1], [2, 2]]) == [[1, 2], [2, 3]]
assert squash_in_half([[-1, 0], [0, 1], [3, 2]]) == [[-1, 1], [3, 2]]


# ANSWER the following questions as COMMENTS

# (1 pt) Did you work on this quiz alone or collaborate with others?
# Alone.


# If you collaborated with others, list full names and UWNetIDs
# of everyone you collaborated with.
