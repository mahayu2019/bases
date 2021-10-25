#!/usr/bin/env python
# coding=utf-8
import pretty_errors

# 6.3.1 遍历所有的键-值对
user_0 = {'username': 'efermi', 'first': 'enrico', 'last': 'fermi'}
print("items()方法,返回字典的键值对列表:")
print(user_0.items())
print("\n遍历输出字典中的键-值对")

for key, Value in user_0.items():  # key,value分别存储对应的键-值
    print("Key: " + key)
    print("Value: " + Value)

# 6.3.2 遍历所有键(keys)和值(values)
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'}
print("\n第二个字典")
print(favorite_language)

# 单独遍历字典中的键
print("\n单独遍历字典中的键:字典.keys()方法")
for name in favorite_language.keys():
    print(name)

# 单独遍历字典中的值
print("\n单独遍历字典中的键:字典.values()方法")
for va in favorite_language.values():
    print(va)

# DIY
x = "efermi"
if x in user_0.values():
    print("\nok")
else:
    print("no")
