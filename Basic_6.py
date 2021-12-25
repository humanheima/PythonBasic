# -*- coding: utf-8 -*-

import math

# 函数

print("abs(-20) = %d"%abs(-20))


# 定义函数
def my_abs(x:int):
    # 类型检查
    if not(isinstance(x,(int,float))):
        raise TypeError('bad operand type')
    if x>=0:
        return x
    else:
        return -x

print("my_abs(-20) = %d"%my_abs(-20))

# 函数返回多个值


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)


# 定义函数，有默认参数
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

# 第一函数，有默认参数
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

# 可变参数

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc(1,2,3))

nums = [1, 2, 3,4]

print(calc(*nums))

# 关键字参数

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

print(person('Adam', 45, gender='M', job='Engineer'))


extra = {'city': 'Beijing', 'job': 'Engineer'}

print(person('Jack', 24, **extra))


# 命名关键字参数


def person2(name, age, *, city, job):
    print(name, age, city, job)

print(person2('Jack', 24, city='Beijing', job='Android Engineer'))


# 递归函数

def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

print("fact(5) = %d"%fact(5))




# 尾递归优化函数

def fact2(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)




