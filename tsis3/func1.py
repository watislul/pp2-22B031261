from itertools import permutations
import random
# functions folder exercises
# 1 task
# def grammToOunce():
#     ounce = gramm / 28.349
#     print(ounce)

# gramm = int(input())
# grammToOunce()
# 2 task
# def farToCel():
#     cel = (5/9) * (far - 32)
#     print(int(cel))

# far = int(input())
# farToCel()
# 3 task
# def solve(numheads, numlegs):
#     num_chicks = 0
#     num_rabbits = 0
#     for i in range(1, numheads + 1):
#         num_chicks = i
#         num_rabbits = numheads - i
#         if(num_chicks * 2 + num_rabbits * 4 == numlegs):
#             break
#     print(f"Number of rabbits = {num_rabbits} and Number of chicks = {num_chicks}")
# solve(35, 94)
# 4 task
# def getPrime():
#     for i in nums:
#         c = 0
#         for j in range(1, i):
#             if i % j == 0:
#                 c += 1
#         if c == 1:
#             pnums.append(i)
#     print(pnums)

# nums = []
# pnums = []
# rang = int(input())
# for i in range (rang):
#     nums.append(int(input()))

# getPrime()
# 5 task
# def strPermut():
#     word = input()
#     perm = permutations(word)
#     for i in list(perm):
#         print(i)

# strPermut()
# 6 task
# def wordRev():
#     word = input()
#     a = word.split()
#     a = list(a)
#     a.reverse()
#     x = ' '.join(a)
#     print(x)

# wordRev()

# task 7
# def has_33(nums):
#    for i in range(len(nums) - 1 ):
#       if nums[i] == 3 and nums[i + 1] == 3:
#          return True
#       elif nums[i] == 3 and nums[i + 1] != 3:
#          return False


# print(has_33([3, 3, 1]))
# print(has_33([1, 1, 3, 3]))
# print(has_33([1, 3, 1]))
# task 8
# def spy_game(nums):
#     for i in range(len(nums) - 2):
#         if nums[i] == 0 and nums[i + 1] == 0 and nums[i + 2] == 7:
#             return True
#         elif nums[i] == 0 and nums[i + 1] != 0:
#             return False
#         elif nums[i] == 0 and nums[i + 1] == 0 and nums[i + 2] != 7:
#             return False

# print(spy_game([1,2,4,0,0,7,5]))
# print(spy_game([1,0,2,4,0,5,7]))
# print(spy_game([1,7,2,0,4,5,0]))

# task 9

# def sphereVol():
#     vol = lambda r: (4/3) * 3.14 * pow(r, 3)
#     print(vol(rad))


# rad = int(input())
# sphereVol()

# task 10

# def uni_list():
#     for i in range(len(nums)):
#         unums.append(nums[i])
#         if nums[i] == nums[i - 1]:
#             unums.pop()

#     print(unums)

# x = int(input())
# nums = []
# unums = []
# for i in range(x):
#     nums.append(int(input()))

# uni_list()

# task 11

# def isPal():
#     if word == word[::-1]:
#         return True
#     else:
#         return False


# word = input()

# print(isPal())

# task 12

# def histogram(nums):
#     curr = '*'
#     for val in nums:
#         if val != 0:
#             curr = curr * val
#         else:
#             curr = ''
#         print(curr)
#         curr = '*'

# histogram([4, 9, 7])

# task 13

# def game():
#     name = input("Hello! What is your name? \n")
#     guess = 0
#     num = 0
#     gnum = random.randint(1, 20)
#     print("Well, {fname}, I am thinking of a number between 1 and 20.\nTake a guess.".format(fname = name))
#     while num != gnum:
#         num = int(input())
#         if num < gnum:
#             guess += 1
#             print("Your guess is too low.\nTake a guess.")
#         elif num > gnum:
#             guess += 1
#             print("Your guess is too big.\nTake a guess.")
#         elif guess == 3:
#             print("You're out of guesses, try again")
#         else:
#             guess +=1
#             print("Good job, {fname}! You guessed my number in {fguess} guesses!".format(fname = name, fguess = guess))
#             break
# game()