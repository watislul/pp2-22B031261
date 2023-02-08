import math
# classes folder exercises
# task 1
# class Person:
#     def __init__(self):
#         self.word = ""

#     def getString(self):
#         self.word = input()

#     def printString(self):
#         print(self.word.upper())

# word = Person()
# word.getString()
# word.printString()

# task 2

# class Shape:
#     def area(self):
#         print(0)

# class Square(Shape):
#     def __init__(self, length):
#         super().__init__()
#         self.length = length
#     def area(self):
#         print(self.length **2)

# shape = Shape()
# square = Square(5)
# shape.area()
# square.area()

# task 3

# class Shape:
#     def area(self):
#         print(0)

# class Rectangle(Shape):
#     def __init__(self, length, width):
#         super().__init__()
#         self.length = length
#         self.width = width
#     def area(self):
#         print(self.length * self.width)

# rectangle = Rectangle(5, 2)
# rectangle.area()

# task 4

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def getCoordinates(self):
#         print(self.x, self.y)

#     def moveCoordinates(self, x, y):
#         self.x += x
#         self.y += y

#     def dist(self, point):
#         return math.sqrt((self.x - point.x) **2 + (self.y - point.y) **2)

# p1 = Point(2, 3)
# p2 = Point(3, 4)
# p1.getCoordinates()
# p2.getCoordinates()
# print(p1.dist(p2))
# p1.moveCoordinates(2, 2)
# p1.getCoordinates()

# task 5
# class Account():
#     def __init__(self, owner):
#         self.owner = owner
#         self.balance = 0

#     def checkBal(self):
#         print(f"Balance is {self.balance}")

#     def deposit(self, amount):
#         self.balance += amount
#         print(f"{amount} has been deposited")

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Not enough money on balance")
#         else:
#             self.balance -= amount
#             print(f"{amount} has been withdrawn from deposit")

# own1 = Account("Anuar")

# own1.checkBal()
# own1.deposit(5000)
# own1.checkBal()
# own1.withdraw(2000)
# own1.checkBal()