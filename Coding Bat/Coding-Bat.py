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

# The squirrels in Palo Alto spend most of the day playing.
# In particular, they play if the temperature is between 60 and 90 (inclusive).
# Unless it is summer, then the upper limit is 100 instead of 90.
# Given an int temperature and a boolean is_summer,
# return True if the squirrels play and False otherwise.


# squirrel_play(70, False) → True
# squirrel_play(95, False) → False
# squirrel_play(95, True) → True

def squirrel_play(temp, is_summer):
    if temp >= 60 and temp <= 100 and is_summer is True:
        return True
    elif temp >= 60 and temp <= 90 and is_summer is False:
        return True
    else:
        return False


# You are driving a little too fast, and a police officer stops you.
# Write code to compute the result, encoded as an int value:
# 0=no ticket, 1=small ticket, 2=big ticket.
# If speed is 60 or less, the result is 0.
# If speed is between 61 and 80 inclusive,
# the result is 1. If speed is 81 or more, the result is 2.
# Unless it is your birthday --
# on that day, your speed can be 5 higher in all cases.


# caught_speeding(60, False) → 0
# caught_speeding(65, False) → 1
# caught_speeding(65, True) → 0

def caught_speeding(speed, is_birthday):
    if speed <= 60:
        return 0
    elif speed >= 61 and speed <= 80 and is_birthday is False:
        return 1
    elif speed >= 81 and is_birthday is False:
        return 2
    elif speed <= 65 and is_birthday is True:
        return 0
    elif speed >= 66 and speed <= 85 and is_birthday is True:
        return 1
    elif speed >= 86 and is_birthday is True:
        return 2


# Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat,
# and a boolean indicating if we are on vacation,
# return a string of the form "7:00"
# indicating when the alarm clock should ring.
# Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00".
# Unless we are on vacation -- then on weekdays
# it should be "10:00" and weekends it should be "off".

# alarm_clock(1, False) → '7:00'
# alarm_clock(5, False) → '7:00'
# alarm_clock(0, False) → '10:00'

def alarm_clock(day, vacation):
    if vacation is False:
        if day == 0 or day == 6:
            return "10:00"
        elif day == 1 or day == 2 or day == 3 or day == 4 or day == 5:
            return "7:00"
    elif vacation is True:
        if day == 0 or day == 6:
            return "off"
        elif day == 1 or day == 2 or day == 3 or day == 4 or day == 5:
            return "10:00"
