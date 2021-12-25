# -*- coding: utf-8 -*-

# IO编程


from io import StringIO

# 写文件

try:
    f = open("README.md", "a")
    f.write("Hello world;")
finally:
    if f:
        f.close()


# 只读的方式打开文件

try:
    # 以读写的方式读取文本文件，读取二进制文件 可以用`rb`模式
    f = open("README.md", "r",encoding="utf-8")
    # 一次读取所有的内容
    # 如果文件很小，read()一次性读取最方便；
    # 如果不能确定文件大小，可以调用read(size)每次最多读取size个字节的内容。
    # 调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。因此，要根据需要决定怎么调用。
    print(f.read())
finally:
    if f:
        f.close()


# 对try/catach的简化
with (open("README.md", "r")) as f1:
    print(f1.read())


# 读写内存中是String

str = StringIO()

str.write("hello")

str.write(" ")

str.write("world")

print(str.getvalue())

readStr = StringIO("Hello!\nHi!\nGoodbye!")

while True:
    s =readStr.readline()
    if(s ==''):
        break
    print(s.strip())


# ByteIO 读写二进制文件

