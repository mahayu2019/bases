#!/usr/bin/env python
# coding=utf-8
import pretty_errors


# 8.3.3  返回字典
def build_person(first_name, last_name):
    """返回一个包含个人信息的字典"""
    person = {'first': first_name, 'last': last_name}
    return person


musician = build_person('jimi', 'hendrix')
print(musician)


def build_person(first_name, last_name, age=''):
    person = {'first': first_name, 'last': last_name}
    if age:  # 如果默认值有加入,则增加一个键值对
        person['age'] = age
    return person


musician = build_person('Tom', 'hack', 35)
print(musician)
