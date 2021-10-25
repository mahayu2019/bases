#!/usr/bin/env python
# coding=utf-8
import pretty_errors
from name_function import get_formatted_name

print("输入你的名字 按'q'退出")
while True:
    first = input("\n输入姓:")
    if first == 'q':
        break
    last = input("输入名:")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print("你的名字:" + formatted_name)
