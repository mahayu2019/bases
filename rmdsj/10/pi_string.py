#!/usr/bin/env python
# coding=utf-8
import pretty_errors

# 10.1.5  使用文件中的内容
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

# 10.1.6包含一百万位的大文件
filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string[:52] + "...")
print(len(pi_string))

# 10.1.7 圆周率是否含生日
birthday = input("输入你的生日:")
if birthday in pi_string:
    print('包含生日')
else:
    print('不包含')
