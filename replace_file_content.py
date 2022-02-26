# -*- coding: utf-8 -*-

# IO编程
# 替换文件中的内容


from io import StringIO

import sys
import re,os
# 写文件

# with open("bundle_info.json", "r+") as f:
#     alllines = f.readlines()
#     for eachline in alllines:
#         print(eachline)
#         print()


# 方法2 python 使用正则表达式 替换文件内容 re.sub 方法替换 

# def alter(file,old_str,new_str):

#     with open(file, "r", encoding="utf-8") as f1,open("%s.bak" % file, "w", encoding="utf-8") as f2:
#         for line in f1:
#             f2.write(re.sub(old_str,new_str,line))
#     os.remove(file)
#     os.rename("%s.bak" % file, file)

# alter("file1.json", "android", "lite")

# 将替换的字符串写到一个新的文件中，然后将原文件删除，新文件改为原来文件的名字

# 定义 alter1方法。
def alter1(file,old_str,new_str):
    """
    :param file: 文件路径
    :param old_str: 需要替换的字符串
    :param new_str: 替换的字符串
    :return: None
    """
    with open(file, "r", encoding="utf-8") as f1,open("%s.bak" % file, "w", encoding="utf-8") as f2:
        for line in f1:
            if old_str in line:
                line = line.replace(old_str, new_str)
            f2.write(line)
    os.remove(file)
    os.rename("%s.bak" % file, file)

# alter1("file1.json", "isBuildIn", "isBuildInn")


# 修改原文件方式

def alter(file,old_str,new_str):
    """
    替换文件中的字符串
    :param file:文件名
    :param old_str:就字符串
    :param new_str:新字符串
    :return:
    """
    file_data = ""
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            if old_str in line:
                line = line.replace(old_str,new_str)
            file_data += line
    with open(file,"w",encoding="utf-8") as f:
        f.write(file_data)

#alter("file1.json", "isBuildInn", "isBuildIn")

# 获取外部传递过来的参数
print(sys.argv[1])
alter(sys.argv[1], "lite", "android")
