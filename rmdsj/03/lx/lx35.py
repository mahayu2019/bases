#!/usr/bin/env python
# coding=utf-8

guests = ['米奇', '老鸭', 'kitty', '机器猫', '超人']
print(guests[2] + "无法参加")
guests[2] = '大力水手'
for gs in guests:
    print("欢迎" + gs + "参加派对!")