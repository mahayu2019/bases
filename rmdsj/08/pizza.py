#!/usr/bin/env python
# coding=utf-8
import pretty_errors


# 8.5 传递任意数量的实参
# 形参前的*号(一个*号是元组,两个**号是字典),
# 创建一个空元组,将所有接收到的实参封装在此元组中

def make_pizza(*toppings):
    print(toppings)


make_pizza("番茄")
make_pizza("胡萝卜", '土豆', "辣椒")


# 用循环输出
def make_pizza(*toppings):
    for tp in toppings:
        print(tp)


make_pizza("番茄")
make_pizza("胡萝卜", '土豆', "辣椒")


# 8.5.1 结合使用位置实参和任意数量实参

def make_pizza(size, *toppings):  # *toopings 只有一个*号是元组形式
    print("\n披萨尺寸:" + str(size) + "\n配料:")
    for pl in toppings:
        print("-" + pl)


make_pizza(15, '三文鱼', '火腿', '沙拉')
make_pizza(8, '黄瓜')

