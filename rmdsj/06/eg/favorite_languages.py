#!/usr/bin/env python
# coding=utf-8
import pretty_errors


# 6.2.6 由类似对象组成的字典
favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'}

print("Sarah's is " + favorite_language['sarah'].title() + ".")

# 遍历字典中嵌套的列表
favorite_language_2 = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
}

for name, language in favorite_language_2.items():
    print('姓名:' + name)
    for lg in language:
        print('\t' + lg)
