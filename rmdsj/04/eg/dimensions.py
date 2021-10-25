#!/usr/bin/env python
# coding=utf-8
import pretty_errors

# 4.5.1 元组,元素值不可修改
dimensions = (200, 50, 30, 'a')
print("原始元组:" + dimensions.__str__())
print("读取元素[0]:" + dimensions[0].__str__())
print("读取元素[2]:" + dimensions[2].__str__())

# 4.5.2 遍历元组
print("\n遍历输出元素值:")
for ds in dimensions:
    print(ds)

# 4.5.3 修改原祖变量,重新给元组变量赋值
dimensions = ('A', 'B')
print("\n修改后的元组")
print(dimensions)
