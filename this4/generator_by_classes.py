#1 return all number in square till the the our N
class squares():
    def __init__(self, end):
        self.current = 1
        self.end_point = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current ** 2 > self.end_point:
            raise StopIteration()
        x = self.current
        self.current += 1
        return x ** 2
'''
n = int(input())
for i in squares(n):
    print(i)
'''
#2
class EvenNumber():
    def __init__(self, end):
        self.current = 0
        self.end_point = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end_point:
            raise StopIteration()
        x = self.current
        self.current += 2
        return x

#n = int(input())
#print(*EvenNumber(n), sep= ', ')
#3
class div():
    def __init__(self, end):
        self.current = 0
        self.end_point = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end_point:
            raise StopIteration()
        x = self.current
        self.current += 12
        return x
#n = int(input())
#print(*div(n))
#4
class Square():
    def __init__(self, cur, end):
        self.current = cur
        self.end_point = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current ** 2 > self.end_point:
            raise StopIteration()
        x = self.current
        self.current += 1
        return x ** 2

#cur = int(input())
#end = int(input())

#for i in Square(cur, end):
#    print(i)

#5
class down():
    def __init__(self, cur):
        self.current = cur

    def __iter__(self):
        return self

    def __next__(self):
        if self.current == -1:
            raise StopIteration()
        x = self.current
        self.current -= 1
        return x

#n = int(input())
#print(*down(n), sep= ', ')

