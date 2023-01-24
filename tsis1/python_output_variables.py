x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#Notice the space character after "Python " and "is ", without them the result would be "Pythonisawesome".

x = 5
y = 10
print(x + y)

"""""
x = 5
y = "John"
print(x + y)
In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:
"""""

x = 5
y = "John"
print(x, y)