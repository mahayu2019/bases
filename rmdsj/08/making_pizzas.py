#!/usr/bin/env python
# coding=utf-8
import pizzamk  # 导入整个模块

pizzamk.make_pizza('9', '沙拉', '奶酪', '三文鱼')

# from pizzamk import make_pizza #导入指定的函数
# make_pizza('9', '沙拉', '奶酪', '三文鱼')

#别名
from pizzamk import make_pizza as mp

mp('8', 'wq', 'wqe')
