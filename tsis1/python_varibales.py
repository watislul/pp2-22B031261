x = 4       # x is of type int
x = "Sally"  # x is now of type str
print(x)

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x, '\n', y, '\n', z)

x = 5
y = "John"
print(type(x))
print(type(y))

x = "John"
# is the same as
x = 'John'
print(x)

a = 4
A = "Sally"
#A will not overwrite a
print(a)
print(A)