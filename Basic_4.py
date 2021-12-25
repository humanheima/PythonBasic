# -*- coding: utf-8 -*-

# 循环

names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print("Hello %s"%name)


sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

sum1 = 0
for x in range(101):
    sum1 = sum1 + x
print(sum1)


n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')
