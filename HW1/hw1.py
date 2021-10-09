# Name: Agnes Li
# CSE 160
# Autumn 2021
# Homework 1

import math

# Problem 1
print("Problem 1 solution follows:")

a = 3
b = -5.86
c = 2.5408
root1 = (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)
root2 = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)

print("Root 1: " + str(root1))
print("Root 2: " + str(root2))
print()

# Problem 2
print("Problem 2 solution follows:")

j = 10
for x in range(2, j + 1):
    print("1/" + str(x) + ": " + str(1 / x))
print()
# Problem 3
print("Problem 3 solution follows:")

n = 10
triangular = 0
for i in range(1, n + 1):
    triangular = triangular + i
print("Triangular number", n, "via loop:", triangular)
print("Triangular number", n, "via formula:", n * (n + 1) / 2)
print()

# Problem 4
print("Problem 4 solution follows:")

n = 10
factorial = 1
for i in range(1, n + 1):
    factorial = factorial * i
print("10!: " + str(factorial))
print()

# Problem 5
print("Problem 5 solution follows:")

n = 10
for x in range(n, 0, -1):
    factorial = 1
    for i in range(1, x + 1):
        factorial = factorial * i
    print(str(x) + "!: " + str(factorial))
print()

# Problem 6
print("Problem 6 solution follows:")

n = 10
total = 1
for x in range(1, n + 1):
    factorial = 1
    for i in range(1, x + 1):
        factorial = factorial * i
    fraction = 1 / factorial
    total = total + fraction
print("e: " + str(total))
print()

# Collaboration

# Thanks to my dad for helping me think about tackling programming problems :)
