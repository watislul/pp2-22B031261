#1 by function and yield
def squares(end_point):
    current = 1
    while(current ** 2 <= end_point):
        yield current ** 2
        current += 1

#n = squares(int(input()))
#print(*n, sep= ', ')
#2 by function and yield
def Evennumbers(end_point):
    current = 0
    while(current <= end_point):
        yield current
        current += 2

#n = Evennumbers(int(input()))
#print(*n, sep= ', ')
#3
def div(end_point):
    current = 0
    while(current <= end_point):
        yield current
        current += 12
#n = div(int(input()))
#print(*n)
#4
def square(current,end_point):
    while(current ** 2 <= end_point):
        yield current ** 2
        current += 1

#cur = int(input())
#end = int(input())
#for i in square(cur, end):
    #print(i)
#5
def down(current):
    while(current >= 0):
        yield current
        current -= 1

#n = int(input())
#print(*down(n), sep=' ! ')