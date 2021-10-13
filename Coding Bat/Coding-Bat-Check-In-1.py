# Return the sum of the odd ints in the given list. Note: the % "mod"
# operator computes the remainder, e.g. 5 % 2 is 1.

# sum_odds([5, 2, 6, 3, 4]) → 8
# sum_odds([3, 6, 11, 2, 5]) → 19
# sum_odds([]) → 0


def sum_odds(nums):
    return sum(num for num in nums if num % 2 == 1)


# Returns True if int hidden_num is found in the given array.
# contains_hidden([5, 2, 6, 3, 4], 3) → True
# contains_hidden([3, 6, 11, 2, 5], 19) → False
# contains_hidden([3, 6, 11, 2, 5], 5) → True


def contains_hidden(nums, hidden_num):
    for num in nums:
        if num == hidden_num:
            return True
    return False


# could also just do "return hidden_num in nums"

# Return the number of times the letter z occurs in the given string.
# count_z('lazy') → 1
# count_z('really lazzzy') → 3
# count_z('') → 0

def count_z(input_str):
    count = 0
    for letter in input_str:
        if letter == "z":
            count = count + 1
    return count
