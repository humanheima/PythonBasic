# -*- coding: utf-8 -*-

from collections.abc import Iterable

import os # 导入os模块，模块的概念后面讲到
# 高级特性

# 切片

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

#从0开始取到index=3结束。
result=L[0:3]


print("result = %s "%result)

# 迭代

print(isinstance("abc",Iterable))

# 列出当前目录下的文件和目录
print([d for d in os.listdir('.')])

# 生成器

g = (x * x for x in range(10))
for n in g:
    print(n)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

fib(6)

# 注意 yield  如果一个函数定义中包含yield关键字，
# 那么这个函数就不再是一个普通函数，而是一个generator函数，调用一个generator函数将返回一个generator
def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

f =fib2(6)

for n in f:
    print("n in f = %d"%n)






