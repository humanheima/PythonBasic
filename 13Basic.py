# -*- coding: utf-8 -*-

# 操作文件和目录

import os
import shutil

print(os.name)
# print(os.environ.get('PATH'))

# 查看当前目录的绝对路径:

print(os.path.abspath("."))

# 创建目录
if os.path.exists("testDir") == False:
    os.mkdir("testDir")
else:
    print("testDir 目录已经存在了")

# 删除目录

if os.path.exists("nn"):
    os.rmdir("nn")
else:
    print("nn 目录不存在")


tempDir = os.path.join("tempDir", "childDir")
print(tempDir)

if os.path.exists(tempDir) == False:
    os.makedirs(tempDir)
else:
    print(tempDir + "目录已经存在")

# split 文件路径和文件名

print(os.path.split("documents/doc_1.txt"))

doc_1Name = os.path.splitext("documents/doc_1.txt")

print("doc_1Name =", doc_1Name)


# 重命名

doc_1=os.path.join(".","documents/doc_1.txt")
if os.path.exists(doc_1):
    os.rename(doc_1,"documents/doc_2.txt")


# remove 文件

doc2 =os.path.join(".","doc_2.txt")
if(os.path.exists(doc2)):
   os.remove(doc2)


# 拷贝文件
shutil.copy("hello_world.py","hello_world2.py")