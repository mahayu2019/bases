#!/usr/bin/env python
# coding=utf-8

'''
反转一个只有三位数的整数
输入123--输出321  ,输入900 输出9
'''


# 案例解法
def reverseInteger(number):
    h = int(number / 100)
    t = int(number % 100 / 10)
    z = int(number % 10)
    return 100 * z + 10 * t + h


# diy解法
def revInteger(number):
    num = str(number)
    h = num[-1]
    t = num[-2]
    z = num[-3]
    return h + t + z


if __name__ == '__main__':
    num = 900
    # ans = reverseInteger(num)
    ans = revInteger(num)
    print("输入值:", num)
    print("输出值:", ans)
