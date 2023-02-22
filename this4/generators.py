import math
# Create a generator that generates the squares of numbers up to some number N.

def square_gen(max):
    n = 1
    while n <= max:
        yield n ** 2
        n += 1

"""
n = int(input())

for i in square_gen(n):
    print(i)
"""
# Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.

def even_gen(max):
    n = 1
    while n <= max:
        if n % 2 == 0:
            yield f"{n}, "
        n += 1
"""
n = int(input())
res = ""
for i in even_gen(n):
    res += i
print(res)
"""

# Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.

def custom_gen(max):
    n = 1
    while n <= max:
        if n % 12 == 0:
            yield n
        n += 1

# n = int(input())
# for i in custom_gen(n):
#    print(i)


# Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.
def squares(min, max):
    n = min
    while n <= max:
        yield n ** 2
        n += 1

"""
a = int(input())
b = int(input())
for i in squares(a, b):
    print(i)

"""
# Implement a generator that returns all numbers from (n) down to 0.
def rev_gen(start):
    n = start
    while n >= 0:
        yield n
        n -= 1

n = int(input())

for i in rev_gen(n):
    print(i)



