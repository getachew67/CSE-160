# Return the sum of the odd ints in the given list. Note: the % "mod"
# operator computes the remainder, e.g. 5 % 2 is 1.

# sum_odds([5, 2, 6, 3, 4]) → 8
# sum_odds([3, 6, 11, 2, 5]) → 19
# sum_odds([]) → 0

x = [5, 2, 6, 3, 4]

def sum_odds(x):
    print(sum(num for num in x if num % 2 == 1))

