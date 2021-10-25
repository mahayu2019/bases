#!/usr/bin/env python
# coding=utf-8


# 6.1 一个简单的字典
alien_0 = {'color': 'green', 'points': 5}
print("字典:"+alien_0.__str__())
print(alien_0['color'])
print(alien_0['points'])

# 6.2.2 添加键-值对
print("\n字典修改前:\n"+alien_0.__str__())
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print("字典修改后(加入新键-值对):\n"+alien_0.__str__())

# 6.2.3 空字典中加入键值对
alien_1 = {}
print("\n空字典:"+alien_1.__str__())
alien_1['color'] = 'red'
alien_1['point'] = 10
print("加入键-值对:\n"+alien_1.__str__())

# 6.2.4 修改字典中的值
print("\n修改字典")
alien_2 = {'color': 'green'}
print('初始颜色:' + alien_2['color'])
alien_2['color'] = 'yellow'
print('修改后的颜色:' + alien_2['color'])

# 6.2.5 删除键-值对
print("\n删除键-值对")
alien_3={'color': 'green','points':5}
print(alien_3)
del alien_3['color']
print(alien_3)
