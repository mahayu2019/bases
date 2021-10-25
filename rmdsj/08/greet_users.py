#!/usr/bin/env python
# coding=utf-8
import pretty_errors


# 8.4 传递列表
def greet_users(names):
    for name in names:
        msg = "Hello," + name.title() + "!"
        print(msg)


usernames = ['张三', '李四', '王五']
greet_users(usernames)
