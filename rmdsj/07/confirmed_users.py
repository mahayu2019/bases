#!/usr/bin/env python
# coding=utf-8

# 7.3.1 在列表间移动元素
unconfirmed_users = ['alice', 'brian', 'candace']  # 待验证用户列表
confirmed_users = []  # 存储已验证用户的空列表

while unconfirmed_users:
    current_user = unconfirmed_users.pop()  # 从待验证列表中弹出并赋值
    print("通过用户:" + current_user.title())
    confirmed_users.append(current_user)  # 将验证的用户加入新列表

print("已验证的用户")
for confirmed_users in confirmed_users:  # 输出新列表内容
    print(confirmed_users.title())
