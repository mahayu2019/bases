#!/usr/bin/env python
# coding=utf-8
import pretty_errors


# 被调用的类
def make_pizza(size, *toppings):
    print('尺寸:' + size)
    for tp in toppings:
        print(tp)
