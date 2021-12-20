# -*- coding: utf-8 -*-

import math
# 条件判断

age = 20
if age >= 18:
    print('your age is', age)
    print('adult')


s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')

    
height = 1.75
weight = 80.5

bmi =math.pow((height/weight),2)

if bmi < 18.5:
    print('过轻')
elif bmi <25:
    print('正常')
elif bmi < 32:
    print('肥胖')
else:
    print('严重肥胖')


