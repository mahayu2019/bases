#!/usr/bin/env python
# coding=utf-8
import pretty_errors

filename = 'pi_digits.txt'

# 10.1.1 读取整个文件
with open(filename) as file_object:
    contents = file_object.read()
    print(contents)

# 10.1.3逐行读取
with open(filename) as file_object:
    for line in file_object:
        print(line)

# 10.1.4 创建一个包含文件各行内容的列表
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
