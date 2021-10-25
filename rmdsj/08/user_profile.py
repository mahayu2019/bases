#!/usr/bin/env python
# coding=utf-8
import pretty_errors


# 8.5.2 使用任意数量的关键字实参
def build_profile(first, last, **user_info):  # 形参带2个*号,代表字典
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():  # 把接收到的关键字实参存入字典
        profile[key] = value
    return profile


# 调用函数时，形参必须以键-值对的方式传入
user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)
