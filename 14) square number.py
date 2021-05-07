import math, random #모듈사용
def sqrts(num):
    a = [0, 0, 0, 0]
    while a[0] ** 2 + a[1] ** 2 + a[2] ** 2 + a[3] ** 2 != num:
        a[0] = int(random.randint(0, int(math.sqrt(num)))) #randint정수리턴인데 왜  int?
        a[1] = int(random.randint(0, int(math.sqrt(num))))
        a[2] = int(random.randint(0, int(math.sqrt(num))))
        a[3] = int(random.randint(0, int(math.sqrt(num))))
    return a
print(sqrts(7))
