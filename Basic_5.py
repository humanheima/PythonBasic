# -*- coding: utf-8 -*-

# 使用dict和set

# dictionary 字典 ，对应 map

# 引用其他地方的函数，有问题，Basic_6中的输出语句也会打印
from Basic_6 import my_abs


print("my_abs(-20) = %d"%my_abs(-20))



d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}

print(d['Bob'])


# 删除元素
print("删除元素 %d" %(d.pop('Tracy')))


# set 集合
s = set([1, 1, 2, 2, 3, 3])

print("set 元素 %s"%s)

s.add(4)

print("set 元素 %s"%s)


