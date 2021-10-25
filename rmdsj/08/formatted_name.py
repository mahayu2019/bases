#!/usr/bin/env python
# coding=utf-8
import pretty_errors


# 8.3.1 返回简单值
# 中间名放在最后,用默认形参指定,默认参数必须在非默认参数之后
def get_formatted_name(first_name, last_name, middel_name=''):
    if middel_name:  # 如果有中间名,则加入
        full_name = first_name + ' ' + middel_name + ' ' + last_name
    else:  # 没有中间名,省略
        full_name = first_name + ' ' + last_name

    return full_name.title()


# 没有中间名的调用
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
# 有中间名的调用
musician = get_formatted_name('Tom', 'joker', 'make')
print(musician)
