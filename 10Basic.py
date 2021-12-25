# -*- coding: utf-8 -*-
# 面向对象编程


import types

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))


bart = Student("Bart Simpson", 59)

bart.print_score()


# 继承


def fn():
    pass

print(type(fn)==types.FunctionType)

#使用dir() 获得一个对象的所有属性和方法
print(dir('ABC'))

