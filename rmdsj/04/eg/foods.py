#!/usr/bin/env python
# coding=utf-8
import pretty_errors

# 4.4.3 复制列表,必须用切片方式复制
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]  # 将my_food列表的副本传给fr
print("我的食物:" + my_foods.__str__())
print("朋友的的食物:" + friend_foods.__str__())

# 添加食物
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("\n各自添加元素后")
print("我的食物:" + my_foods.__str__())
print("朋友的的食物:" + friend_foods.__str__())
