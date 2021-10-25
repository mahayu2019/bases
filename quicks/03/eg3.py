#!/usr/bin/env python
# coding=utf-8

'''
函数
'''


# 参数
def hello(name):
    print('hello ' + name)


hello('马克')
hello('胡伟156')


# 返回值--return
def getnum(num):
    total = 5 + num
    return total

print(getnum(98))