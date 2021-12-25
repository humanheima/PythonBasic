# -*- coding: utf-8 -*-

# 高阶函数


from functools import reduce

print(abs)
print(abs(10))

def add(x, y, f):
    return f(x) + f(y)

print(add(-5, 6, abs))


def f(x):
    return x * x

# 调用map函数
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])

print(list(r))

# 调用reduce函数

def add(x,y):
    return x + y

print(reduce(add, [1, 3, 5, 7, 9]))




