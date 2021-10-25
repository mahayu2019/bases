#!/usr/bin/env python
# coding=utf-8
import pretty_errors


# 11.1 测试函数
def get_formatted_name(first, last, middle=''):
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()
