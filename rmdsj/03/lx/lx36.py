#!/usr/bin/env python
# coding=utf-8

guests = ['米奇', '老鸭', 'kitty', '机器猫', '超人']
print('换大桌')
guests.insert(0,'路飞')   #insert需要指定元素索引和值
guests.insert(2, '钢铁侠') #insert需要指定元素索引和值
guests.append('杰克')
for gs in guests:
    print("欢迎" + gs + "参加派对!")
