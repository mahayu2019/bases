#!/usr/bin/env python
# coding=utf-8
import pretty_errors

# 8.4.1 在函数中修改列表
# 创建一个要打印的列表
unprinted_designs = ['ipcase', 'robot', 'dodec']
completed_models = []

while unprinted_designs:
    current_design = unprinted_designs.pop()  # list的pop函数逐个弹出元素放入函数使用

    print("打印文件:" + current_design)
    completed_models.append(current_design)  # list的append加入弹出的元素形成新list

print("\n已打印文件:")
for completed_model in completed_models:
    print(completed_model)
