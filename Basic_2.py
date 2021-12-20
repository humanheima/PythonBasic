# -*- coding: utf-8 -*-

# 使用list和tuple

classmates = ['Michael', 'Bob', 'Tracy']

print(classmates)

print("classmates 长度 = %d" %(len(classmates)))

print("第一个同学是:%s" %classmates[0])

classmates.append('Adam')

print("最后一个同学是:%s" %classmates[-1])


# 插入元素
classmates.insert(1,'Jack')

# 删除元素

print("删除末尾的元素 %s" %classmates.pop())

# 删除指定位置的元素
print("删除指定位置的元素 %s" %classmates.pop(1))


# tuple tuple和list非常类似，但是tuple一旦初始化就不能修改


classmates2 = ('Michael', 'Bob', 'Tracy')

# 不能修改，修改出错
# classmates2[1]="Hello"

print("tuple 第一个元素 %s" % classmates2[1])


