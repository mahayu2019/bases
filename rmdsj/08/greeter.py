#!/usr/bin/env python
# coding=utf-8
import pretty_errors


# 8.1 定义函数
def greet_user():
    print("hello user")


greet_user()


# 8.1.1 向函数传递信息
def greet_user(uname):
    print("hello " + uname)


greet_user('mahayu')


# 8.3.4 结合使用函数和while循环
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()


# 用无限循环获取输入
while True:
    print("\n输入名字:(输入'q'结束)")
    f_name = input("First name:")
    if f_name == 'q':
        break
    l_name = input("Last name:")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\n你好," + formatted_name + "!")
