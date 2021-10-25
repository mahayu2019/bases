#!/usr/bin/env python
# coding=utf-8

guests = ['米奇', '老鸭', 'kitty', '机器猫', '超人', '路飞', '钢铁侠']
n = len(guests)
while n > 2:
    print(guests.pop() + "滚蛋")
    n = n - 1
for u in guests:
    print(u + "请继续")


while n > 0:
    n = len(guests) - 1
    print("杀"+guests[n])
    del guests[n]
    n-1

print(guests)