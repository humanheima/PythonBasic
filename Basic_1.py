# -*- coding: utf-8 -*-
# 注释
a = 100
if a >= 0:
    print(a)
else:
    print(-a)

print('Hello, %s' % 'world')
print('Hi, %s, you have $%d.' % ('Michael', 1000000))

# 整数{1:.1f}，index为1的参数，保留1位小数
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format("小明", 17.125))


# f-string

r = 2.5
s = 3.14 * r ** 2
print(f'The area of a circle with radius {r} is {s:.2f}')
