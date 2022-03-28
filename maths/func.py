# 1,1,2,3,5,8,13,21,34,55
from time import time


def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


def fibo2(n):
    if n == 1 or n == 2:
        return 1
    a = 1
    b = 1
    for i in range(n - 2):
        a, b = b, a + b
    return b


for i in range(10, 38):
    ts = time()
    fibo(i)
    t1 = time() - ts
    ts = time()
    fibo2(i)
    t2 = time() - ts
    print(t1, t2)
