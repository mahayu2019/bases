#!/usr/bin/env python
# coding=utf-8
import pretty_errors

number = input("输入一个数:")
number = int(number)

if number % 2 == 0:
    print(str(number) + "可以整除")
else:
    print(str(number) + "不可整除")
