#!/usr/bin/env python
# coding=utf-8

# 6.4.2 在字典中存储列表
# 存储所点比萨的信息
pizza = {'crust': 'thick', 'toppings': ['mushrooms', 'extra cheese'], }

# 概述所点的比萨
print('你点的比萨' + pizza['crust'] + '-配料:')
for topping in pizza['toppings']:
    print('\t' + topping)
