#1
'''
a = [1,2,3,4,5,4,3,2]
b = [str(index) for index in a]
s = '*'.join(b)
print(eval(s))

print(eval('*'.join([str(index) for index in list(map(int, input().split()))])))

print(eval('*'.join(input().split())))
'''
#2
'''
stroka = input()
lower = [
    1 if str(index).islower() else 0
    for index in stroka
]

upper = [
    1 if str(index).isupper() else 0
    for index in stroka
]
print('lower: ',sum(lower))
print('upper: ',sum(upper))
'''

#3
'''
s = input()
t = s[::-1]
print(hash(s))
print(hash(t))
if hash(s) == hash(t):
    print('Palindrom')
else:
    print('Not Palindrom')
'''
#4
from time import sleep
'''
num = int(input())
milliseconds = int(input())
sleep(milliseconds / 1000)
print(f'Square root of {num} after {milliseconds} milliseconds is {num ** 0.5}')
'''
#5
'''
a = (
    index == 'True' for index in input().split
)
x = all(a)
'''