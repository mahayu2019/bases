#!/usr/bin/env python
# coding=utf-8
import pretty_errors

# 7.3.3 使用用户输入来填充字典
rs = {}  # 准备一个空字典

# 设置一个标志,之处调查是否继续
polling_active = True

while polling_active:
    # 提示输入被调查者的名字和回答
    name = input("\n你的名字?")
    response = input("你的选择")

    # 将答案存储到字典中
    rs[name] = response  # 使用键-值对方式存入字典中

    # 询问是否继续
    repeat = input("继续?(yes/no)")
    if repeat == 'no':
        polling_active = False

print("\n--- 统计 ---")
for name, response in rs.items():  # 循环从字典中输出键-值对
    print(name + "选择" + response + ".")
