#!/usr/bin/env python
# coding=utf-8
import pretty_errors

# 7.1.2 使用int()来获取数值输入
height = input("你的身高多少?")
height = int(height)

if height >= 36:
    print("\身高可行")
else:
    print("No!")
