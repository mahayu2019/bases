#!/usr/bin/env python
# coding=utf-8


# 3.3.1 sort()方法 永久性排序,列表顺序不可逆
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print("永久性排序--sort,无法恢复原序列")
print(cars)

# 逆序排列,加入参数reverse=True
cars.sort(reverse=True)
print(cars)

# 3.3.2  sorted()函数 临时排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\n临时排序--sorted,不改变原序列")
print(sorted(cars))
print("对比原序列")
print(cars)
print("使用reverse=True 逆序排列")
print(sorted(cars, reverse=True))

# 3.3.3 reverse()方法 反转列表
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\n原始列表")
print(cars)
cars.reverse()
print("reverse()方法 反转列表")
print(cars)

# 3.3.4 确定列表长度
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\n列表长度", len(cars))
