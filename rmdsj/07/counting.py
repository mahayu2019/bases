#!/usr/bin/env python
# coding=utf-8
import pretty_errors


# 7.2.1 使用while循环
current_number = 1
while current_number <= 10:
    print(current_number)
    current_number += 1

# 7.2.5 在循环中使用continue
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue  # 返回,重新进入循环
    print(current_number)
