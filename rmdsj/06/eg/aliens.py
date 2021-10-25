#!/usr/bin/env python
# coding=utf-8

# 6.4.1 字典列表
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

# 创建30个外星人
aliens_2 = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens_2.append(new_alien)

# 显示前五个外星人
for alien in aliens_2[:5]:
    print(alien)
print('....')

# 创建了多少外星人
print("一共" + str(len(aliens_2)) + "个外星人")

# 前三个改成黄色,并修改相关键-值对
for alien in aliens_2[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'

for alien in aliens_2[:10]:
    print(alien)
