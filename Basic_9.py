# -*- coding: utf-8 -*-

# Python 命令行参数


# 1. 使用 sys 的 sys.argv 来获取命令行参数：
#
# python -u "/Users/xmly/python_project/Basic_9.py" test  
# 输出结果：
# 参数个数为: 2 个参数。
# 参数列表: ['/Users/xmly/python_project/Basic_9.py', 'test']
#

from functools import reduce

import sys,getopt

print('参数个数为:', len(sys.argv), '个参数。')
print('参数列表:', str(sys.argv))

# 2. 使用getopt模块 

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print('test.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('test.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print('输入的文件为：', inputfile)
   print('输出的文件为：', outputfile)

if __name__ == "__main__":
   main(sys.argv[1:])





