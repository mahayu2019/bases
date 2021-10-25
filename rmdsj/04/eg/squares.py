#!/usr/bin/env python
# coding=utf-8
import pretty_errors

squares = []
for value in range(1, 11):
    square = value ** 2  # 计算平方数
    squares.append(square)  # 填充列表

print("计算1-10的平方数,存入列表")
print(squares)
