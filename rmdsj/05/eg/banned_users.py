#!/usr/bin/env python
# coding=utf-8

# 5.2.7  检查特定值是否包含在列表中
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:  # not in-->不包含,in-->包含
    print(user.title(), '你不在其内')
