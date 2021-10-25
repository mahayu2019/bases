#!/usr/bin/env python
# coding=utf-8


# 7.2.4 使用break退出循环
prompt = "\n输入访问城市名称:"
prompt += "\n(输入 'quit' 结束程序.)"

while True:
    city = input(prompt)
    if city == 'quit':
        break  # 终止循环,退出程序
    else:
        print("我也想去" + city.title())

